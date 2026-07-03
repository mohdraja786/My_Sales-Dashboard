import pandas as pd

file_name = "my_data.csv"

try:
    df = pd.read_csv(file_name)
    
    # नया कॉलम जोड़ना
    df['Status'] = df['Age'].apply(lambda x: 'Senior' if x > 25 else 'Junior')
    
    # बदलावों के साथ इस डेटा को एक नई फाइल में सेव करना
    output_file = "my_analyzed_data.csv"
    df.to_csv(output_file, index=False) 
    
    print("--- डेटा का विश्लेषण पूरा हुआ और फाइल सेव हो गई! ---")
    print(f"अपने फोल्डर में चेक करें, '{output_file}' नाम की नई फाइल बन गई होगी।")
    
except FileNotFoundError:
    print("फाइल नहीं मिली, कृपया नाम चेक करें।")