from flask import Flask, request, jsonify,render_template
import pickle
import warnings

app = Flask(__name__,static_url_path='', 
            static_folder='static',
            template_folder='templates')
#CORSxq


# Load the model
model = pickle.load(open('model.pkl', 'rb'))

@app.route('/')
def home():
    return render_template('index.html')

@app.route('/predict', methods=['POST'])
def predict():
    if not request.is_json:
        return jsonify({'error': 'Request must contain JSON data.'}), 400

    try:
        warnings.filterwarnings("ignore")
        # Get the JSON data from the request
        data = request.get_json()

        # Process the data to match the model's expected input format
        features = [[
            data['NG'], 
            data['FGT'], 
            data['HZT'], 
            data['Stack'], 
            data['Feed Rate'], 
            data['CO'], 
            data['Cooler'], 
            data['RPM'], 
            data['BA'], 
            data ['Molochite']

     ]]
            
        prediction = model.predict(features)
        print(prediction);
     
    # Return the prediction as JSON
        return jsonify({'prediction': prediction[0]})
    
    except Exception as e:
        return jsonify({'error': str(e)}), 400



if __name__ == '__main__':
    app.run(debug=True)
