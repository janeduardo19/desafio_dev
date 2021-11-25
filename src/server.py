from flask import Flask
from extract import Extract
from timsort import TimSort


def extract_data():

    cont_page = 9950

    ext_data = Extract(cont_page)

    return ext_data.get_data()


def organize_data():

    ord_data = TimSort()

    data = extract_data()

    return ord_data.tim_sort(data)


result = organize_data()

app = Flask(__name__)


@app.route("/")
def page():
    return {'numbers': result}


def run_api():
    app.run(debug=True)
