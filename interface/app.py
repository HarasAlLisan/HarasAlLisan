import streamlit as st
import json

# --- تحميل نصوص القرآن (نظيف) ---
def load_clean_text():
    with open("../data/quran_clean.json", "r", encoding="utf-8") as f:
        clean_data = json.load(f)
    return clean_data

# --- تحميل بيانات الميزان المفصلة ---
def load_mizan():
    with open("../data/quran_fatiha_mizan.json", "r", encoding="utf-8") as f:
        mizan_data = json.load(f)
    return mizan_data

# --- إيجاد ميزان الآية حسب رقمها ---
def find_mizan_by_verse(verse_id, mizan_list):
    for item in mizan_list:
        if item["verse_id"] == verse_id:
            return item["mizan"]
    return None

# --- واجهة المستخدم ---
st.set_page_config(page_title="ميزان سورة الفاتحة", layout="centered", page_icon="📖")
st.title("📖 ميزان سورة الفاتحة")
st.write("تحليل تفاعلي لآيات سورة الفاتحة مع بيانات الميزان.")

clean_data = load_clean_text()
mizan_data = load_mizan()

# اختر سورة الفاتحة من النص النظيف
fatiha = clean_data.get("001")

if fatiha:
    verses = fatiha.get("verses", {})
    for verse_num_str, verse_text in verses.items():
        verse_num = int(verse_num_str)
        mizan = find_mizan_by_verse(verse_num, mizan_data)
        with st.expander(f"آية {verse_num}: {verse_text}", expanded=True):
            if mizan:
                st.markdown(f"**نوع البيان:** {mizan.get('type', '')}")
                intent = mizan.get("intent") or mizan.get("primary_intent", "")
                if intent:
                    st.markdown(f"**النية:** {intent}")
                structure = mizan.get("structure", [])
                if structure:
                    st.markdown(f"**التركيب:** {', '.join(structure)}")
                letter_count = mizan.get("letter_count", "")
                if letter_count:
                    st.markdown(f"**عدد الحروف:** {letter_count}")
                if mizan.get("is_balanced_with_basmala"):
                    st.success("✅ هذه الآية متوازنة مع البسملة.")
            else:
                st.warning("❗ لا يوجد تحليل ميزاني لهذه الآية.")
else:
    st.error("❌ لم يتم العثور على سورة الفاتحة في نص القرآن النظيف.")