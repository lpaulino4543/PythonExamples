store = [("Shirt", 20.00),
        ("Pants", 35.00),
        ("Jacket", 50.00),
        ("Socks", 10.00)]
to_usd = lambda data: (data[0],data[1]/0.82)
to_euro = lambda data: (data[0],data[1]*0.82)
store_usd = list(map(to_usd, store))
store_euro = list(map(to_euro,store))
for i in store_usd:
    print(i)
for i in store_euro:
    print(i)
