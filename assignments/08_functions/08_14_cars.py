def make_car(manufacturer,model,**extra_info):
    extra_info['manufacturer'] = manufacturer
    extra_info['model'] = model
    return extra_info

car = make_car('Toyota','Rav4',color = 'black',year = '2023')
print(car)