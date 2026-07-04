from flask import Flask, render_template
import pandas as pd # यह CSV पढ़ने के काम आएगा

app = Flask(__name__)

@app.route('/')
def home():
    # 1. अपनी CSV फ़ाइल का नाम यहाँ डालें 
    # (अगर आपकी फ़ाइल का नाम कुछ और है, तो यहाँ बदल दें)
    df = pd.read_csv('my_analyzed_data.csv')
    
    # 2. Pandas डेटा को HTML के समझने लायक फॉर्मेट (Dictionary) में बदल रहे हैं
    my_data = df.to_dict(orient='records')
    
    # 3. डेटा को HTML पेज पर भेज रहे हैं
    return render_template('index.html', table_data=my_data)

if __name__ == '__main__':
    app.run(debug=True)