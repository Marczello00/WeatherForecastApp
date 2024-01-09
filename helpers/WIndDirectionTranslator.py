def obtainWindDirection(degrees):
    if degrees is None:
        return "Unknown"
    degrees = degrees % 360
    if degrees >= 337.5 or degrees < 22.5:
        return "N"
    elif 22.5 <= degrees < 67.5:
        return "NE"
    elif 67.5 <= degrees < 112.5:
        return "E"
    elif 112.5 <= degrees < 157.5:
        return "SE"
    elif 157.5 <= degrees < 202.5:
        return "S"
    elif 202.5 <= degrees < 247.5:
        return "SW"
    elif 247.5 <= degrees < 292.5:
        return "W"
    elif 292.5 <= degrees < 337.5:
        return "NW"
    else:
        return "Unknown"
