# AdvancedNetworking_HTTPS_Assignment

#### Environment and tools used for the assignment:
Windows 11, Python 3.10.0, Command Prompt and Google Chrome

#### Question: 
1.(a). Using an appropriate library, write a small web server which takes URLs of the form "http://hostname:port/{add,subtract,multiply,divide}/x/y" and prints the result as a single text/plain result.  So the URL http://hostname:port/add/5/7Links to an external site. 

1.(b). Extend your code to instead of taking a URL containing the expression, instead take JSON via a POST operation.

##### 1. First step:
```
Download the zip file from git repository or clone the repository using:
Command for cloning: git clone https://github.com/kevinsudhir/AdvancedNetworking_HTTPS_Assignment.git
To download zip file, simply open the following link https://github.com/kevinsudhir/AdvancedNetworking_HTTPS_Assignment/archive/refs/heads/main.zip
This will download AdvancedNetworking_HTTPS_Assignment-main zip file and this can be extracted.
After cloning or downloading zip file follow the below steps or follow the extracted Readme_HTTP_Assignment.pdf to further execute the assignment.
```

##### 2. Second step:
- File name to be run from the folder: http_assignment.py
- Run the following command in command prompt/terminal to execute the file according to installed Python environment:
```
py http_assignment.py or 
python http_assignment.py or 
python3 http_assignment.py
```

##### 3. Third step:
- Open any web browser and type the following in address bar to get result for question 1.(a):
```
http://localhost:8000/{add,subtract,multiply,divide}/x/y
For example: http://localhost:8000/multiply/2/6
```

##### 4. Open another command prompt and type the following command to get result for question 1.(b)
```
curl -i -X POST -H "Content-Type:application/json" -d "{  \"operation\" : \"{add,subtract,multiply,divide}\",  \"arguments\" : [x,y] }" http://localhost:8000
For Example: curl -i -X POST -H "Content-Type:application/json" -d "{  \"operation\" : \"divide\",  \"arguments\" : [4,2] }" http://localhost:8000
```
**Note**: This above command is to run in windows command prompt
```
curl -XPOST -d '{"operation":"{add,subtract,multiply,divide}","arguments":[x,y]}' "http://localhost:8080"
For Example: curl -XPOST -d '{"operation":"divide","arguments":[4,7]}' "http://localhost:8080"
```
**Note**: This above command is to run in Linux/Ubuntu shell/terminal or Mac terminal.

##### 5. Following are the results observed
- For question 1.(a):
```
By adding the following as web address in address bar of google chrome: http://localhost:8000/multiply/3/-99
Output in cmd/terminal: 127.0.0.1 - - [10/Dec/2021 07:44:40] "GET /multiply/3/-99 HTTP/1.1" 200 -
Output in chrome: 
HTTP/1.0 200 OK
Server: SimpleHTTP/0.6 Python/3.10.0
Date: Fri, 10 Dec 2021 20:26:42 GMT
Content-type: text/plain
Output: -297.0
```
- For question 1.(b):
```
Running the following command in new cmd: curl -i -X POST -H "Content-Type:application/json" -d "{  \"operation\" : \"divide\",  \"arguments\" : [2,4] }" http://localhost:8000
Running the following command in new Linux/Ubuntu/Mac terminal: curl -XPOST -d '{"operation":"divide","arguments":[2,4]}' "http://localhost:8080"
Output in the main cmd/terminal: 
127.0.0.1 - - [10/Dec/2021 09:15:23] "POST / HTTP/1.1" 200 -
Output in the new cmd/terminal: 
HTTP/1.0 200 OK
Server: SimpleHTTP/0.6 Python/3.10.0
Date: Fri, 10 Dec 2021 09:15:23 GMT
Content-Length: 18
{"Output": "-2.0"}
```
##### 6. To stop the server
```
- Enter Ctrl+C or Cmd+C to stop the server
```