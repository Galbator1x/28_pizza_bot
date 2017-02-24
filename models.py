from flask_sqlalchemy import SQLAlchemy

db = SQLAlchemy()


class Pizza(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    title = db.Column(db.String(255), unique=True)
    description = db.Column(db.Text)

    def __str__(self):
        return self.title


class PizzaChoices(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    title = db.Column(db.String(255))
    price = db.Column(db.Integer)
    pizza = db.relationship('Pizza', backref='choices')
    pizza_id = db.Column(db.Integer, db.ForeignKey(Pizza.id))

    def __str__(self):
        return '{} - {}'.format(self.title, self.price)
