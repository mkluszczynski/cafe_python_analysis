from cafe.CafeRepository import CafeRepository

file = open("data/MRN_OSM_amenity_cafe_4326_Point.csv")

cafeRepo = CafeRepository(file)

for cafe in cafeRepo.find({"select": ["name", "smoking"]}):
    if cafe["smoking"] != '':
        print(cafe)


#ilość danych kawiarni
#ilość dot. możliwości palenia
#

