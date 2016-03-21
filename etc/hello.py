def application(environ, start_response):
	#
	body=''
	if environ['QUERY_STRING']:
		a=environ['QUERY_STRING'].split('&')
		for i in a:
			body+=i+'\n'
	#
	status = '200 OK'
	headers = [('Content-Type', 'text/plain')]
	
	start_response(status, headers)
	return body

#dic1={'QUERY_STRING':'a=5&b=3&c=lolo'}
#print(wsgi_application(dic1,))
