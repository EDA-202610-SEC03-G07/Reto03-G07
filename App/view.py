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


def print_req_2(control, combustible, hp_min, hp_max):
    """
        Función que imprime la solución del Requerimiento 2 en consola
    """

    (delta, total, avg_price, avg_hp, shown_sales) = logic.req_2(control, combustible, hp_min, hp_max)

    summary = [
        ["Tipo de combustible consultado", combustible],
        ["Rango de horsepower", f"{hp_min:,.0f} HP - {hp_max:,.0f} HP"],
        ["Total de unidades vendidas", total],
        ["Tiempo de ejecucion (ms)", f"{delta:.2f}"],
        ["Precio promedio (USD)", f"${avg_price:,.2f}"],
        ["Horsepower promedio", f"{avg_hp:,.2f} HP"],
    ]

    print("\n" + "=" * 70)
    print("                 REQUERIMIENTO 2")
    print("=" * 70)
    print(tabulate(
        summary,
        headers=["Metrica", "Valor"],
        tablefmt="rounded_outline",
        colalign=("left", "right")
    ))

    print("\n" + "=" * 70)
    print("       VENTAS FILTRADAS POR COMBUSTIBLE Y RANGO DE HP")
    print("=" * 70)
    print(tabulate(
        sales_to_rows(shown_sales),
        headers=sales_headers(),
        tablefmt="rounded_outline",
        colalign=("left", "right", "left", "left", "right", "right", "center")
    ))

def print_req_3(control, year, fuel_type, min_price, max_price):
    """
        Función que imprime la solución del Requerimiento 3 en consola
    """
    # TODO: Imprimir el resultado del requerimiento 3
    (delta, total, avg_price, shown_sales) = logic.req_3(control, year, fuel_type, min_price, max_price)

    summary = [
        ["Año consultado", year],
        ["Tipo de combustible", fuel_type],
        ["Rango de precio", f"${min_price:,.0f} - ${max_price:,.0f}"],
        ["Total de unidades vendidas", total],
        ["Tiempo de ejecucion (ms)", f"{delta:.2f}"],
        ["Precio promedio (USD)", f"${avg_price:,.2f}"],
    ]

    print("\n" + "=" * 70)
    print("                 REQUERIMIENTO 3")
    print("=" * 70)
    print(tabulate(
        summary,
        headers=["Metrica", "Valor"],
        tablefmt="rounded_outline",
        colalign=("left", "right")
    ))

    print("\n" + "=" * 70)
    print("       VENTAS FILTRADAS POR AÑO, COMBUSTIBLE Y RANGO DE PRECIO")
    print("=" * 70)
    if al.size(shown_sales) == 0:
        print("No se encontraron ventas con los filtros ingresados.")
    else:
        print(tabulate(
            sales_to_rows(shown_sales),
            headers=sales_headers(),
            tablefmt="rounded_outline",
            colalign=("left", "right", "left", "left", "right", "right", "center")
        ))


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
    


def print_req_5(control,horsepower,delta,n):
    delta_time, total_vehiculos, top_colores=logic.req_5(control,horsepower, delta, n)
    print("\n" + "="*70)
    print("REQUERIMIENTO 5")
    print("="*70)

    resumen = [
        ["Horsepower de referencia", f"{horsepower} HP"],
        ["Delta", f"{delta} HP"],
        ["Rango de horsepower", f"{horsepower - delta} HP - {horsepower + delta} HP"],
        ["N solicitado", n],
        ["Total de vehículos encontrados", total_vehiculos],
        ["Tiempo de ejecución (ms)", f"{delta_time:.2f}"]
    ]

    print(tabulate(
        resumen,
        headers=["Métrica", "Valor"],
        tablefmt="rounded_grid"
    ))

    if total_vehiculos == 0 or al.size(top_colores) == 0:
        print("\nNo se encontraron vehículos dentro del rango indicado.")
        return

    tabla = []

    for i in range(al.size(top_colores)):
        color_info = al.get_element(top_colores, i)

        tabla.append([
            color_info["color"],
            color_info["total_ventas"],
            f'{color_info["hp_promedio"]:.2f} HP'
        ])

    print("\n" + "="*70)
    print("TOP N DE COLORES CON MÁS VEHÍCULOS VENDIDOS")
    print("="*70)

    print(tabulate(
        tabla,
        headers=[
            "Color",
            "Vehículos vendidos",
            "Horsepower promedio"
        ],
        tablefmt="rounded_grid"
    ))


def print_req_6(control, min_year, max_year, min_price, max_price, cantidad_m):
    """
        Función que imprime la solución del Requerimiento 6 en consola
    """
    # TODO: Imprimir el resultado del requerimiento 6
    (delta, total_modelos, lista_top) = logic.req_6(control, min_year, max_year, min_price, max_price, cantidad_m)

    summary = [
        ["Rango de años", f"{min_year} - {max_year}"],
        ["Rango de precio", f"${min_price:,.0f} - ${max_price:,.0f}"],
        ["M solicitado", cantidad_m],
        ["Total de modelos considerados", total_modelos],
        ["Tiempo de ejecucion (ms)", f"{delta:.2f}"],
    ]

    print("\n" + "=" * 70)
    print("                 REQUERIMIENTO 6")
    print("=" * 70)
    print(tabulate(summary, headers=["Metrica", "Valor"], tablefmt="rounded_outline", colalign=("left", "right")))

    rows = []
    ventas_rep = al.new_list()
    for i in range(al.size(lista_top)):
        modelo = al.get_element(lista_top, i)
        rows.append([
            modelo["modelo"],
            modelo["cantidad_ventas"],
            f"${modelo['mu']:,.2f}",
            f"${modelo['sigma']:,.2f}",
            f"{modelo['estabilidad']:.4f}",
            f"{modelo['promedio_hp']:.2f} HP",
        ])
        al.add_last(ventas_rep, modelo["venta_representativa"])

    print("\n" + "=" * 70)
    print("           TOP M MODELOS CON PRECIO MAS ESTABLE")
    print("=" * 70)
    print(tabulate(rows, headers=["Modelo", "Ventas", "Promedio Precio (μ)", "Desviacion", "Estabilidad", "HP Promedio"],
                   tablefmt="rounded_outline"))

    print("\n" + "=" * 70)
    print("           VENTA REPRESENTATIVA POR MODELO")
    print("=" * 70)
    print(tabulate(sales_to_rows(ventas_rep), headers=sales_headers(), tablefmt="rounded_outline",
                   colalign=("left", "right", "left", "left", "right", "right", "center")))

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
            combustible=input("ingrese el tipo de combustible que desea analizar: ")
            hp_min=int(input("ingrese la potencia (HP) minima: "))
            hp_max=int(input("ingrese la potencia (HP) maxima: "))
            print_req_2(control,combustible,hp_min,hp_max)
            
        elif int(inputs) == 3:
            year = int(input("Ingrese el año a consultar: "))
            fuel_type = input("Ingrese el tipo de combustible: ").strip()
            min_price = int(input("Ingrese el precio base minimo: "))
            max_price = int(input("Ingrese el precio base maximo: "))
            print_req_3(control, year, fuel_type, min_price, max_price)

        elif int(inputs) == 4:
            year = int(input("Ingrese el anio a consultar: "))
            n = int(input("Ingrese la cantidad N de modelos a mostrar: "))
            print_req_4(control, year, n)

        elif int(inputs) == 5:
            horsepower=int(input("ingrese la potencia (hp) que desea consultar: "))
            delta=int(input("ingrese el valor de delta con el que desea trabajar: "))
            n=int(input("ingrese el numero n de datos que desea conocer: "))
            print_req_5(control,horsepower,delta,n)
            

        elif int(inputs) == 6:
            min_year = int(input("Ingrese el año minimo: "))
            max_year = int(input("Ingrese el año maximo: "))
            min_price = int(input("Ingrese el precio base minimo (USD): "))
            max_price = int(input("Ingrese el precio base maximo (USD): "))
            cantidad_m = int(input("Ingrese la cantidad M de modelos a mostrar: "))
            print_req_6(control, min_year, max_year, min_price, max_price, cantidad_m)
            

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