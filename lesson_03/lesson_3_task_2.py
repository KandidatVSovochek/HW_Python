from smartphone import smartphone

catalog = [smartphone('Samsung', 'S25', +79255552525),
           smartphone('Iphone', 11, +79878888787),
           smartphone('Nokia', 3110, +79828282828),
           smartphone('Oppo', 'Reno14', +79565555656),
           smartphone('Lenovo', 'Moto', +79455212125)]

for phone in catalog:
    print(f"{phone.brand} - {phone.model}. {phone.number}")
