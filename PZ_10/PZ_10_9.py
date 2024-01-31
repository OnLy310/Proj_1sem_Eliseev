# В магазинах имеются следующие товары. Магнит - молоко, соль, сахар. Пятерочка - мясо, молоко, сыр. Перекресток -
# молоко, творог, сыр, сахар. Определить:
# 1. полный список всех товаров.
# 2. в каких магазинах можно приобрести одновременно молоко и сыр.
# 3. в каких магазинах можно приобрести сахар.

magnit = {"молоко", "соль", "сахар"}
pyaterochka = {"мясо", "молоко", "сыр"}
perekrestok = {"молоко", "творог", "сыр", "сахар"}

stores = {
    "Магнит": magnit,
    "Пятерочка": pyaterochka,
    "Перекресток": perekrestok
}

all_products = set.union(*stores.values())
print("1. Полный список всех товаров:", all_products)

milk_and_cheese_stores = {store for store, products in stores.items() if "молоко" in products and "сыр" in products}
print("2. Магазины с молоком и сыром:", milk_and_cheese_stores)

sugar_stores = {store for store, products in stores.items() if "сахар" in products}
print("3. Магазины с сахаром:", sugar_stores)
