from flask import Flask, render_template, request, send_file
import pandas as pd
import json
import io

app = Flask(__name__)

# ग्लोबल वेरिएबल ताकि अपलोड किया हुआ डेटा डाउनलोड फंक्शन को भी मिल सके
current_df = pd.read_csv('my_analyzed_data.csv')

@app.route('/', methods=['GET', 'POST'])
def home():
    global current_df
    error_message = None

    if request.method == 'POST':
        file = request.files['file']
        if file.filename != '':
            filename = file.filename.lower()
            
            if filename.endswith('.csv') or filename.endswith('.xlsx') or filename.endswith('.xls'):
                try:
                    if filename.endswith('.csv'):
                        temp_df = pd.read_csv(file)
                    else:
                        temp_df = pd.read_excel(file)
                    
                    if 'Age' in temp_df.columns and 'City' in temp_df.columns:
                        current_df = temp_df  # ग्लोबल डेटा अपडेट करें
                    else:
                        error_message = "गलत कॉलम! कृपया ऐसी फाइल अपलोड करें जिसमें 'Age' और 'City' कॉलम हों।"
                except Exception as e:
                    error_message = "फाइल पढ़ने में दिक्कत हुई।"
            else:
                error_message = "अमान्य फाइल फॉर्मेट!"
    
    total_age = current_df['Age'].sum()
    best_city = current_df.groupby('City')['Age'].sum().idxmax()
    
    chart_data = current_df.groupby('City')['Age'].sum()
    labels = json.dumps(chart_data.index.tolist())
    values = json.dumps(chart_data.values.tolist())
    
    return render_template('index.html', 
                           table=current_df.to_html(classes='table table-striped'), 
                           total=total_age, 
                           best=best_city,
                           labels=labels,
                           values=values,
                           error=error_message)

# [नया फीचर]: एक्सेल फाइल डाउनलोड करने का रूट
@app.route('/download')
def download_file():
    global current_df
    
    # मेमोरी में ही एक्सेल फाइल बनाना (कंप्यूटर पर बिना सेव किए सीधे डाउनलोड के लिए)
    output = io.BytesIO()
    with pd.ExcelWriter(output, engine='openpyxl') as writer:
        current_df.to_excel(writer, index=False, sheet_name='SalesData')
    output.seek(0)
    
    return send_file(output, 
                     mimetype='application/vnd.openxmlformats-officedocument.spreadsheetml.sheet',
                     as_attachment=True, 
                     download_name='Dashboard_Data.xlsx')

if __name__ == '__main__':
    app.run(debug=True)