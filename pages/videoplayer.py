import theme
from nicegui import ui


def video():
    with theme.frame('Video'):
        ui.page_title('Video')
        ui.markdown('# Video')
        v = ui.video('https://test-videos.co.uk/vids/bigbuckbunny/mp4/h264/360/Big_Buck_Bunny_360_10s_1MB.mp4')
        v.on('ended', lambda _: ui.notify('Video playback completed'))

