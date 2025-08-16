import os

for root, dirs, files in os.walk("."):
    for d in dirs:
        if d.startswith(" "):
            print(f"⚠️ مجلد غير صحيح: '{d}' في المسار: {os.path.join(root, d)}")
