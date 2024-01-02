from PIL import Image
IconMapping = {
0: "sunny.png",
1: "cloudy.png",
2: "cloudy.png",
3: "cloudy.png",
45: "foggy.png",
48: "foggy.png",
51: "drizzle.png",
53: "drizzle.png",
55: "drizzle.png",
56: "drizzle.png",
57: "drizzle.png",
61: "rain.png",
63: "rain.png",
65: "rain.png",
66: "freezing-rain.png",
67: "freezing-rain.png",
71: "snowfall.png",
73: "snowfall.png",
75: "snowfall.png",
78: "snowfall.png",
80: "showers.png",
81: "showers.png",
82: "showers.png",
85: "snowfall.png",
86: "snowfall.png",
95: "thunderstorm.png",
96: "thunderstorm.png",
99: "thunderstorm.png"
}

def getIcon(weather_code):
    return Image.open("./resources/" + IconMapping.get(weather_code, "sunny.png"))

def getIconNight(weather_code):
    if weather_code == 0:
        return Image.open("./resources/sunny-night.png")
    elif weather_code in [1,2,3]:
        return Image.open("./resources/cloudy-night.png")
    else:
        return getIcon(weather_code)