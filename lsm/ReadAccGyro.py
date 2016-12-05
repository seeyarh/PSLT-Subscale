from datetime import datetime
from time import sleep
import csv
from altimu import AltIMU


imu = AltIMU()
imu.enable()
imu.calibrateGyroAngles()

start = datetime.now()

while True:
	dataFile = open("AccGyroData.csv", "a")
	data = "\n"
	stop = datetime.now() - start
	start = datetime.now()
	deltaT = stop.microseconds/1000000.0
	
	accList = imu.getAccelerometerAngles()
	data += str(accList[0]) + "," + str(accList[1]) + "," + str(accList[2])
	gyroList = imu.trackGyroAngles(deltaT = deltaT)
	data += "," + str(gyroList[0]) + "," + str(gyroList[1]) + "," +str(gyroList[2])
	dataFile.write(data)
	dataFile.close()
	sleep(.5)

