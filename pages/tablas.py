from nicegui import ui
import theme
from typing import Dict
import pandas as pd
import os

#Definir columnas en la tabla (informacion de como esta compuesta)
columns = [
    {'name': 'name', 'label': 'Name', 'field': 'name', 'required': True, 'align': 'left'},
    {'name': 'age', 'label': 'Age', 'field': 'age', 'sortable': True},
    {'name': 'nationality','label':'Nationality','field':'nationality','sorteable': False}
]   
#Definir filas en la tabla (informacion dentro de la tabla)
rows = [
    {'name': 'Alice', 'age': 18, 'nationality': 'Brazilian'},
    {'name': 'Bob', 'age': 21, 'nationality': 'American'},
    {'name': 'Carol','nationality': 'American'},
]

#Definir funcion 'tabla' para poder llamarla luego desde 'all_pages.py' 
def tabla():
    #Definir funcion para poder pasarlo a csv e importarlo
    def download_csv():
        # Crear el DataFrame a partir de 'rows' ya que 'rows' incluye la informacion de la tabla y 'colums' la descripcion de la tabla
        df = pd.DataFrame(rows)
        
        # Obtener la ruta de la carpeta de descargas del usuario
        downloads_folder = os.path.join(os.path.expanduser('~'), 'Downloads')
        
        # Ruta completa donde poner el archivo csv en la carpeta de descargas
        csv_path = os.path.join(downloads_folder, 'tabla.csv')

        # Guardar el DataFrame como archivo CSV en la carpeta de descargas
        df.to_csv(csv_path, index=False)

    # Llamar a la función download_csv al hacer clic en el botón
    ui.button("Importar", on_click=download_csv)

    with theme.frame('Tablas'):
        ui.page_title('Tablas')
    #Darle un nombre a la variable para despues poder agregarle un menu para filtrar (esta variable permite mostrar la tabla con sus valores asignados)
    tablax = ui.table(columns=columns, rows=rows, row_key='name')
    #Menu para filtrar
    def toggle(column: Dict, visible: bool) -> None:
        column['classes'] = '' if visible else 'hidden'
        column['headerClasses'] = '' if visible else 'hidden'
        tablax.update()

    with ui.button(icon='menu'):
        with ui.menu(), ui.column().classes('gap-0 p-2'):
            for column in columns:
                ui.switch(column['label'], value=True, on_change=lambda e,
                        column=column: toggle(column, e.value))
    

    #Se define nueva funcion para poder agregar 'name'
    def add_task():
        #task_name mediante .value.strip() consigue el valor de task_item... no se puede poner task_item directamente ya que representa un campo de entrada y no el valor en si mismo como sucede normalmente
        task_name = task_item.value.strip()
        #se compara a la nueva variable con False/0/""
        if not task_name:
            ui.notify('NO PUEDE ESTAR VACIO')
        #se compara a la nueva variable con True/1/"valor real"
        else:
            tablax.add_rows({'name': task_name})
            task_item.value = ""
            


    task_item = ui.input("Ingrese un nombre")
    ui.button("agregar",on_click=add_task)
    