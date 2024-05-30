from flask_frozen import Freezer
from ipsearch import app  # Cambia 'ipsearch' por el nombre de tu archivo principal de Flask

freezer = Freezer(app)

if __name__ == '__main__':
    freezer.freeze()