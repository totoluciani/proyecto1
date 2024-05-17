import all_pages
import home_page
import theme

from nicegui import app, ui



@ui.page('/')
def index_page() -> None:
    with theme.frame('Homepage'):
        home_page.content()


# this call shows that you can also move the whole page creation into a separate file
all_pages.create()

ui.image('https://picsum.photos/id/377/640/360')


ui.run()