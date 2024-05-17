from nicegui import ui
from pages.videoplayer import video
from pages.cars import cars
from pages.tablas import tabla

def create() -> None:
    ui.page('/video/')(video)
    ui.page('/cars/')(cars)
    ui.page('/tablas/')(tabla)

if __name__ == '__main__':
    create()