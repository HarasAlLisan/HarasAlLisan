
streamlit run app.py
import streamlit as st
from transformers import AutoTokenizer, AutoModelForSequenceClassification
import torch

# تحميل النموذج
model_name = "aubmindlab/bert-base-arabertv02-twitter"
tokenizer = AutoTokenizer.from_pretrained(model_name)
model = AutoModelForSequenceClassification.from_pretrained(model_name)

# عنوان التطبيق
st.title("تحليل النية - Haras Al Lisan")

# إدخال النص
text = st.text_input("أدخل الجملة للتحليل:")⅞

if text:
    inputs = tokenizer(text, return_tensors="pt", truncation=True, padding=Truewith torch.no_grad():
                outputs = model(**inputs)
                        probs = torch.nn.functional.softmax(outputs.logits, dim=                          label = torch.argmax(probs, dim=1).item()
                                        st.write(f"🔎 النية المتوقعة: **LABEL_{label}**"
                                        