import json
import streamlit as st

class missingFieldError(Exception):
    def __init__(self, field_name):
        super().__init__(f"Eksik alan: {field_name}")
        
class JobApplication:
    def __init__(self, applicant):
        if "name" not in applicant:
            raise missingFieldError("name")
        if "email" not in applicant:
            raise missingFieldError("email")
        self.name = applicant["name"]
        self.email = applicant["email"]
        self.job_category = applicant["job_category"]
        
    def evalute(self):
        return "Başvuru değerlenidrme sürecinde"
    
class SoftwareEngineerApplication(JobApplication):
    def __init__(self, applicant):
        super().__init__(applicant)
        self.experience = applicant.get("experience_year", 0)
    def evalute(self):
        return f"{self.name} için uygunluk durumu: {'kabul edildi' if self.experience >=3 else 'Reddedildi'}
    
st.title("Akıllı iş başvurusu takip sistemi")
job_json = st.text_area("iş başvurusu bilgilerini json formatında girin")
if st.button("başvuruyu değerlendir"):
    try:
        job_data = json.loads(job_json)
        job_category = job_data.get("applicant", {})get("job_category", "")
        if job_category == "SoftwareEngineer":
            application = SoftwareEngineerApplication(job_data["applicant"])
        else:
            st.error("geçersiz iş kategorisi!")
            application = None
        if application:
            st.success(application.evalute())
    except missingFieldError as mfe:
        st.error(f"Eksik bilgi hatası: {mfe}")
    except Exception as e:
        st.error(f"Hata: {e}")