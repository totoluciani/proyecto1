from nicegui import ui


def menu() -> None:
    ui.link('Home', '/').classes(replace='text-black')
    ui.link('Video', '/video/').classes(replace='text-black')
    ui.link('Cars', '/cars/').classes(replace='text-black')
    ui.link('Tablas','/tablas/').classes(replace='text-black')