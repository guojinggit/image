from PIL import ImageGrab
import  log


def screen():
    im = ImageGrab.grab()
    addr = "screen.jpeg"
    im.save(addr, 'jpeg')
    log.info("save jpeg" )