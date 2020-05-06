from flask import Flask, request, render_template
from flask_sqlalchemy import SQLAlchemy

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///db.db'
db = SQLAlchemy(app)


class Car(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    manufacture = db.Column(db.String(80), nullable=False)
    model = db.Column(db.String(50), nullable=False)

    def __repr__(self):
        return f'<Car {self.manufacture} {self.model}>'


db.create_all()


@app.route('/')
def search():
    query = request.args.get('q') or None

    if query is not None:
        cars = Car.query.filter(Car.manufacture.like(query) | Car.model.like(query)).all()
    else:
        cars = Car.query.all()

    return render_template('cars.html', cars=cars)


if __name__ == '__main__':
    app.run()
