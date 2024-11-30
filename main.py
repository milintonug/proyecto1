from flask import Flask,render_template, request
import requests

app = Flask(__name__)

def get_weather_data(city:str):
    """
    Funcion que espera el nombre de la ciudad por parametro, para luego realizar un get a openweather
    para consultar el clima de la ciudad ingresada
    """
    API_KEY =  '4028269385f3fcbc8b6677a46432f06a' 
    idioma = 'es'
    url = f'http://api.openweathermap.org/data/2.5/weather?q={city}&units=metric&lang={idioma}&appid={API_KEY}'
    r = requests.get(url).json()
    return r


@app.route("/", methods=['POST', 'GET'])
def index():
    if request.method == 'POST':
        ciudad = request.form.get('txtCiudad')
        if ciudad:
            data = get_weather_data(ciudad)
            cod = data.get('cod')
            if cod != 200:
                return render_template('index.html', ciudad='', humedad='', presion='', descripcion='', icon='', cod=cod , longitud='', latitud='')
            humedad = data.get('main').get('humidity')
            presion = data.get('main').get('pressure')
            longitud = data.get('coord').get('lon')
            latitud = data.get('coord').get('lat')
            descripcion = data.get('weather')[0].get('description')
            icon = data.get('weather')[0].get('icon')
            return render_template('index.html', ciudad=ciudad, humedad=humedad, presion=presion, descripcion=descripcion, icon=icon, cod=cod, longitud=longitud, latitud=latitud)
        else:
            return render_template('index.html', ciudad='', humedad='', presion='', descripcion='', icon='', cod='')
    return render_template('index.html', ciudad='', humedad='', presion='', descripcion='', icon='', cod='')


@app.route("/cv")
def cv():
    return render_template("cv.html")

if __name__ == "__main__":
    app.run(debug=True)