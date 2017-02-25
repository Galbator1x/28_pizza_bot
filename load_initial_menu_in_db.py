from menu import catalog
from models import Pizza, PizzaChoices
from server import session


def load_menu_in_db(catalog):
    for item in catalog:
        pizza = Pizza()
        pizza.title = item.get('title')
        pizza.description = item.get('description')
        session.add(pizza)
        for size in item.get('choices', []):
            p_size = PizzaChoices()
            p_size.pizza = pizza
            p_size.title = size.get('title')
            p_size.price = size.get('price')
            session.add(p_size)
    session.commit()


if __name__ == '__main__':
    load_menu_in_db(catalog)
