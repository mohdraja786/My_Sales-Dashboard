from flask import Flask, render_template, request
import pandas as pd
import json

app = Flask(__name__)

@app.route('/', methods=['GET', 'POST'])
def home():
    # डिफ़ॉल्ट फाइल (यह हमेशा सुरक्षित रहेगी)
    df = pd.read_csv('my_analyzed_data.csv') 
    error_message = None  # एरर मैसेज स्टोर करने के लिए

    if request.method == 'POST':
        file = request.files['file']
        if file.filename != '':
            filename = file.filename.lower()
            
            # 1. सुरक्षा चेक: केवल Excel या CSV फाइल ही अंदर आ सकती है
            if filename.endswith('.csv') or filename.endswith('.xlsx') or filename.endswith('.xls'):
                try:
                    # फाइल को रीड करें
                    if filename.endswith('.csv'):
                        temp_df = pd.read_csv(file)
                    else:
                        temp_df = pd.read_excel(file)
                    
                    # 2. कॉलम चेक: क्या फाइल में 'Age' और 'City' मौजूद हैं?
                    if 'Age' in temp_df.columns and 'City' in temp_df.columns:
                        df = temp_df  # सब सही है, तो डेटा अपडेट करें
                    else:
                        error_message = "गलत कॉलम! कृपया ऐसी फाइल अपलोड करें जिसमें 'Age' और 'City' कॉलम हों।"
                
                except Exception as e:
                    error_message = "फाइल पढ़ने में दिक्कत हुई। कृपया सही फाइल अपलोड करें।"
            else:
                error_message = "अमान्य फाइल! केवल .csv, .xlsx, या .xls फाइलें ही अपलोड की जा सकती हैं।"
    
    # कैलकुलेशन पुराना वाला ही रहेगा
    total_age = df['Age'].sum()
    best_city = df.groupby('City')['Age'].sum().idxmax()
    
    chart_data = df.groupby('City')['Age'].sum()
    labels = json.dumps(chart_data.index.tolist())
    values = json.dumps(chart_data.values.tolist())
    
    # इस बार हम 'error' भी HTML को भेज रहे हैं
    return render_template('index.html', 
                           table=df.to_html(classes='table table-striped'), 
                           total=total_age, 
                           best=best_city,
                           labels=labels,
                           values=values,
                           error=error_message) # यह नया है

if __name__ == '__main__':
    app.run(debug=True)