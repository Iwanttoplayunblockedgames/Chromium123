import os

try:
    from webbot import Browser
except ModuleNotFoundError:
    os.system('pip install webbot')
    from webbot import Browser

web = Browser()

web.go_to("https://google.com")

while True:
    print(input())