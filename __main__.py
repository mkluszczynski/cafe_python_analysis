from cafe.CafeRepository import CafeRepository
from cafe.CafeService import CafeService

file = open("data/MRN_OSM_amenity_cafe_4326_Point.csv")

cafeRepo = CafeRepository(file)
cafeService = CafeService(cafeRepo)

for cafe in cafeService.getSmokeCount():
    print(cafe)

for payment in cafeService.getPaymentMethods():
    print(payment)

#ilość danych kawiarni
#ilość dot. możliwości palenia
#ilość akceptowanych metod płatności
#godziny otwarcia
#ilość kawiarni w danym mieście



