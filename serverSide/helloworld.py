
from bottle import route, run, request, static_file
import sys, json

root_dir='.'

@route('/web/<path:path>')
def static(path):
    return static_file(path,root_dir)

@route('/hello')
def hello():
    return "Hello World!"

@route('/test')
def test():
    return request.query['par']



if len(sys.argv)==1:
	run(host='localhost', port=8080, debug=True)
elif len(sys.argv)==2:
	run(host='localhost', port=sys.argv[1], debug=True)
else:
	run(host=sys.argv[1], port=sys.argv[2], debug=True)
