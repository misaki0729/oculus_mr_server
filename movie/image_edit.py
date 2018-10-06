#!/usr/bin/python
'''
	orig author: Igor Maculan - n3wtron@gmail.com
	A Simple mjpg stream http server
'''
import cv2
from BaseHTTPServer import BaseHTTPRequestHandler,HTTPServer
import time

capture=None

class CamHandler(BaseHTTPRequestHandler):
	def do_HEAD(self):
		print self.path
		self.send_response(200)
		self.send_header('Content-type','multipart/x-mixed-replace; boundary=--jpgboundary')
		self.end_headers()		
	def do_GET(self):
		print("pythn")
		self.send_response(200)
		# self.send_header('Content-type','multipart/x-mixed-replace; boundary=--jpgboundary')
		self.send_header('Content-type','image/jpeg;')
		self.end_headers()
		count = 0
		while True:
			rc,img = capture.read()
			if not rc:
				return
			imgRGB = cv2.cvtColor(img,cv2.COLOR_BGR2RGB)
			r, buf = cv2.imencode(".jpg",imgRGB)
			cv2.imwrite("test" + str(count) + ".jpg", imgRGB)
			count += 1
		# self.wfile.write("--jpgboundary\r\n")
		self.send_header('Content-type','image/jpeg')
		self.send_header('Content-length',str(len(buf)))
		self.end_headers()
		self.wfile.write(bytearray(buf))
		self.wfile.write('\r\n')
		time.sleep(0.1)
		return

def main():
	global capture
	capture = cv2.VideoCapture(0)
	capture.set(cv2.CAP_PROP_FRAME_WIDTH, 1280) 
	capture.set(cv2.CAP_PROP_FRAME_HEIGHT, 720)
	try:
		server = HTTPServer(('',9090),CamHandler)
		print "server started"
		server.serve_forever()
	except KeyboardInterrupt:
		capture.release()
		server.socket.close()

if __name__ == '__main__':
	main()