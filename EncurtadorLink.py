import pyshorteners
url = input('Entre com a LINK que será encurtada: ')
s = pyshorteners.Shortener().tinyurl.short(url)
print('Sue LINK encurtado : {}'.format(s))