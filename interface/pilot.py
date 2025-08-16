streamlit run pilot.py
st.title("🧭 مساعد الطيار - HarasAlLisan")

عرض هيكل المجلدات

st.subheader("📂 هيكل الملفات الحالي:")
for root, dirs, files in os.walk("../"):
level = root.replace("../", "").count(os.sep)
indent = "  " * level
st.text(f"{indent}{os.path.basename(root)}/")
subindent = "  " * (level + 1)
for f in files:
st.text(f"{subindent}{f}")

فحص وجود الملفات الأساسية

st.subheader("✅ التحقق من الملفات الأساسية:")
required_files = [
"../data/quran_clean.json",
"../data/quran_fatiha_mizan.json",
"../interface/app.py"
]
for path in required_files:
if os.path.isfile(path):
st.success(f"موجود: {path}")
else:
st.error(f"مفقود: {path}")

