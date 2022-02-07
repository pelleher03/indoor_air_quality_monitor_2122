import network

#Sier til programmet hva navnet på nettverket er, og hva passoret er
ssid = 'VG3Data'
password = 'Admin:1234'

def connect():
    #Sier at ESP32 skal settes opp som en trådløs enhet
    sta_if = network.WLAN(network.STA_IF)
    #Om ESP32 ikke er koblet til, skal man aktivere og koble enheten til nettverket
    if not sta_if.isconnected():
        sta_if.active(True)
        sta_if.connect(ssid, password)
        #ESP32 bil gå i en evig loop helt til den blir koblet til
        while sta_if.isconnected() == False:
          pass
        print('Connection successful')
    #Om ESP32 er koblet til vil den printe dette ut og returnere dette.
    else:
        print('Already connected!')
    print(sta_if.ifconfig())
    return sta_if
