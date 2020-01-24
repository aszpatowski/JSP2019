import urllib3.request
import http.server

strona = urllib3.PoolManager()
strona1 = urllib3.PoolManager()
r = strona.request('GET', 'http://www.wp.pl')
nie = strona1.request('GET', 'http://www.wp.pl/tak')

print( r.status )
print( http.server.BaseHTTPRequestHandler.responses[ r.status ] )

print( nie.status )
print( http.server.BaseHTTPRequestHandler.responses[ nie.status ] )
