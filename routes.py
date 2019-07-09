from flask import Flask, render_template
from sklearn.externals import joblib
import numpy as np

app = Flask(__name__)

@app.route("/")

def index():
	model = joblib.load('regr.pkl')
	prediction = model.predict([[4, 2.5, 3005, 15, 17903.0]]).round(1)
	prediction = str(prediction)
	return render_template("index.html", prediction=prediction)

if __name__ == '__main__':
    app.run(debug=True)