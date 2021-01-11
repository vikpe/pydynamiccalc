import abc


class AbstractPriceCalculator(abc.ABC):
    @classmethod
    def calculate_price(cls, card_info: dict) -> float:
        raise NotImplementedError


class DefaultPriceCalculator(AbstractPriceCalculator):
    @classmethod
    def calculate_price(cls, card_info: dict) -> float:
        return card_info["price"]
