from flask import Flask, render_template
import pandas as pd
import json

app = Flask(__name__)

@app.route('/')
def home():
    df = pd.read_csv('my_analyzed_data.csv') 
    
    # कॉलम के नाम बदल दिए गए हैं जो आपकी फ़ाइल में मौजूद हैं
    total_age = df['Age'].sum()
    # 'best' निकालने के लिए हमने 'City' का इस्तेमाल किया है
    best_city = df.groupby('City')['Age'].sum().idxmax()
    
    # चार्ट के लिए डेटा
    chart_data = df.groupby('City')['Age'].sum()
    labels = json.dumps(chart_data.index.tolist())
    values = json.dumps(chart_data.values.tolist())
    
    return render_template('index.html', 
                           table=df.to_html(classes='table table-striped'), 
                           total=total_age, 
                           best=best_city,
                           labels=labels,
                           values=values)

if __name__ == '__main__':
    app.run(debug=True)