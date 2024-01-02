def obtainWindDirection(degrees):
    if degrees is None:
        return "Unknown"
    degrees = degrees%360
    if degrees >= 337.5 or degrees < 22.5:
        return "N"
    elif degrees >= 22.5 and degrees < 67.5:
        return "NE"
    elif degrees >= 67.5 and degrees < 112.5:
        return "E"
    elif degrees >= 112.5 and degrees < 157.5:
        return "SE"
    elif degrees >= 157.5 and degrees < 202.5:
        return "S"
    elif degrees >= 202.5 and degrees < 247.5:
        return "SW"
    elif degrees >= 247.5 and degrees < 292.5:
        return "W"
    elif degrees >= 292.5 and degrees < 337.5:
        return "NW"
    else:
        return "Unknown"