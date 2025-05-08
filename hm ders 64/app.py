import streamlit as st
import pyodbc
import os
from dotenv import load_dotenv
import pandas as pd

from sqlalchemy import create_engine
import urllib
# .env dosyasını yükle
load_dotenv()

# SQLAlchemy bağlantısı (read işlemleri için)
def get_connection():
    params = urllib.parse.quote_plus(
        "DRIVER={ODBC Driver 17 for SQL Server};SERVER=DESKTOP-1P0456N;DATABASE=E_Commerce;trusted_connection=yes;"
    )
    return create_engine("mssql+pyodbc:///?odbc_connect=%s" % params)

# PyODBC bağlantısı (write işlemleri için cursor kullanımı için)
def get_raw_connection():
    return pyodbc.connect("DRIVER={ODBC Driver 17 for SQL Server};SERVER=DESKTOP-1P0456N;DATABASE=E_Commerce;trusted_connection=yes;")

# Sayfa yapılandırması
st.set_page_config(page_title="Stok Yönetim Sistemi", page_icon="📦", layout="wide")


# Sidebar menü
def sidebar():
    with st.sidebar:
        st.image("https://inciflo.com/wp-content/uploads/2024/06/stock-management-system-min.jpg", width=100)
        st.title("Stok Yönetim Sistemi")
        menu = st.radio("Menü", ["Ürün Yönetimi", "Kategori Yönetimi", "Stok Hareketleri", "Raporlar"])
        st.markdown("---")
        if st.button("Veritabanını Yenile"):
            st.experimental_rerun()
        return menu


# Ürün Yönetimi Sayfası
def product_management():
    st.header(" Ürün Yönetimi")
    tab1, tab2, tab3 = st.tabs(["Ürün Listesi", "Yeni Ürün Ekle", "Ürün Güncelle"])

    with tab1:
        conn = get_connection()
        products = pd.read_sql("""
            SELECT p.ProductID, p.ProductName, c.CategoryName, p.UnitPrice, p.UnitsInStock
            FROM Products p
            JOIN Categories c ON p.CategoryID = c.CategoryID
            ORDER BY p.ProductName
        """, conn)
        st.dataframe(products, use_container_width=True, hide_index=True,
                     column_config={
                         "ProductID": "ID",
                         "ProductName": "Ürün Adı",
                         "CategoryName": "Kategori",
                         "UnitPrice": st.column_config.NumberColumn("Fiyat", format="%.2f ₺"),
                         "UnitsInStock": "Stok"
                     })

    with tab2:
        with st.form("add_product_form"):
            cols = st.columns(2)
            name = cols[0].text_input("Ürün Adı*")
            category_id = cols[1].number_input("Kategori ID*", min_value=1, step=1)
            cols = st.columns(2)
            price = cols[0].number_input("Fiyat*", min_value=0.0, step=0.1, format="%.2f")
            stock = cols[1].number_input("Başlangıç Stok*", min_value=0, step=1)
            if st.form_submit_button("Ürün Ekle"):
                if name and category_id and price is not None:
                    conn = get_raw_connection()
                    cursor = conn.cursor()
                    cursor.execute("""
                        INSERT INTO Products (ProductName, CategoryID, UnitPrice, UnitsInStock)
                        VALUES (?, ?, ?, ?)
                    """, name, category_id, price, stock)
                    conn.commit()
                    conn.close()
                    st.success("Ürün başarıyla eklendi!")
                    st.rerun()
                else:
                    st.error("Lütfen zorunlu alanları doldurun (*)")

    with tab3:
        conn = get_connection()
        active_products = pd.read_sql("SELECT ProductID, ProductName FROM Products", conn)
        if not active_products.empty:
            selected_product = st.selectbox(
                "Güncellenecek Ürün",
                active_products.apply(lambda x: f"{x['ProductID']} - {x['ProductName']}", axis=1))
            product_id = int(selected_product.split(" - ")[0])
            product_info = pd.read_sql(f"SELECT * FROM Products WHERE ProductID = {product_id}", conn).iloc[0]

            with st.form("update_product_form"):
                new_name = st.text_input("Ürün Adı", value=product_info['ProductName'])
                cols = st.columns(2)
                new_price = cols[0].number_input("Fiyat", value=float(product_info['UnitPrice']))
                new_category = cols[1].number_input("Kategori ID", value=product_info['CategoryID'])
                discontinued = st.checkbox("Üretimden Kaldır", value=bool(product_info['Discontinued']))

                if st.form_submit_button("Güncelle"):
                    conn = get_raw_connection()
                    cursor = conn.cursor()
                    cursor.execute("""
                        UPDATE Products
                        SET ProductName = ?, UnitPrice = ?, CategoryID = ?, Discontinued = ?
                        WHERE ProductID = ?
                    """, new_name, new_price, new_category, discontinued, product_id)
                    conn.commit()
                    conn.close()
                    st.success("Ürün başarıyla güncellendi!")
                    st.rerun()
        else:
            st.warning("Güncellenecek aktif ürün bulunamadı")


# Kategori Yönetimi Sayfası
def category_management():
    st.header(" Kategori Yönetimi")
    tab1, tab2 = st.tabs(["Kategori Listesi", "Yeni Kategori Ekle"])
    with tab1:
        conn = get_raw_connection()
        categories = pd.read_sql(
            "SELECT CategoryID, CategoryName, Description FROM Categories",
            conn)
        #conn.close()
        st.dataframe(categories,
                     use_container_width=True,
                     hide_index=True,
                     column_config={
                         "CategoryID": "ID",
                         "CategoryName": "Kategori Adı",
                         "Description": "Açıklama"
                     })
    with tab2:
        with st.form("add_category_form"):
            name = st.text_input("Kategori Adı*")
            description = st.text_area("Açıklama")
            if st.form_submit_button("Kategori Ekle"):
                if name:
                    conn = get_raw_connection()
                    cursor = conn.cursor()
                    cursor.execute(
                        "INSERT INTO Categories (CategoryName, Description) VALUES (?, ?)",
                        name, description if description else None)
                    conn.commit()
                    #conn.close()
                    st.success("Kategori başarıyla eklendi!")
                    st.rerun()
                else:
                    st.error("Lütfen kategori adını girin")


# Stok Hareketleri Sayfası
def stock_transactions():
    st.header(" Stok Hareketleri")
    tab1, tab2, tab3 = st.tabs(
        ["Stok Girişi", "Stok Çıkışı", "Hareket Geçmişi"])
    with tab1:
        with st.form("stock_in_form"):
            conn = get_raw_connection()
            products = pd.read_sql(
                "SELECT ProductID, ProductName FROM Products",
                conn)
            #conn.close()
            selected_product = st.selectbox(
                "Ürün",
                products.apply(
                    lambda x: f"{x['ProductID']} - {x['ProductName']}",
                    axis=1))
            product_id = int(selected_product.split("-")[0])
            quantity = st.number_input("Miktar", min_value=1, step=1)
            notes = st.text_area("Notlar")
            if st.form_submit_button("Stok Girişi Yap"):
                conn = get_raw_connection()
                cursor = conn.cursor()
                cursor.execute("{CALL sp_AddStock(?, ?, ?)}", product_id,
                               quantity, notes if notes else None)
                conn.commit()
                #conn.close()
                st.success("Stok girişi başarıyla kaydedildi!")
                st.rerun()
    with tab2:
        with st.form("stock_out_form"):
            conn = get_connection()
            products = pd.read_sql(
                """
            SELECT p.ProductID, p.ProductName
            FROM Products p
            WHERE p.Discontinued = 0 AND p.UnitsInStock > 0
            """, conn)
            #conn.close()
            if not products.empty:
                selected_product = st.selectbox(
                    "Ürün",
                    products.apply(
                        lambda x: f"{x['ProductID']} - {x['ProductName']}",
                        axis=1))
                product_id = int(selected_product.split(" - ")[0])
                quantity = st.number_input("Miktar", min_value=1, step=1)
                notes = st.text_area("Notlar")
                if st.form_submit_button("Stok Çıkışı Yap"):
                    conn = get_connection()
                    cursor = conn.cursor()
                    try:
                        cursor.execute("{CALL sp_RemoveStock(?, ?, ?)}",
                                       product_id, quantity,
                                       notes if notes else None)
                        conn.commit()
                        st.success("Stok çıkışı başarıyla kaydedildi!")
                        st.experimental_rerun()
                    except Exception as e:
                        st.error(f"Hata: {str(e)}")

                else:
                    st.warning("Stoğu olan aktif ürün bulunamadı")
    with tab3:
        conn = get_raw_connection()
        products = pd.read_sql("SELECT ProductID, ProductName FROM Products",
                               conn)
        #conn.close()
        selected_product = st.selectbox(
            "Ürün Seçin",
            products.apply(lambda x: f"{x['ProductID']} - {x['ProductName']}",
                           axis=1))
        product_id = int(selected_product.split(" - ")[0])
        conn = get_raw_connection()
        history = pd.read_sql(
            f"{{CALL sp_GetProductStockHistory({product_id})}}", conn)
        #conn.close()
        if not history.empty:
            history['TransactionDate'] = pd.to_datetime(
                history['TransactionDate']).dt.strftime('%d.%m.%Y %H:%M')
            st.dataframe(history,
                         use_container_width=True,
                         hide_index=True,
                         column_config={
                             "TransactionID": "ID",
                             "TransactionType": "Hareket Türü",
                             "Quantity": "Miktar",
                             "TransactionDate": "Tarih",
                             "Notes": "Notlar"
                         })
        else:
            st.info("Bu ürüne ait stok hareketi bulunamadı")


# Raporlar Sayfası
def reports():
    st.header(" Raporlar")
    tab1, tab2 = st.tabs(["Ürün Detayları", "Stok Değeri"])
    with tab1:
        conn = get_connection()
        product_details = pd.read_sql("SELECT * FROM vw_ProductDetails", conn)
        #conn.close()
        st.dataframe(product_details,
                     use_container_width=True,
                     hide_index=True,
                     column_config={
                         "ProductID":
                         "ID",
                         "ProductName":
                         "Ürün Adı",
                         "CategoryName":
                         "Kategori",
                         "UnitPrice":
                         st.column_config.NumberColumn("Fiyat",
                                                       format="%.2f ₺"),
                         "UnitsInStock":
                         "Stok",
                         "SupplierCount":
                         "Tedarikçi Sayısı"
                     })
    with tab2:
        conn = get_connection()
        categories = pd.read_sql(
            "SELECT CategoryID, CategoryName FROM Categories", conn)
        #conn.close()
        selected_category = st.selectbox(
            "Kategori Seçin (Tümü için boş bırakın)",
            ["Tüm Kategoriler"] + categories.apply(
                lambda x: f"{x['CategoryID']} - {x['CategoryName']}",
                axis=1).tolist())
        if selected_category == "Tüm Kategoriler":
            category_id = None
        else:
            category_id = int(selected_category.split(" - ")[0])
            conn = get_connection()
        if category_id:
            inventory_value = pd.read_sql(
                f"SELECT dbo.fn_CalculateInventoryValue({category_id}) AS InventoryValue",
                conn)
            category_name = categories[categories['CategoryID'] ==
                                       category_id]['CategoryName'].values[0]
            st.metric(f"{category_name} Kategorisi Toplam Stok Değeri",
                      f"{inventory_value.iloc[0]['InventoryValue']:,.2f} ₺")
        else:
            inventory_value = pd.read_sql(
                "SELECT dbo.fn_CalculateInventoryValue(NULL) AS InventoryValue",
                conn)
            st.metric("Toplam Stok Değeri",
                      f"{inventory_value.iloc[0]['InventoryValue']:,.2f} ₺")
            # Kategorilere göre stok değeri grafiği
            category_values = pd.read_sql(
                """
            SELECT c.CategoryName, SUM(p.UnitPrice * p.UnitsInStock) AS TotalValue
            FROM Products p
            JOIN Categories c ON p.CategoryID = c.CategoryID
            WHERE p.Discontinued = 0
            GROUP BY c.CategoryName
            ORDER BY TotalValue DESC
            """, conn)
            #conn.close()
            if not category_values.empty:
                st.bar_chart(category_values.set_index('CategoryName'),
                             use_container_width=True)


# Ana Uygulama
def main():
    menu = sidebar()
    if menu == "Ürün Yönetimi":
        product_management()
    elif menu == "Kategori Yönetimi":
        category_management()
    elif menu == "Stok Hareketleri":
        stock_transactions()
    elif menu == "Raporlar":
        reports()


if __name__ == "__main__":
    main()
