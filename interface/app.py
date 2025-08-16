import streamlit as st
import yaml

# تحميل الملف
with open("../al-bayan/001_al_fatiha.yaml", "r", encoding="utf-8") as f:
    data = yaml.safe_load(f)

# عنوان السورة
st.title(f"📖 سورة {data['sura']['name']}")

# عرض كل آية + وزنها
for ayah in data["sura"]["ayahs"]:
    st.markdown(f"**{ayah['verse_id']}.** {ayah['text']}")
    st.markdown(f"🔹 **النية:** {ayah['mizan'].get('intent', '—')}")
    st.markdown(f"🧬 **الهيكل:** {', '.join(ayah['mizan'].get('structure', []))}")
    st.markdown(f"🔢 **عدد الحروف:** {ayah['mizan'].get('letter_count', '—')}")
    st.markdown("---")