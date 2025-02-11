import tkinter as tk
import subprocess
import re

def get_power_options():
    result = subprocess.run(["powercfg", "/L"], capture_output=True, text=True)
    lines = result.stdout.splitlines()
    plans = []
    guid_dict = {}
    for line in lines:
        match = re.search(r'([a-f0-9\-]+)\s+\((.*?)\)', line)
        if match:
            guid = match.group(1)
            plan_name = match.group(2)
            plans.append(plan_name)
            guid_dict[plan_name] = guid
    return plans, guid_dict

def get_current_power_plan(guid_dict):
    result = subprocess.run(["powercfg", "/GETACTIVESCHEME"], capture_output=True, text=True)
    active_guid = result.stdout.split(': ')[1].split(' ')[0]
    for name, guid in guid_dict.items():
        if guid.lower() == active_guid.lower():
            return name

def change_power_plan(selected_plan, window):
    guid_dict = get_power_options()[1]
    selected_guid = guid_dict.get(selected_plan)
    if selected_guid:
        subprocess.run(["powercfg", "/S", selected_guid])

def show_power_options(frame):
    # Güç planı seçeneklerini al
    power_plans, guid_dict = get_power_options()
    
    # Seçili plan için StringVar oluştur
    selected_plan = tk.StringVar(value=get_current_power_plan(guid_dict))  # Varsayılan olarak aktif planı seç

    # Önceki içerikleri temizle
    for widget in frame.winfo_children():
        widget.destroy()

    # Radiobutton'lar için ayrı bir çerçeve oluştur
    radio_frame = tk.Frame(frame, bg="#242424")
    radio_frame.pack(pady=5)

    # Güç planı seçeneklerini oluştur
    for plan in power_plans:
        radiobutton = tk.Radiobutton(
            radio_frame,
            text=plan,
            variable=selected_plan,
            value=plan,
            bg="#242424",
            fg="white",
            activebackground="#242424",
            activeforeground="white",
            selectcolor="#242424",
            font=("Calibri", 11)
        )
        radiobutton.pack(anchor='w', padx=55, pady=0)  # Radiobutton'ları sağa kaydırmak için boşluk ekleyin

    # Güç planını değiştirmek için buton ekle
    select_button = tk.Button(
        frame,
        text="Select Power Plan",
        command=lambda: change_power_plan(selected_plan.get(), frame),
        bg="#944e2b",
        fg="white",
        font=("Calibri", 12),
        relief="flat",
        overrelief="raised",
        activebackground="#b55a38",
        activeforeground="white",
        width=20,
        height=2
    )
    select_button.pack(pady=(5, 5))  # Butonu yukarı çekmek için pady değerini ayarlayın

