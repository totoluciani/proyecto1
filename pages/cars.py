import theme
from nicegui import ui
from datetime import datetime

def cars():
    with theme.frame('Cars'):
        ui.page_title('Cars')
        ui.markdown('# Cars page')
        ui.icon('star')
        label = ui.label()
        ui.label('The lyrics of "Everlong" by Foo Fighters express longing and devotion.')
        ui.link('My instagram', 'https://www.instagram.com/totolucianii/')
        ui.timer(1.0, lambda: label.set_text(f'{datetime.now():%X}'))
        ui.chat_message('Hello NiceGUI!',
                        name='Messi',
                        stamp='now',
                        avatar='https://upload.wikimedia.org/wikipedia/commons/b/b4/Lionel-Messi-Argentina-2022-FIFA-World-Cup_%28cropped%29.jpg')

        with ui.dropdown_button('Cars', auto_close=True):
            ui.item('Porsche 911', on_click=lambda: ui.navigate.to ('https://es.wikipedia.org/wiki/Porsche_911'))
            ui.item('Lamborghini Aventador', on_click=lambda: ui.navigate.to ('https://es.wikipedia.org/wiki/Lamborghini_Aventador'))



