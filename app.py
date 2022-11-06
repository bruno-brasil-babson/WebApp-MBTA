from flask import Flask, render_template, request
from mbta_helper import find_stop_near

app = Flask(__name__)


@app.route('/nearest_mbta/', methods=["GET", "POST"])
def get_nearest_mbta():
    if request.method == "POST":
        place_name = request.form["place"]
        nearest_station = find_stop_near(place_name)[0]
        is_wheelchair = find_stop_near(place_name)[1]
        if is_wheelchair == 1:
            flag = ''
        else:
            flag = 'not'
        return render_template('mbta-result.html', place=place_name, station=nearest_station, accessibility=flag)

    return render_template('mbta-form.html')


@app.route('/')
# if website domain is www.abc.com, http://www.abc.com/ will triger the function below, hello()
@app.route('/hello/<name>')
# if the route contains /hello/name, it will triger the function below, hello(name)
def hello(name=None):
    if name:
        # return f'<h1>Hello, {name}!</h1><p>I am excited to learn flask.</p>'
        return render_template('hello.html', username=name)
    return '<h1>Hello, world!</h1>'

if __name__ == "__main__":
    app.run(debug=True)