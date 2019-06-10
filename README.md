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

## car_safety.py Demo

<p align="center">
  <img src="/media/demo.png">
</p>

---

* Terminal
```
 ...

 Distance (meter): 5.3772297  5.9687967 10.231259  11.89317
 Distance (meter): 5.3772297  5.9687967 10.231259  11.89317
 
```

## How To Change Video Input

* Default

```python
# Input video
# For using video file
cap = cv2.VideoCapture('../media/2.mp4')
# For using camera
#cap = cv2.VideoCapture(1)

```

* Use camera

```python
# Input video
# For using video file
#cap = cv2.VideoCapture('../media/2.mp4')
# For using camera
"""
my laptop have 2 cam, so i use 'cv2.VideoCapture(1)' to use rear camera,
if your laptop have 1 camera change it to 'cv2.VideoCapture(0)'
"""
cap = cv2.VideoCapture(1)

```

## To Run speedometer 

* speed_raspberry.py 
can only run on raspberry pi 3.

 ```
 # in car_camera directory

 python3 speed_raspberry.py

 ```

* speed_android.py 
can only run on android.

 ```
 # in car_camera directory

 python3 speed_android.py

 ```

## To Run the sensor 
sensor.py can only run on raspberry pi 3.

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



