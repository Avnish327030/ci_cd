from flask import Flask

app = Flask(__name__)


@app.route("/", methods=['GET', 'POST'])
def index():
    return "<h1>This  is avnish yadav for ci cd demo</h1>"


# This is a sample Python script.

# Press Shift+F10 to execute it or replace it with your code.
# Press Double Shift to search everywhere for classes, files,
# tool windows, actions, and settings.


# Press the green button in the gutter to run the script.
if __name__ == '__main__':
    app.run()

# See PyCharm help at https://www.jetbrains.com/help/pycharm/
