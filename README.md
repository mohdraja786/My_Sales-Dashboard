# 📊 Advanced Sales & Data Analytics Dashboard

यह एक फुल-स्टैक डायनामिक डेटा एनालिटिक्स डैशबोर्ड है जिसे **Python (Flask)**, **Pandas**, और **JavaScript (Chart.js)** की मदद से बनाया गया है। यह यूजर को अपनी एक्सेल या सीएसवी फाइल अपलोड करने, उसका लाइव चार्ट देखने और डेटा को वापस डाउनलोड करने की सुविधा देता है।

## 🌐 लाइव प्रोजेक्ट लिंक
आप इस प्रोजेक्ट का लाइव जादू यहाँ देख सकते हैं:
👉 **[https://my-sales-dashboard-zofm.onrender.com](https://my-sales-dashboard-zofm.onrender.com)**

---

## ✨ मुख्य फीचर्स (Key Features)

* **📁 Multi-Format Upload:** यह सिस्टम `.csv`, `.xlsx`, और `.xls` (एक्सेल) दोनों तरह की फाइलों को आसानी से स्वीकार करता है।
* **🛡️ Smart File Validation:** अगर कोई गलत फाइल या बिना सही कॉलम (`Age`, `City`) वाली फाइल अपलोड करने की कोशिश करता है, तो ऐप क्रैश नहीं होता बल्कि सुंदर सा एरर मैसेज दिखाता है।
* **📈 Dynamic Chart Switcher:** यूजर बिना पेज रिफ्रेश किए एक क्लिक में **Bar Chart**, **Line Chart**, या **Pie Chart** में डेटा को लाइव बदल सकता है।
* **🌙 Premium Dark Mode:** आँखों की सुरक्षा और बेहतरीन लुक के लिए इसमें लाइट और डार्क मोड का लाइव थीम स्विचर लगा है।
* **📥 Export to Excel:** यूजर एक क्लिक में पूरे डेटा टेबल को वापस एक असली एक्सेल फाइल बनाकर अपने कंप्यूटर या मोबाइल में डाउनलोड कर सकता है।

---

## 🛠️ इस्तेमाल की गई तकनीकें (Tech Stack)

* **Backend:** Python, Flask
* **Data Processing:** Pandas, OpenPyXL
* **Frontend:** HTML5, CSS3, Bootstrap 5 (VIP UI)
* **Charts/Visuals:** Chart.js (Interactive JavaScript Library)
* **Deployment:** GitHub, Render Cloud

---

## 💻 अपने कंप्यूटर पर कैसे चलाएं? (Local Setup)

1. इस प्रोजेक्ट को क्लोन करें या डाउनलोड करें।
2. टर्मिनल में जरूरी लाइब्रेरी इंस्टॉल करें:
   ```bash
   pip install flask pandas openpyxl gunicorn