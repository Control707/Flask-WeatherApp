from flask import Flask, request, render_template
from weather import get_weather
from waitress import serve

app=Flask(__name__)

@app.route("/", methods=["GET", "POST"])
@app.route("/index", methods=["GET", "POST"])
def index():
    return render_template("index.html")

@app.route("/weather", methods=["GET", "POST"])
def weather():
    try:
        city = request.args.get("city")
        if not city.strip():
            raise ValueError("City name is empty")
        
        weather = get_weather(city)
        if weather["cod"] != 200:
            raise ValueError(weather["message"].capitalize())
        
        title = weather["name"]
        status = weather["weather"][0]["description"].capitalize()
        temp = f"{weather["main"]["temp"]:.1f}"
        feels = weather["main"]["feels_like"]
    
        return render_template("weather.html", title=title, status=status, temp=temp, feels=feels)
    except ValueError as e:
        return render_template("weather.html", message=str(e))
        

if __name__ == "__main__":
    serve(app, host="0.0.0.0", port=8000)