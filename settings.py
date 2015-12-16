comprotocol = 'http'
serverdomain = 'localhost'
projectname = 'condoproject'
base_url = comprotocol + '://' + serverdomain + '/' + projectname

login_url = base_url + '/usuarios/restLogin/'


kapp = None

req_headers = {
	'Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,*/*;q=0.8',
	'Accept-Encoding': 'gzip, deflate',
	'Accept-Language': 'es-ES,es;q=0.8,en-US;q=0.5,en;q=0.3',
	'Connection': 'keep-alive',
	'Host': 'localhost',
	'User-Agent': 'Mozilla/5.0 (Windows NT 6.1; rv:42.0) Gecko/20100101 Firefox/42.0'
}