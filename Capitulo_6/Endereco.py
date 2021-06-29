from pygeocoder import pygeocoder

endereco = 'avenida paulista, 100, Sao Paulo'
resultado = pygeocoder('AIzaSyDR4b40dB9Aamlc7vJBju1FozznNbyN8oM').geocoder(endereco).postal_code
print(resultado)