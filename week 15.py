from datetime import datetime,timedelta

def world_times():
    my_city = datetime.now()
    berlin = my_city - timedelta(hours = 7)
    baguio_city = datetime.now()
    las_vegas = my_city + timedelta(hours = 8)
    all_times = f"It is {my_city:%I:%M} in my city.That means it's {berlin:%I:%M} in Berlin, {baguio_city:%I:%M} in Baguio City and  {las_vegas:%I:%M} in Las Vegas!"
    print(all_times)

world_times()
