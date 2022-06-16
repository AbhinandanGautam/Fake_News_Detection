from flask import Flask,render_template,request,flash
import pickle

vector = pickle.load(open("vectorizer.pkl", 'rb'))
model = pickle.load(open("finalized_model.pkl", 'rb'))

app = Flask(__name__)

@app.route("/", methods=['GET', 'POST'])
def home():
    if request.method == "POST":
        news = str(request.form['news'])
        print(news)

        predict = model.predict(vector.transform([news]))[0]
        print(predict)

        mess = "News headline is -> {}".format(predict)

        return render_template("index.html",message=mess)
    else:
        return render_template("index.html",message="")

if __name__ == '__main__':
    app.run(debug=True)