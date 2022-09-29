def car_info(mark,consommation,**complementary):
    car = {'label':mark,'ecology indice':consommation,'sup':complementary}
    return car

car_buyed = car_info('subaru','G',color = 'blue',ESP ='yes')
print(car_buyed)