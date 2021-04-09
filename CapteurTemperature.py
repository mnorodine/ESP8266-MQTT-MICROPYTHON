mport machine
import onewire
import ds18x20
import time

ds_pin = machine.Pin(4)  # ou une autre broche libre
#  on peut mettre plusieurs capteurs en parallèle

# crée une classe d'objets ds_capteurs
ds_capteurs = ds18x20.DS18X20(onewire.OneWire(ds_pin))

#  on va chercher les adressses de tous les capteurs DS18b20 présents
adresses = ds_capteurs.scan()
#  on affiche le résultat du scan du bus OneWire
print('Adresse des capteurs DS trouvés : ', adresses)

while True:
    