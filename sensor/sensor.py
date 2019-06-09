from flask import Flask 
from flask_sockets import Sockets
import time
import os
import subprocess
import sys


app = Flask(__name__) 
sockets = Sockets(app)

global book_id
book_id = sys.argv[1]

folder = './data/'

@sockets.route('/accelerometer') 
def echo_socket(ws):
	f=open(folder + book_id + "accl.txt","a")
	while True:
		message = ws.receive()
		data = message.split(',')
		acceleration_x = '{0:.5}'.format(data[0])
		acceleration_y = '{0:.5}'.format(data[1])
		acceleration_z = '{0:.5}'.format(data[2])
		warning = 0

		for i in str(warning):
			if float(acceleration_x) >= 8.0:
				print('WARNING!')
				warning += 1
				break
			if float(acceleration_x) <= -8.0:
				print('WARNING!')

		acceleration = 'Acceleration:  X:' + acceleration_x + ' ' + 'Y:' + acceleration_y + ' ' + 'Z:' + acceleration_z + ' ' + 'Warning: ' + str(warning)
		print(acceleration)
		ws.send(message)
		f.write(acceleration + '\n')
		f.flush()
    		
	f.close()


@sockets.route('/gyroscope') 
def echo_socket(ws):
	f=open(folder + book_id + "gyro.txt","a")
	while True:
		message = ws.receive()
		data = message.split(',')
		gyro_x = '{0:.5}'.format(data[0])
		gyro_y = '{0:.5}'.format(data[1])
		gyro_z = '{0:.5}'.format(data[2])
		gyro = 'Gyro: X:' + gyro_x + ' ' + 'Y:' + gyro_y + ' ' + 'Z:' + gyro_z
		print(gyro)
		ws.send(message)
		f.write(gyro + '\n')
		f.flush()
	f.close()


@sockets.route('/geolocation')
def echo_socket(ws):
	f=open(book_id + "geo.txt","a")
	while True:
		message = ws.receive()
		print(message)
		ws.send(message)
		print(message, file=f)
	f.close()
	

@app.route('/') 
def hello(): 
	return 'Hello World!'

if __name__ == "__main__":
	from gevent import pywsgi
	from geventwebsocket.handler import WebSocketHandler
	server = pywsgi.WSGIServer(('0.0.0.0', 5000), app, handler_class=WebSocketHandler)
	server.serve_forever()
