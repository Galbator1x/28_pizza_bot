from sqlalchemy import Column, ForeignKey, Integer, String, Text
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import relationship

base = declarative_base()


class Pizza(base):
    __tablename__ = 'pizza'
    id = Column(Integer, primary_key=True)
    title = Column(String(255), unique=True)
    description = Column(Text)

    def __str__(self):
        return self.title


class PizzaChoices(base):
    __tablename__ = 'pizza_choices'
    id = Column(Integer, primary_key=True)
    title = Column(String(255))
    price = Column(Integer)
    pizza = relationship('Pizza', backref='choices', lazy='select')
    pizza_id = Column(Integer, ForeignKey(Pizza.id))

    def __str__(self):
        return '{} - {}'.format(self.title, self.price)
