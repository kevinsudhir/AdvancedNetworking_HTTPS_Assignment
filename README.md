# AdvancedNetworking_HTTPS_Assignment

### Assignment executed environment and tools
Windows 11, Python 3.10.0 and Command Prompt

##### 1. Question: 1.(a). Using an appropriate library, write a small web server which takes URLs of the form "http://hostname:port/{add,subtract,multiply,divide}/x/y" and prints the result as a single text/plain result.  So the URL http://hostname:port/add/5/7Links to an external site. 
1.(b). Extend your code to instead of taking a URL containing the expression, instead take JSON via a POST operation.

Download the zip file from git repository or git clone the repository
File name to be run: http_server.py

##### 2. First step:
- Run the following command in command prompt to execute the file:
```
py http_server.py or python http_server.py or python3 http_server.py according to installed environment
```

##### 3. Second step:
- Open any web browser and type the following in address bar to get result for question 1.(a):
```
http:\\localhost:8000\{add,subtract,multiply,divide}/x/y
For example: http:\\localhost:8000\add/10/5
```

##### 4. Open another command prompt and type the following command to get result for question 1.(b)
```
curl -i -X POST -H "Content-Type:application/json" -d "{  ^"operation^" : ^"{add,subtract,multiply,divide}^",  ^"arguments^" : [x,y]" }" http://localhost:8000
For Example: curl -i -X POST -H "Content-Type:application/json" -d "{  ^"operation^" : ^"divide^",  ^"arguments^" : [4,2]" }" http://localhost:8000
```
**Note**: This above command is to run in windows command prompt
```
curl -XPOST -d '{"operation":"{add,subtract,multiply,divide}","arguments":[x,y]}' "http://localhost:8080"
For Example: curl -XPOST -d '{"operation":"divide","arguments":[4,7]}' "http://localhost:8080"
```
**Note**: This above command is to run in Linux/Ubuntu shell/terminal or Mac terminal as curl functions well in Mac/Linux/Ubuntu.

##### 5. Following are the results observed
- For question 1.(a):
```
Adding as web address in address bar of google chrome: http://localhost:8000/multiply/3/-99
127.0.0.1 - - [10/Dec/2021 07:44:40] "GET /multiply/3/-99 HTTP/1.1" 200 -
Output: -297.0
```
- For question 1.(b):
```
Running the following command in cmd: curl -i -X POST -H "Content-Type:application/json" -d "{  ^"operation^" : ^"divide^",  ^"arguments^" : [400,6]" }" http://localhost:8000
Running the following command in Linux/Ubuntu/Mac terminal: curl -XPOST -d '{"operation":"divide","arguments":[400,6]}' "http://localhost:8080"
127.0.0.1 - - [09/Dec/2021 23:48:18] "POST / HTTP/1.1" 200 -
{"Output": "66.667"}
```
##### 9. To stop the server
- Enter Ctrl+C or Cmd+C to stop the server
