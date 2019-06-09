# Car_Safety
This program made for help people to drive safety by give a warning. 
This program give you information like distance between your vehicle and the other, accelerometer, and gyroscope.

# Steps:
* Clone the repository or download the zip file and unzip it to a directory of your choice.
* Make sure you have python 3 installed and you can access both pip and python from the command line/ terminal
* To check the same open command line/terminal and type `python --version` and `pip --version`
* cd to the directory where the folder was extracted in the command line

# Directory:

```
|---car_camera
|      |---data
|      |---protos
|      |---ssd_mobilenet_v1_coco_2018_01_28
|      |---utils
|      |---car_safety.py
|---media
|---sensor
|      |---__pycache__
|      |---data
|      |---gui.py
|      |---sensor.py
|---README.md
|---requirements.txt

```

# Pre-install
 ```
 cd Car_Safety
 pip3 install -r requirements.txt
 pip3 install opencv-python
 pip3 install tensorflow  
 pip3 install numpy
 pip3 install matplotlib

 ```

## To Run the car_safety 
 ```
 cd car_camera
 python3 car_safety.py
 ```

## To Run the sensor 
 ```
 # in Car_Safety directory

 cd sensor
 python3 sensor.py

 # for gui (book_id, acceleration_x, acceleration_y, acceleration_z, gyro_x, gyro_y, gyro_z)
 # for book_id its just axample 
 
 python3 gui.py

 ```

## gui.py 

---

<p align="center">
  <img src="/media/gui.png">
</p>

---

## Sensor Format
 ```
 @ sensor.py

 Acceleration:  X:   Y:   Z: 
 Gyro:  X:   Y:   Z:
 ```



