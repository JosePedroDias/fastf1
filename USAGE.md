# fastf1

https://theoehrly.github.io/Fast-F1/index.html

```
pip3 install fastf1
```

```py
import fastf1

#optional
fastf1.Cache.enable_cache('cache') 

ev = fastf1.events.get_event(2022, 20)
sess = ev.get_session(ev.Session4) # qualifying
sess = ev.get_session(ev.Session5) # race

sess.load(laps=True, telemetry=True, weather=True, messages=True)
# https://theoehrly.github.io/Fast-F1/core.html#fastf1.core.Session.load

pos1 = sess.pos_data.get('1') # max
pos1 = sess.pos_data.get('22') # tsu
#pos1.X,Y,Z
#.to_list(), .to_json()

xs = pos1.X.to_list()
ys = pos1.Y.to_list()
zs = pos1.Z.to_list()
positions = list(zip(xs, ys, zs))

import csv
with open('pos.csv', 'w', encoding='UTF8') as f:
    writer = csv.writer(f)
    writer.writerow(['x', 'y', 'z'])
    for x, y, z in positions:
      writer.writerow([x, y, z])

cd = sess.car_data.get('1')
cd.SessionTime, Speed, Throttle, Brake, nGear, DRS, RPM, Time, (T)

with open('sd.csv', 'w', encoding='UTF8') as f:
    writer = csv.writer(f)
    writer.writerow(['time', 'speed', 'throttle', 'brake', 'gear', 'drs', 'rpm'])
    for i in range(len(cd)):
      o = cd.T[i]
      writer.writerow([o.SessionTime, o.Speed, o.Throttle, o.Brake, o.nGear, o.DRS, o.RPM])

t = cd.SessionTime.to_list()
speed = cd.Speed.to_list()
throttle = cd.Throttle.to_list()
brake = cd.Brake.to_list()
gear = cd.nGear.to_list()
drs = cd.DRS.to_list()
rpm = cd.RPM.to_list()
carData = list(zip(t, speed, throttle, brake, gear, drs, rpm))

with open('carData.csv', 'w', encoding='UTF8') as f:
    writer = csv.writer(f)
    writer.writerow(['time', 'speed', 'throttle', 'brake', 'gear', 'drs', 'rpm'])
    for row in carData:
      writer.writerow(row)

driverLaps = sess.laps.pick_driver('LEC')
lap = driverLaps.pick_fastest()
lap.to_json()

sess.session_status
sess.results
sess.car_data
sess.pos_data
```

- https://matplotlib.org/stable/gallery/lines_bars_and_markers/simple_plot.html
- https://www.f1-tempo.com/
- https://medium.com/towards-formula-1-analysis/
- how-to-analyze-formula-1-telemetry-in-2022-a-python-tutorial-309ced4b8992
