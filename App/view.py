import sys
default_limit = 1000
sys.setrecursionlimit(default_limit*10)
import App.logic as logic  
from tabulate import tabulate
from DataStructures.List import array_list as al
def new_logic():
    """
        Se crea una instancia del controlador
    """
    #TODO: Llamar la función de la lógica donde se crean las estructuras de datos
    control = logic.new_logic()
    return control

def print_menu():
    print("Bienvenido")
    print("0- Cargar información")
    print("1- Ejecutar Requerimiento 1")
    print("2- Ejecutar Requerimiento 2")
    print("3- Ejecutar Requerimiento 3")
    print("4- Ejecutar Requerimiento 4")
    print("5- Ejecutar Requerimiento 5")
    print("6- Ejecutar Requerimiento 6")
    print("7- Salir")

def load_data(control):
    """
    Carga los datos
    """
    #TODO: Realizar la carga de datos
    filename = "mercedes_sales_large.csv"
    (control,total,delta_time,first_five,last_five) = logic.load_data(control, filename)
    summary = [
        ["Archivo cargado", filename],
        ["Total de ventas cargadas", total],
        ["Tiempo de carga (ms)", f"{delta_time:.2f}"],
    ]
    
    print("\n" + "=" * 70)
    print("                 RESUMEN DE CARGA DE DATOS")
    print("=" * 70)
    print(tabulate(
        summary,
        headers=["Métrica", "Valor"],
        tablefmt="rounded_outline",
        colalign=("left", "right")
    ))

    print("\n" + "=" * 70)
    print("       PRIMERAS 5 VENTAS EN ORDEN CRONOLÓGICO")
    print("=" * 70)
    print(tabulate(
        sales_to_rows(first_five),
        headers=sales_headers(),
        tablefmt="rounded_outline",
        colalign=("left", "right", "left", "left", "right", "right", "center")
    ))

    print("\n" + "=" * 70)
    print("        ÚLTIMAS 5 VENTAS EN ORDEN CRONOLÓGICO")
    print("=" * 70)
    print(tabulate(
        sales_to_rows(last_five),
        headers=sales_headers(),
        tablefmt="rounded_outline",
        colalign=("left", "right", "left", "left", "right", "right", "center")
    ))

    return control




def print_data(control, id):
    """
        Función que imprime un dato dado su ID
    """
    #TODO: Realizar la función para imprimir un elemento
    pass

def print_req_1(control, model, min_price, max_price):
    """
        Función que imprime la solución del Requerimiento 1 en consola
    """


    (delta, total, avg_price, shown_sales) = logic.req_1(control, model, min_price, max_price)

    summary = [
        ["Modelo consultado", model],
        ["Rango de precio", f"${min_price:,.0f} - ${max_price:,.0f}"],
        ["Total de unidades vendidas", total],
        ["Tiempo de ejecucion (ms)", f"{delta:.2f}"],
        ["Precio promedio (USD)", f"${avg_price:,.2f}"],
        
    ]

    print("\n" + "=" * 70)
    print("                 REQUERIMIENTO 1")
    print("=" * 70)
    print(tabulate(
        summary,
        headers=["Metrica", "Valor"],
        tablefmt="rounded_outline",
        colalign=("left", "right")
    ))

    print("\n" + "=" * 70)
    print("       VENTAS FILTRADAS POR MODELO Y RANGO DE PRECIO")
    print("=" * 70)
    # print("Total:", total)
    # print("Rows:", sales_to_rows(shown_sales))
    print(tabulate(
        sales_to_rows(shown_sales),
        headers=sales_headers(),
        tablefmt="rounded_outline",
        colalign=("left", "right", "left", "left", "right", "right", "center")
    ))


def print_req_2(control):
    """
        Función que imprime la solución del Requerimiento 2 en consola
    """
    # TODO: Imprimir el resultado del requerimiento 2
    pass


def print_req_3(control):
    """
        Función que imprime la solución del Requerimiento 3 en consola
    """
    # TODO: Imprimir el resultado del requerimiento 3
    pass


def print_req_4(control, year, n):
    """
        Función que imprime la solución del Requerimiento 4 en consola
    """
    

    (delta,total_models, top_models) = logic.req_4(control, year, n)

    summary = [
        ["Anio consultado", year],
        ["N solicitado", n],
        ["Total de modelos considerados", total_models],
        ["Tiempo de ejecucion (ms)", f"{delta:.2f}"],
    ]

    print("\n" + "=" * 70)
    print("                 REQUERIMIENTO 4")
    print("=" * 70)
    print(tabulate(
        summary,
        headers=["Metrica", "Valor"],
        tablefmt="rounded_outline",
        colalign=("left", "right")
    ))

    print("\n" + "=" * 70)
    print("           TOP MODELOS CON MAYOR NUMERO DE VENTAS")
    print("=" * 70)
    print(tabulate(
        req_4_to_rows(top_models),
        headers=req_4_headers(),
        tablefmt="rounded_outline",
        colalign=("left", "right", "right", "right", "right")
    ))
    sales_list = al.new_list()

    for i in range(al.size(top_models)):
        model = al.get_element(top_models, i)
        sale = model["max_horsepower_sale"]
        al.add_last(sales_list, sale)
    print("\n" + "=" * 70)
    print("           Venta mayor Caballos de Fuerza")
    print("=" * 70)
    print(tabulate(
        sales_to_rows(sales_list),
        headers=sales_headers(),
        tablefmt="rounded_outline",
        colalign=("left", "right", "left", "left", "right", "right", "center")
    ))
    


def print_req_5(control):
    """
        Función que imprime la solución del Requerimiento 5 en consola
    """
    # TODO: Imprimir el resultado del requerimiento 5
    pass


def print_req_6(control):
    """
        Función que imprime la solución del Requerimiento 6 en consola
    """
    # TODO: Imprimir el resultado del requerimiento 6
    pass

# Se crea la lógica asociado a la vista
control = new_logic()

# main del ejercicio
def main():
    """
    Menu principal
    """
    working = True
    #ciclo del menu
    while working:
        print_menu()
        inputs = input('Seleccione una opción para continuar\n')
        if int(inputs) == 0:
            print("Cargando información de los archivos ....\n")
            data = load_data(control)
        elif int(inputs) == 1:
            model = input("Ingrese el modelo a consultar: ").strip()
            min_price = int(input("Ingrese el precio base minimo (USD): "))
            max_price = int(input("Ingrese el precio base maximo (USD): "))
            print_req_1(control, model, min_price, max_price)

        elif int(inputs) == 2:
            print_req_2(control)

        elif int(inputs) == 3:
            print_req_3(control)

        elif int(inputs) == 4:
            year = int(input("Ingrese el anio a consultar: "))
            n = int(input("Ingrese la cantidad N de modelos a mostrar: "))
            print_req_4(control, year, n)

        elif int(inputs) == 5:
            print_req_5(control)

        elif int(inputs) == 6:
            print_req_6(control)

        elif int(inputs) == 7:
            working = False
            print("\nGracias por utilizar el programa") 
        else:
            print("Opción errónea, vuelva a elegir.\n")
    sys.exit(0)


#Helpers para imprimir datos carga, req1, req2, req3
def sales_headers():
    return [
        "Modelo",
        "Año",
        "Tipo Combustible",
        "Color",
        "Precio Base (USD)",
        "Caballos de Fuerza",
        "Turbo"
    ]


def sales_to_rows(sales_list):
    rows = []

    for i in range(al.size(sales_list)):
        sale = al.get_element(sales_list, i)

        rows.append([
            sale["model"],
            sale["year"],
            sale["fuel_type"],
            sale["color"],
            f"${sale['base_price']:,.0f}",
            sale["horsepower"],
            sale["turbo"]
        ])

    return rows


def req_4_headers():
    return [
        "Modelo",
        "Ventas",
        "Precio Prom.",
        "HP Prom.",
        "% Turbo",
    ]


def req_4_to_rows(models_list):
    rows = []

    for i in range(al.size(models_list)):
        model = al.get_element(models_list, i)

        rows.append([
            model["model"],
            model["sales_count"],
            f"${model['avg_price']:,.2f}",
            f"{model['avg_horsepower']:.2f}",
            f"{model['turbo_percentage']:.2f}%",
        ])

    return rows