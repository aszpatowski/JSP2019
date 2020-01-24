import urllib3.request
import sys
import re

if( len( sys.argv ) == 1 ):
    print( "Nie podales sciezki!" )
else:
    f = open( sys.argv[1], 'r' )
    tekst = f.read()
    wyniki = re.findall( 'http[s]?://[^ ;<>]*', tekst )
    if(len(wyniki)==0):
       print("Nie ma")
    else:
        print( wyniki )