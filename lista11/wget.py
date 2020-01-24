import urllib3.request
import sys

if( len( sys.argv ) == 1 ):
    print( "Nie podano URL!" )
    exit
else:
    strona = urllib3.PoolManager()
    r = strona.request('GET', sys.argv[1] )
    #print( r.data )
    if( sys.argv[1][ len( sys.argv[1] ) - 1 ] == '/' ):
        nazwa = 'index.html'
    else:
        nazwa = sys.argv[1].split('.')
        if( 'www' not in nazwa[0] ):
            nazwa = nazwa[0].split('/')[2] + '.html'
        else:
            nazwa = nazwa[1] + '.html'
    f = open( nazwa, 'w' )
    f.write( str(r.data) )

