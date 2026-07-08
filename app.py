from flask import Flask, render_template, request
import pandas as pd
import json

app = Flask(__name__)

# methods=['GET', 'POST'] जोड़ने से हम फाइल रिसीव कर पाएंगे
@app.route('/', methods=['GET', 'POST'])
def home():
    # डिफ़ॉल्ट रूप से आपकी पुरानी फ़ाइल लोड होगी
    df = pd.read_csv('my_analyzed_data.csv') 

    # अगर कोई नई फ़ाइल अपलोड करता है, तो उसे पढ़ेंगे
    if request.method == 'POST':
        file = request.files['file']
        if file.filename != '':
            df = pd.read_csv(file)
    
    # कैलकुलेशन और चार्ट का डेटा (कोड वही है)
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