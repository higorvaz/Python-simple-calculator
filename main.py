from flask import Flask
from flask import render_template
from flask import request

app = Flask(__name__)


@app.route('/', methods=["POST", "GET"])
def home():
    if request.method == "POST":
        val1 = int(request.form["field1"])
        val2 = int(request.form["field2"])

        if (request.form.get("add")):
            res = val1 + val2
            return render_template('index.html', val=res)
        if (request.form.get("sub")):
            res = val1 - val2
            return render_template('index.html', val=res)

        return render_template('index.html')
    else:
        return render_template('index.html', val="na")


app.run(host="0.0.0.0", debug=True)
