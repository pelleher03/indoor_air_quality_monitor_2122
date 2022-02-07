from time import sleep
import json
from wlan import connect
import uasyncio
from nanoweb import Nanoweb
import sensors
from html_functions import naw_write_http_header, render_template
from leds import blink

#Koblet til det trådløse nettverket
sta_if = connect()

#Lager en instans av Nanoweb klassen
naw = Nanoweb()

#Lager en global variabel som inneholder all dataen man skal bruke, data fra bmp, ccs og hdc
data = dict(
    bmp = dict(temperature=0, pressure=0),
    ccs = dict(tvoc=0, eco2=0),
    hdc = dict(temperature=0, humidity=0),
    )

#
@naw.route("/")
#Funksjon som returnerer nettsiden
def index(request):
    naw_write_http_header(request)
    html = render_template(
        'index.html',
        temperature_bmp=str(data['bmp']['temperature']),
        pressure=str(data['bmp']['pressure']),
        tVOC=str(data['ccs']['tvoc']),
        eCO2=str(data['ccs']['eco2']),
        temperature_hdc=str(data['hdc']['temperature']),
        humidity=str(data['hdc']['humidity']),
        )
    await request.write(html)


@naw.route("/api/data")
def api_data(request):
    naw_write_http_header(request, content_type='application/json')
    await request.write(json.dumps(data))

#Lager en asynkron løkke
loop = uasyncio.get_event_loop()
#Lager to oppgaver som kan kjøre "samtidig"
#Henter sensor data
loop.create_task(sensors.collect_sensors_data(data, True))
#Kjører nettsiden
loop.create_task(naw.run())
#Gjør at en lysdiode lyser
#loop.create_task(blink())
loop.run_forever()
    

