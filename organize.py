import os
import shutil

folders = {
    "al-bayan": ["surah", "ayat", "quran"],
    "al-manhaj": ["mizan", "niyyah", "rules", "algorithm"],
    "data": ["raw", "unverified", "external"],
    "interface": [".html", ".css", ".js"],
    "docs": ["README", "SIYADA", "LisanAdam", "A1-Key", "philosophy"],
    ".devcontainer": ["devcontainer.json", "Dockerfile"]
}

for folder in folders:
    os.makedirs(folder, exist_ok=True)

for filename in os.listdir("."):
    if os.path.isfile(filename):
        moved = False
        for folder, keywords in folders.items():
            for keyword in keywords:
                if keyword in filename or filename.endswith(keyword):
                    shutil.move(filename, os.path.join(folder, filename))
                    print(f"✔ Moved {filename} → {folder}/")
                    moved = True
                    break
            if moved:
                break

print("\n✅ تم ترتيب الملفات بنجاح.")
0

