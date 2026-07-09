from flask import Flask, render_template, request
import pandas as pd
import json

# यह लाइन मिसिंग थी, इसे सुनिश्चित करें
app = Flask(__name__)

@app.route('/', methods=['GET', 'POST'])
def home():
    # डिफ़ॉल्ट फ़ाइल (पुरानी CSV)
    df = pd.read_csv('my_analyzed_data.csv') 

    if request.method == 'POST':
        file = request.files['file']
        if file.filename != '':
            # चेक कर रहे हैं कि फाइल Excel है या CSV
            if file.filename.endswith('.xlsx') or file.filename.endswith('.xls'):
                df = pd.read_excel(file)
            elif file.filename.endswith('.csv'):
                df = pd.read_csv(file)
    
    # कैलकुलेशन (Age और City कॉलम के साथ)
    total_age = df['Age'].sum()
    best_city = df.groupby('City')['Age'].sum().idxmax()
    
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