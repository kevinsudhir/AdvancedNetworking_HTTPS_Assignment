import http.server
import socketserver
import json

class MyHttpRequestHandler(http.server.SimpleHTTPRequestHandler):
	# Function for web server which takes URLs of the form
	def do_GET(self):
		# Setting headers
		self.send_response(200)
		self.send_header("Content-type", "text/plain")
		self.end_headers()

		self.wfile.write(bytes(self.headers.send_response))

		address = self.path[1:].split('/')	

		res = 0
		
		try:
			# Printing error and skipping execution if address length is wrong
			if(len(address)<3 or len(address)>3):
				res = "404 Client Error: URL NOT FOUND. Enter correct URL"
			else:	
					# Executing respective operations from the data obtained through URL
					if address[0] == 'add':
						res = add(address[1],address[2])				
					elif address[0] == 'subtract':
						res = sub(address[1],address[2])				
					elif address[0] == 'multiply':
						res = mul(address[1],address[2])				
					elif address[0] == 'divide':
						res = div(address[1],address[2]) 
					# Printing error if operation is given wrong
					else:	
						res = "404 Client Error: URL NOT FOUND. Enter correct URL"
		# Except block to catch unexpected error			
		except:
			res = "Something went wrong"

		finally:
			self.wfile.write("Output: ".encode())
			self.wfile.write(str(res).encode())

	# Function for web server which takes JSON via a POST operation
	def do_POST(self):
		try:
			self.data_string = self.rfile.read(int(self.headers['Content-Length']))
			data= json.loads(self.data_string)
			res=0

			argsLen = len(data['arguments'])
			
			# Printing error and skipping execution if address length is wrong
			if(argsLen < 2 or argsLen > 2 or len(data)<2):
				res = "Error: Enter correct number of arguments"

			else:
				# Executing respective operations from the data obtained through JSON
				if(data['operation']=='add'):
					res=add(data['arguments'][0],data['arguments'][1])
				
				elif(data['operation']=='subtract'):
					res=sub(data['arguments'][0],data['arguments'][1])
				
				elif(data['operation']=='multiply'):
					res=mul(data['arguments'][0],data['arguments'][1])
				
				elif(data['operation']=='divide'):
					res=div(data['arguments'][0],data['arguments'][1])
				
				else:	
					# Printing error if operation data is given wrong
					res = "Error: Enter correct operation value"
					
		# Except block to catch unexpected error				
		except:
			res="There is an error in input"
		
		finally:
			#Assigning Output	
			result= str(json.dumps({'Output': str(res)}))

			# Setting headers
			self.send_response(200)
			self.send_header("Content-Length",str(len((result))))
			self.end_headers()

			#Printing output
			self.wfile.write(str(result).encode())

# functions for operations			
def add(x,y):
	result = float(x) + float(y)
	return result
	
def sub(x,y):
	result = float(x) - float(y)
	return result
	
def mul(x,y):
	result = float(x) * float(y)
	return result  
	
def div(x,y):
	try:
		result = format(float(x) / float(y),".3f")
	# Catching Zero Division error
	except ZeroDivisionError as error:
		result = error	
	finally:
		return result

# main function
def main():
	handler_object = MyHttpRequestHandler
	PORT = 8000
	myserver = socketserver.TCPServer(("", PORT), handler_object)
	print('Server started')
	print('Server is running on the port: %s' % PORT)
	
	try:
		myserver.serve_forever()
	except RuntimeError:
		myserver.shutdown()
		sys.exit()
	except KeyboardInterrupt:
		pass

	myserver.server_close()
	print("Server stopped")

# calling the main function	
if __name__ == '__main__':
	main() 
	