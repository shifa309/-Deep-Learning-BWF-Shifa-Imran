def make_car(manufacturer, model, **args):
    car = {
        'manufacturer': manufacturer,
        'model': model
    }
    car.update(args)
    return car

car = make_car('subaru', 'outback', color='blue', tow_package=True)
print(car)

