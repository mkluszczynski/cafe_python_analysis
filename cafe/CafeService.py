from .CafeRepository import CafeRepository

class CafeService:

    __cafeRepo : CafeRepository

    def __init__(self, cafeRepo: CafeRepository) -> None:
        self.__cafeRepo = cafeRepo

    def getNames(self):
        return self.__cafeRepo.find({"select": ["name"]})
    
    def getNamesCount(self):
        return self.__cafeRepo.countColumn("name")

    def getSmokeCount(self):
        return self.__cafeRepo.countColumn("smoking")

    def getPaymentMethods(self):
        paymentMethodsColumns = [
            "payment:cash",
            "payment:credit_cards",
            "payment:debit_cards",
            "payment:cryptocurrencies",
            "payment:apple_pay",
        ]
        paymentList = []
        for payment in paymentMethodsColumns:
            paymentList.append({payment: self.__cafeRepo.countColumn(payment)})

        return paymentList