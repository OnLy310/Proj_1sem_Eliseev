# В магазинах имеются следующие товары. Магнит - молоко, соль, сахар. Пятерочка - мясо, молоко, сыр. Перекресток -
# молоко, творог, сыр, сахар. Определить:
# 1. полный список всех товаров.
# 2. в каких магазинах можно приобрести одновременно молоко и сыр.
# 3. в каких магазинах можно приобрести сахар.

magnit = ["молоко", "соль", "сахар"]
pyaterochka = ["мясо", "молоко", "сыр"]
perekrestok = ["молоко", "творог", "сыр", "сахар"]

full_product_list = set(magnit + pyaterochka + perekrestok)
print("1. Полный список товаров: ", full_product_list)

milk_and_cheese_store = [store for store in {"Магнит": magnit,
                                             "Пятерочка": pyaterochka,
                                             "Перекресток": perekrestok}.items() if "молоко" in store[1] and "сыр" in
                         store[1]]
print("2. В магазинах можно приобрести одновременно молоко и сыр: ", [store[0] for store in milk_and_cheese_store])

sugar_stores = [store for store in {"Магнит": magnit,
                                    "Пятерочка": pyaterochka,
                                    "Перекресток": perekrestok}.items() if "молоко" in store[1]]
print("3. В магазинах можно приобрести сахар: ", [store[0] for store in sugar_stores])
