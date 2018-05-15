
from bottle import route, run, request, static_file
import sys, json

root_dir='.'


list_colors=[]

@route('/cb/setColor')
def setColor():
	list_colors.append(request.query.color)
	return json.dumps({"pos":[0.5,0.5]})
	

@route('/cb/getColors')
def getColor():
	return json.dumps(list_colors)	

@route('/cb/clearColors')
def getColor():
	list_colors=[]
	return ""
	


@route('/cb/<path:path>')
def static(path):
    return static_file(path,'cb')
    


@route('/cb')
def index():
    return static_file('index.html','cb')

if len(sys.argv)==1:
	run(host='localhost', port=8080, debug=True)
elif len(sys.argv)==2:
	run(host='localhost', port=sys.argv[1], debug=True)
else:
	run(host=sys.argv[1], port=sys.argv[2], debug=True)
