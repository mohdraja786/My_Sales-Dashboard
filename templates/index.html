from flask import Flask, render_template, request, Response # Response को जोड़ा गया है
import pandas as pd

app = Flask(__name__)

@app.route('/')
def home():
    df = pd.read_csv('sales report.csv', encoding='latin1', engine='python', on_bad_lines='skip')
    df.columns = df.columns.str.strip()
    
    regions = df['Region'].unique().tolist()
    selected_region = request.args.get('region', 'All')
    
    if selected_region != 'All':
        df = df[df['Region'] == selected_region]
    
    my_table = df.head(5).to_html(classes='table table-striped table-hover', index=False)
    
    chart_data = df.groupby('Category')['Sales'].sum().reset_index()
    categories = chart_data['Category'].tolist()
    sales = chart_data['Sales'].tolist()
    
    return render_template('index.html', 
                           table_data=my_table, 
                           categories=categories, 
                           sales=sales,
                           regions=regions,
                           selected=selected_region)

# -------- यह नया कोड डाउनलोड बटन के लिए है --------
@app.route('/download')
def download():
    # 1. फाइल पढ़ें
    df = pd.read_csv('sales report.csv', encoding='latin1', engine='python', on_bad_lines='skip')
    df.columns = df.columns.str.strip()
    
    # 2. चेक करें कि यूजर को कौन सा रीजन चाहिए
    region = request.args.get('region', 'All')
    if region != 'All':
        df = df[df['Region'] == region]
        
    # 3. डेटा को वापस CSV फॉर्मेट में बदलें
    csv_data = df.to_csv(index=False)
    
    # 4. यूजर को फाइल डाउनलोड करवाएं
    return Response(
        csv_data,
        mimetype="text/csv",
        headers={"Content-disposition": f"attachment; filename=Sales_Data_{region}.csv"}
    )
# --------------------------------------------------

if __name__ == '__main__':
    app.run(debug=True)