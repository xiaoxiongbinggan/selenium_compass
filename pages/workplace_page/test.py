import time

a=time.strftime('%Y%m%d-%H%M%S') + '.png'
b=time.localtime()
c=time.strftime('%D-%S')
e=time.strftime('%Y%M%D-%H%M%S')
print(a)
print(c)
print(e)


def screen_short(self):
    filename = time.strftime('%Y%m%d-%H%M%S') + '.png'
    self.driver.get_screenshot_as_png(filename)