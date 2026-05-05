import time
import csv
import os
import tracemalloc
csv.field_size_limit(2147483647)

from DataStructures.Tree import red_black_tree as rbt
from DataStructures.Priority_queue import priority_queue as pq
from DataStructures.Map import map_linear_probing as mp
from DataStructures.List import array_list as al
data_dir = os.path.join(os.path.dirname(os.path.dirname(os.path.realpath(__file__))), 'Data')
def new_logic():
    """
    Crea el catalogo para almacenar las estructuras de datos
    """
    #TODO: Llama a las funciónes de creación de las estructuras de datos
    catalog = {
    "sales": al.new_list(),
    "size": 0,

    # Carga: primeras y ultimas ventas en orden cronologico
    "by_year": rbt.new_map(),

    # REQ 1: modelo y rango de precio
    "model_price": mp.new_map(1000),

    # REQ 2: fuel type y rango de horsepower
    "fuel_hp": mp.new_map(20),

    # REQ 3: year y fuel type y rango de precio
    "year_fuel_price": mp.new_map(100),

    # REQ 4: year y modelo y estadisticas
    "year_model_stats": mp.new_map(20),

    # REQ 5: rango de horsepower y colores mas vendidos
    "by_horsepower": rbt.new_map(),

    # REQ 6: rango de años y precios y modelos estables
    "year_price": mp.new_map(20)
}
    return catalog


# Funciones para la carga de datos

def load_data(catalog, filename):
    """
    Carga los datos del reto
    """
    # TODO: Realizar la carga de datos
    start_time = get_time()
    filepath = os.path.join(data_dir, filename)
    input_file = csv.DictReader(open(filepath, encoding='utf-8'))

    for row_sales in input_file:
        sale = clean_sale(row_sales)
        al.add_last(catalog["sales"], sale)
        catalog["size"] += 1
        
        add_to_rbt_list(catalog["by_year"], sale["year"], sale)
        model_tree = rbt_in_map(catalog["model_price"], sale["model"])
        add_to_rbt_list(model_tree, sale["base_price"], sale)
        
        fuel_tree = rbt_in_map(catalog["fuel_hp"], sale["fuel_type"])
        add_to_rbt_list(fuel_tree, sale["horsepower"], sale)
        
        year_fuel_tree = map_in_map(catalog["year_fuel_price"], sale["year"], 20)
        fuel_price_tree = rbt_in_map(year_fuel_tree, sale["fuel_type"])
        add_to_rbt_list(fuel_price_tree, sale["base_price"], sale)
        
        add_year_model_stats(catalog, sale)
        
        add_to_rbt_list(catalog["by_horsepower"], sale["horsepower"], sale)
        
        price_tree = rbt_in_map(catalog["year_price"], sale["year"])
        add_to_rbt_list(price_tree, sale["base_price"], sale) 
    end_time = get_time()
    delta = delta_time(start_time, end_time)
    
    first, last = get_first_last_sales(catalog)
    return catalog, catalog["size"], delta, first, last
        
        
        
        


# Funciones de consulta sobre el catálogo


def req_1(catalog, model, min_price, max_price):
    """
    Retorna el resultado del requerimiento 1
    """
    start_time = get_time()
    model = model.upper()
    model_tree = mp.get(catalog["model_price"], model)
    filtered_sales = al.new_list()
    total_price = 0

    if model_tree is not None:
        price_groups = rbt.values(model_tree, min_price, max_price)
        current_group = price_groups["first"]

        while current_group is not None:
            sales_list = current_group["info"]

            for i in range(al.size(sales_list)):
                sale = al.get_element(sales_list, i)
                al.add_last(filtered_sales, sale)
                total_price += sale["base_price"]

            current_group = current_group["next"]

    al.merge_sort(filtered_sales, compare_req_1)

    total = al.size(filtered_sales)
    avg_price = 0
    if total > 0:
        avg_price = total_price / total

    shown_sales = get_first_last(filtered_sales, 6)

    end_time = get_time()
    delta = delta_time(start_time, end_time)

    return delta, total, avg_price,shown_sales
    


def req_2(catalog):
    """
    Retorna el resultado del requerimiento 2
    """
    # TODO: Modificar el requerimiento 2
    pass


def req_3(catalog):
    """
    Retorna el resultado del requerimiento 3
    """
    # TODO: Modificar el requerimiento 3
    pass


def req_4(catalog, year, n):
    """
    Retorna el resultado del requerimiento 4
    """
    start_time = get_time()

    year_map = mp.get(catalog["year_model_stats"], year)
    top_models = al.new_list()
    total_models = 0

    if year_map is not None:
        total_models = mp.size(year_map)
        stats_values = mp.value_set(year_map)
        ranking = pq.new_heap(is_min_heap=False)

        for i in range(al.size(stats_values)):
            stats = al.get_element(stats_values, i)
            result = build_req_4_result(stats)
            priority = (result["sales_count"], result["avg_price"])
            pq.insert(ranking, priority, result)

        limit = n
        if total_models < limit:
            limit = total_models

        for i in range(limit):
            al.add_last(top_models, pq.remove(ranking))

    al.merge_sort(top_models, compare_req_4)

    end_time = get_time()
    delta = delta_time(start_time, end_time)

    return delta,total_models, top_models
    


def build_req_4_result(stats):
    count = stats["count"]
    avg_price = 0
    avg_horsepower = 0
    turbo_percentage = 0

    if count > 0:
        avg_price = stats["price_sum"] / count
        avg_horsepower = stats["horsepower_sum"] / count
        turbo_percentage = (stats["turbo_yes"] / count) * 100

    return {
        "model": stats["model"],
        "sales_count": count,
        "avg_price": avg_price,
        "avg_horsepower": avg_horsepower,
        "turbo_percentage": turbo_percentage,
        "max_horsepower_sale": stats["max_horsepower_sale"]
    }


def req_5(catalog):
    """
    Retorna el resultado del requerimiento 5
    """
    # TODO: Modificar el requerimiento 5
    pass

def req_6(catalog):
    """
    Retorna el resultado del requerimiento 6
    """
    # TODO: Modificar el requerimiento 6
    pass


# Funciones para medir tiempos de ejecucion

def get_time():
    """
    devuelve el instante tiempo de procesamiento en milisegundos
    """
    return float(time.perf_counter()*1000)


def delta_time(start, end):
    """
    devuelve la diferencia entre tiempos de procesamiento muestreados
    """
    elapsed = float(end - start)
    return elapsed

#Helpers de carga de datos
def clean_sale(row):
    return {
        "model": clean_text(row["Model"]),
        "year": clean_int(row["Year"]),
        "region": clean_text(row["Region"]),
        "color": clean_text(row["Color"]),
        "fuel_type": clean_text(row["Fuel Type"]),
        "base_price": clean_int(row["Base Price (USD)"]),
        "horsepower": clean_int(row["Horsepower"]),
        "sales_volume": clean_int(row["Sales Volume"]),
        "turbo": clean_text(row["Turbo"])
    }
def clean_text(value):
    if value is None or value.strip() == "":
        return "Unknown"
    return value.strip().upper()


def clean_int(value):
    if value is None or str(value).strip() == "":
        return 0
    return int(value)

def add_to_rbt_list(tree, key, sale):
    sales = rbt.get(tree, key)

    if sales is None:
        sales = al.new_list()
        al.add_last(sales, sale)
        rbt.put(tree, key, sales)
    else:
        al.add_last(sales, sale)
        
def rbt_in_map(my_map, key):
    """
    Busca un arbol RBT asociado a key dentro de my_map.
    Si no existe, crea uno nuevo, lo guarda y lo retorna.
    """
    tree = mp.get(my_map, key)

    if tree is None:
        tree = rbt.new_map()
        mp.put(my_map, key, tree)

    return tree

def map_in_map(my_map, key, size):
    """
    Busca un mapa asociado a key dentro de my_map.
    Si no existe, crea uno nuevo, lo guarda y lo retorna.
    """
    inner_map = mp.get(my_map, key)

    if inner_map is None:
        inner_map = mp.new_map(size)
        mp.put(my_map, key, inner_map)


    return inner_map

def add_year_model_stats(catalog, sale):
    year_map = map_in_map(
        catalog["year_model_stats"],
        sale["year"],
        1000
    )

    stats = mp.get(year_map, sale["model"])

    if stats is None:
        stats = {
            "model": sale["model"],
            "count": 0,
            "price_sum": 0,
            "horsepower_sum": 0,
            "turbo_yes": 0,
            "max_horsepower_sale": sale
        }
        mp.put(year_map, sale["model"], stats)

    stats["count"] += 1
    stats["price_sum"] += sale["base_price"]
    stats["horsepower_sum"] += sale["horsepower"]

    if sale["turbo"] == "YES":
        stats["turbo_yes"] += 1

    if mejor_venta_horsepowe(sale, stats["max_horsepower_sale"]):
        stats["max_horsepower_sale"] = sale


def mejor_venta_horsepowe(new_sale, current_sale):
    if new_sale["horsepower"] > current_sale["horsepower"]:
        return True

    if new_sale["horsepower"] == current_sale["horsepower"]:
        if new_sale["base_price"] < current_sale["base_price"]:
            return True

        if new_sale["base_price"] == current_sale["base_price"]:
            return new_sale["year"] < current_sale["year"]

    return False


def get_first_last_sales(catalog):
    ordered_sales = al.new_list()

    for sale in catalog["sales"]["elements"]:
        al.add_last(ordered_sales, sale)

    al.merge_sort(ordered_sales, compare_load_order)

    total = al.size(ordered_sales)

    first_five = al.new_list()
    last_five = al.new_list()

    # Primeros 5
    count = 0
    for sale in ordered_sales["elements"]:
        if count == 5:
            break
        al.add_last(first_five, sale)
        count += 1

    # Últimos 5
    count = 0
    start = total - 5
    if start < 0:
        start = 0

    index = 0
    for sale in ordered_sales["elements"]:
        if index >= start:
            if count == 5:
                break
            al.add_last(last_five, sale)
            count += 1
        index += 1

    return first_five, last_five

def compare_load_order(sale_1, sale_2):
    if sale_1["year"] != sale_2["year"]:
        return sale_1["year"] < sale_2["year"]

    if sale_1["base_price"] != sale_2["base_price"]:
        return sale_1["base_price"] < sale_2["base_price"]

    return sale_1["model"] < sale_2["model"]


def compare_req_1(sale_1, sale_2):
    if sale_1["base_price"] != sale_2["base_price"]:
        return sale_1["base_price"] < sale_2["base_price"]

    if sale_1["horsepower"] != sale_2["horsepower"]:
        return sale_1["horsepower"] > sale_2["horsepower"]

    return sale_1["color"] < sale_2["color"]


def compare_req_4(model_1, model_2):
    if model_1["sales_count"] != model_2["sales_count"]:
        return model_1["sales_count"] > model_2["sales_count"]

    if model_1["avg_price"] != model_2["avg_price"]:
        return model_1["avg_price"] > model_2["avg_price"]

    return model_1["model"] < model_2["model"]


def get_first_last(my_list, amount):
    total = al.size(my_list)

    if total <= amount * 2:
        return my_list

    result = al.new_list()

    for i in range(amount):
        al.add_last(result, al.get_element(my_list, i))

    start = total - amount
    for i in range(start, total):
        al.add_last(result, al.get_element(my_list, i))

    return result