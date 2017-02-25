from menu import catalog
from models import Pizza, PizzaChoices
from server import session


def load_menu_in_db(catalog):
    for item in catalog:
        pizza = Pizza()
        pizza.title = item.get('title')
        pizza.description = item.get('description')
        session.add(pizza)
        for choice in item.get('choices', []):
            p_choice = PizzaChoices()
            p_choice.pizza = pizza
            p_choice.title = choice.get('title')
            p_choice.price = choice.get('price')
            session.add(p_choice)
    session.commit()


if __name__ == '__main__':
    load_menu_in_db(catalog)
