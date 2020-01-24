import urllib3.request
import sys
import re

if( len( sys.argv ) == 1 ):
    print( "Nie podanlej sciezki!" )
else:
    f = open( sys.argv[1], 'r' )
    tekst = f.read()
    wyniki = ' '.join( re.findall( '\s[a|A|E|e][^ .()\n!?,…;:]+', tekst ) )#pojedyncza litera 'a' to dla mnie nie slowo
    print( wyniki )