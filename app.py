import json
from importlib import import_module

from pykm.calculators import AbstractPriceCalculator

# load config
with open("config.json") as fp:
    config = json.load(fp)

print("config", config)

# get calculator module and class
calc_module_name, calc_class_name = config["calculator"].rsplit(".", maxsplit=1)
print("calc_module_name", calc_module_name)
print("calc_class_name", calc_class_name)

# import module and get class
try:
    calc_module = import_module(calc_module_name)
    calc_class = getattr(calc_module, calc_class_name)
except ModuleNotFoundError:
    print(f"ERROR: module '{calc_module_name}' not found.")
    exit(0)
except AttributeError:
    print(f"ERROR: class '{calc_class_name}' not found in module '{calc_module_name}'.")
    exit(0)

# validate class
if not issubclass(calc_class, AbstractPriceCalculator):
    print("ERROR: calculator must be of type abstract price calculator")

# create instance
calc_instance = calc_class()

# calculate some stuff
card_info = {
    "name": "Goblin Berzerker",
    "price": 10
}
print("card", card_info)
print("calculated price", calc_instance.calculate_price(card_info))
