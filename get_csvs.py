import warnings
warnings.simplefilter(action='ignore', category=FutureWarning)

import fastf1
import csv

fastf1.Cache.enable_cache('cache') 

#GPS
mex22 = (2022, 20)

#DRIVERS
dAlb = '23'
dAlo = '14'
dBot = '77'
dGas = '10'
dHam = '44'
dLat = '6'
dLec = '16'
dMag = '20'
dNor = '4'
dOco = '31'
dPer = '11'
dRic = '3'
dRus = '63'
dSai = '55'
dSch = '47'
dStr = '18'
dTsu = '22'
dVer = '1'
dVet = '5'
dZho = '24'

gp = mex22
driver = dVer
#driver = dHam

gp_name = '%s_%s' % (gp[0], gp[1])
#print(gp_name)

ev = fastf1.events.get_event(gp[0], gp[1])
#print(ev)

is_quali = False

if is_quali:
    session_type = 'quali'
else:
    session_type = 'race'

if is_quali:
    session = ev.get_session(ev.Session4) # qualifying in mex
else:
    session = ev.get_session(ev.Session5) # race in mex

session.load(laps=True, telemetry=True, weather=True, messages=True)

print('** SESSION STATUS **')
print(session.session_status)

def getSessionData(session, driver, do_pos=False, do_cd=False, do_laps=False):
    if do_pos:
        pos = session.pos_data.get(driver)

        t = pos.SessionTime.to_list()
        t = map(lambda dt: dt.total_seconds(), t)
        x = pos.X.to_list()
        y = pos.Y.to_list()
        z = pos.Z.to_list()
        positions = list(zip(t, x, y, z))

        with open('%s_%s_pos_%s.csv' % (gp_name, session_type, driver), 'w', encoding='UTF8') as f:
            writer = csv.writer(f)
            writer.writerow(['t', 'x', 'y', 'z'])
            for row in positions:
                writer.writerow(row)

    if do_cd:
        cd = session.car_data.get(driver)

        t = cd.SessionTime.to_list()
        t = map(lambda dt: dt.total_seconds(), t)
        speed = cd.Speed.to_list()
        throttle = cd.Throttle.to_list()
        brake = cd.Brake.to_list()
        gear = cd.nGear.to_list()
        drs = cd.DRS.to_list()
        rpm = cd.RPM.to_list()
        carData = list(zip(t, speed, throttle, brake, gear, drs, rpm))

        with open('%s_%s_cd_%s.csv' % (gp_name, session_type, driver), 'w', encoding='UTF8') as f:
            writer = csv.writer(f)
            writer.writerow(['time', 'speed', 'throttle', 'brake', 'gear', 'drs', 'rpm'])
            for row in carData:
                writer.writerow(row)
    
    if do_laps:
        #laps = session.laps.get(driver)
        laps = session.laps.pick_driver(driver)
        with open('%s_%s_laps_%s.csv' % (gp_name, session_type, driver), 'w', encoding='UTF8') as f:
            f.write(laps.to_csv())
        
        #lap = laps.pick_fastest()
        #print(laps)
        #print(laps.to_csv())

#getSessionData(session, driver, True, True, False)
getSessionData(session, driver, False, False, True)
