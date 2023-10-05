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