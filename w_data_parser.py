from collections import namedtuple
import sys

WEATHER_DATA_FILE = "w_data.dat"

DAY_INDEX = 0
WEATHER_MAX_INDEX = 1
WEATHER_MIN_INDEX = 2

WeatherSpread = namedtuple("WeatherSpread", "day spread")


def parse_line(line_parts):
    # skip anything under outside WEATHER_MIN_INDEX, the last index we care about
    if len(line_parts) <= WEATHER_MIN_INDEX:
        return
    day = line_parts[DAY_INDEX]
    weather_max = line_parts[WEATHER_MAX_INDEX]
    weather_min = line_parts[WEATHER_MIN_INDEX]

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
with open(WEATHER_DATA_FILE) as f:
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
