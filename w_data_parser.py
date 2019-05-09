from collections import namedtuple
import sys


WeatherSpread = namedtuple("WeatherSpread", "day spread")


def parse_line(line_parts):
    # skip anything under 3 elements to avoid out of bound indices
    if len(line_parts) < 3:
        return
    day = line_parts[0]
    weather_max = line_parts[1]
    weather_min = line_parts[2]

    if not day.isdigit():
        return
    day = int(day)

    if not weather_max.replace(".", "").isdigit():
        return
    weather_max = float(weather_max)

    # its probably safe to assume if we gotten here we can just parse for a float, but i will check for consistency/safety
    if not weather_min.replace(".", "").isdigit():
        return
    weather_min = float(weather_min)
    return WeatherSpread(day=day, spread=weather_max - weather_min)


least_weather_spread = WeatherSpread(day=-1, spread=sys.float_info.max)

# lazily read w_data line by line
with open("w_data.dat") as f:
    for line in f:
        weather = parse_line(line.split())
        if not weather:
            continue
        if weather.spread < least_weather_spread.spread:
            least_weather_spread = weather

print(least_weather_spread)

# # functional approach, not lazy, loads entire file into memory
# f = open('w_data.dat')
# result = min(filter(lambda x: x != None, map(parse_line, map(lambda l: l.split(), f.readlines()))), key=lambda x: x.spread)
# print(result)
