from flask import *
from time import *
import src

app = Flask(__name__)


@app.route("/")
def main():
    Date = []
    Lunch = []
    Date, Lunch = src.dbGet()
    obj = {
        'day' : Date[0],
        'menu' : Lunch[0]
    }
    return render_template('main.html', **obj)

if __name__ == '__main__':
    app.run(debug=True)
    
print('test')