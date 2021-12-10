import http.server
import socketserver
import json
import re

class MyHttpRequestHandler(http.server.SimpleHTTPRequestHandler):
	# Function for web server which takes URLs of the form
	def do_GET(self):
		# Setting headers
		self.send_response(200)
		self.send_header("Content-type", "text/plain")
		self.end_headers()

		address = self.path[1:].split('/')	

		error = 0
		res = 0
		res = testcases(address)
		try:
			# Printing error and skipping execution if address length is wrong
			if res == 0:	
					# Executing respective operations from the data obtained through URL
					if address[0].lower() == 'add':
						res = add(address[1],address[2])				
					elif address[0].lower() == 'subtract':
						res = sub(address[1],address[2])				
					elif address[0].lower() == 'multiply':
						res = mul(address[1],address[2])				
					elif address[0].lower() == 'divide':
						res = div(address[1],address[2]) 
						if any(ch.isalpha() for ch in res):
							error = 1							
					# Printing error if operation is given wrong
					else:	
						res = "404 Client Error: URL NOT FOUND. Enter correct operator"
						error = 2
			else:
				error = 1

		# Except block to catch unexpected error			
		except:
			res = "Something went wrong"
			error = 2
		finally:
			if error == 0:
				self.send_response(200)
			elif error == 1:
				self.send_response(405)
			else:
				self.send_response(404)
			
			self.send_header("Content-type", "text/plain")
			self.end_headers()	
			self.wfile.write("Output: ".encode())
			self.wfile.write(str(res).encode())


	# Function for web server which takes JSON via a POST operation
	def do_POST(self):
		try:
			self.data_string = self.rfile.read(int(self.headers['Content-Length']))
			data= json.loads(self.data_string)
			res=0
			error = 0

			argsLen = len(data['arguments'])
			
			# Printing error and skipping execution if address length is wrong
			if(argsLen < 2 or argsLen > 2 or len(data)<2):
				res = "Error: Enter correct number of arguments"
				error = 1
			else:
				# Executing respective operations from the data obtained through JSON

				if(data['operation'].lower()=='add'):
					res=add(data['arguments'][0],data['arguments'][1])
				
				elif(data['operation'].lower()=='subtract'):
					res=sub(data['arguments'][0],data['arguments'][1])
				
				elif(data['operation'].lower()=='multiply'):
					res=mul(data['arguments'][0],data['arguments'][1])
				
				elif(data['operation'].lower()=='divide'):
					res=div(data['arguments'][0],data['arguments'][1])
					if any(ch.isalpha() for ch in res):
							error = 2
				else:	
					# Printing error if operation data is given wrong
					res = "Error: Enter correct operation value"
					error = 2
					
		# Except block to catch unexpected error				
		except:
			res="Error: Enter correct arguments"
			error = 1
		finally:
			#Assigning Output	
			result= str(json.dumps({'Output': str(res)}))

			if error == 0:
				self.send_response(200)
			elif error == 1:
				self.send_response(404)
			else:
				self.send_response(405)

			# Setting headers			
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
		result = "Error: Division by zero is not possible"	
	finally:
		return result

# Test cases to find error and print it
def testcases(address):
	special_characters = '"!@#$%^&*()-+?_=,<>/"'
	if(len(address)<3 or len(address)>3):
		result = "404 Client Error: URL NOT FOUND. Enter correct URL"
	elif address[1]=='' or address[2]=='':
		if address[1]=='':
			result = "404 Client Error: URL NOT FOUND. Argument 1 cannot be empty"
		else:	
			result = "404 Client Error: URL NOT FOUND. Argument 2 cannot be empty"
	elif any(ch.isalpha() for ch in address[1]) or 	any(ch.isalpha() for ch in address[2]):
		result = "404 Client Error: URL NOT FOUND. Arguments cannot have alphabets"
	elif any(ch in special_characters for ch in address[1]) or any(ch in special_characters for ch in address[2]):
		result = "404 Client Error: URL NOT FOUND. Arguments cannot have special characters"
	else:	
		result=0

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
	