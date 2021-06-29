from pygeocoder import pygeocoder

endereco = '393, Rua Dr Jose Maria, Recife, PE'
print(pygeocoder('AIzaSyDR4b40dB9Aamlc7vJBju1FozznNbyN8oM').geocode(endereco).coordinates)