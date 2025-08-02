Streamlit"cd interface
streamlit run app.py
# interface/app.py

import streamlit as st
import json

# --- تحميل البيانات ---
def load_data():
    with open("../data/quran_original.json", "r", encoding="utf-8") as f:
        quran = json.load(f)

    with open("../data/quran_mizan.json", "r", encoding="utf-8") as f:
        mizan = json.load(f)

    return quran, mizan

# --- البحث عن الميزان لكل آية ---
def find_mizan(verse_id, mizan_data):
    for item in mizan_data:
        if item["verse_id"] == verse_id:
            return item["mizan"]
    return None

# --- واجهة Streamlit ---
st.set_page_config(page_title="ميزان سورة الفاتحة", layout="centered", page_icon="📖")
st.title("📖 ميزان سورة الفاتحة")
st.write("تحليل تفاعلي لآيات سورة الفاتحة ضمن مشروع لسان آدم بقوة البيان.")

quran, mizan_data = load_data()

for verse in quran["verses"]:
    with st.expander(f"آية {verse['id']}: {verse['text_arabic']}", expanded=True):
        mizan = find_mizan(verse["id"], mizan_data)
        if mizan:
            st.markdown(f"**🔹 نوع البيان:** {mizan.get('type', '')}")
            st.markdown(f"**🔸 النية:** {mizan.get('intent', mizan.get('primary_intent', ''))}")
            st.markdown(f"**🔹 التركيب:** {', '.join(mizan.get('structure', []))}")
            st.markdown(f"**🔸 عدد الحروف:** {mizan.get('letter_count', '')}")
            if mizan.get("is_balanced_with_basmala"):
                st.success("✅ هذه الآية متوازنة مع البسملة.")
        else:
            st.warning("❗ لا يوجد تحليل ميزاني لهذه الآية.")