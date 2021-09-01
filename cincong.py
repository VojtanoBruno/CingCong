#hrac a jeho palce
class Hraci:
    def __init__(self, hrac_cislo, nick):
        self.hrac_cislo = hrac_cislo
        self.nick = nick
    
    def data_hrac(self):
        return {'id': self.hrac_cislo, 'jmeno': self.nick, 'palcu': 2}
    
    list_hracu = []


def palcu_hra():
    for i in range (len(hrac.list_hracu)):
        Hraci.list_hracu[i]['pal_vsazka'] = int(input(f"Hráči {hrac.list_hracu[i]['jmeno']}, Kolik palcu bude dohromady zvedlich? "))
        Hraci.list_hracu[i]['pal_ve_hre'] = int(input(f"Hráči {hrac.list_hracu[i]['jmeno']}, kolik palců zvedáš ty? (0-2) "))

def palcu_ve_hre():
    celkem_palcu = 0
    for i in range (len(hrac.list_hracu)):
        celkem_palcu = celkem_palcu + hrac.list_hracu[i]['pal_ve_hre']
    return celkem_palcu
    
def vyhodnoceni():
    for i in range (len(Hraci.list_hracu)):
        if hrac.list_hracu[i]['pal_vsazka'] == palcu_ve_hre():
            print(f"{hrac.list_hracu[i]['jmeno']} BINGO!!!")
            hrac.list_hracu[i]['palcu'] = hrac.list_hracu[i]['palcu'] - 1
            print(f" Zbyva ti {hrac.list_hracu[i]['palcu']} palcu")
        else:
            print(f"{hrac.list_hracu[i]['jmeno']} smůla smůla smůlička")
            print(f" Zbyva ti {hrac.list_hracu[i]['palcu']} palcu")
        

#momentalni soucet vsech palcu
def soucet_palcu():
    zbyv_pal = 0
    for i in range (len(hrac.list_hracu)):
        zbyv_pal = zbyv_pal + hrac.list_hracu[i]['palcu']
    return zbyv_pal

#vstupni nastaveni poctu hracu a jejich nicků
pocet_hracu = int(input("Zadej počet hráčů: "))
for i in range (pocet_hracu):
    nick = str(input(f'Zadejte nick {i+1}. hráče:'))
    hrac = Hraci(i+1, nick)
    hrac.list_hracu.append(hrac.data_hrac())



    #print(hrac.data_hrac())
    #print(f"Hráč číslo {hrac.data_hrac()['id']} s přezdívkou {hrac.data_hrac()['jmeno']} má {hrac.data_hrac()['palcu']} palců")
#print(hrac.list_hracu[0]['jmeno'])



print(f've hře je {len(hrac.list_hracu)} hráčů a dohromady mají ve hře {soucet_palcu()} palců')
palcu_hra()
vyhodnoceni()
