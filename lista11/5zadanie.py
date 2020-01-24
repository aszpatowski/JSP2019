import urllib3.request
import sys
import re

if( len( sys.argv ) == 1 ):
    print( "Nie podales sciezki!" )
else:
    tekst = "PythonExcercises"#f.read()
    wyniki = ' '.join( re.findall( '[A-Z][^ .()\n!?,…;:A-Z]+', tekst ) )#pojedyncza litera 'a' to dla mnie nie slowo
    print( wyniki )
