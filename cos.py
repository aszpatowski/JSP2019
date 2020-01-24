import numpy as np
#np.set_printoptions(threshold=np.nan)
        

class vec_spin:
    
    def __init__(self, s):
        self.s = s
        self.h = 1
        vx = [0.5*np.sqrt((a-1)*(2*self.s+2-a)) for a in range(2,int(2*s+2))]
        self.x = np.diag(vx,k=1) + np.diag(vx,k=-1)
        vy = [0.5j*np.sqrt((a-1)*(2*self.s+2-a)) for a in range(2,int(2*s+2))]
        self.y = np.diag(vy,k=1) + np.diag(vy,k=-1)
        self.z = np.diag([-a+1+s for a in range(1,int(2*s + 2))])

#    def tensorProd(sSpinelf, A, B):
#        return np.kron(A, B)
def S( s, i, n ):
    Spin = vec_spin(s)
    if( i == 1 ):
        Spin.Sx = np.kron( Spin.x, np.identity( int( s * 2 + 1 ) ** ( n - 1 ) ) )
        Spin.Sy = np.kron( Spin.y, np.identity( int( s * 2 + 1 ) ** ( n - 1 ) ) )
        Spin.Sz = np.kron( Spin.z, np.identity( int( s * 2 + 1 ) ** ( n - 1 ) ) )
    elif( i < n ):
        Spin.Sx = np.kron( np.kron( np.identity( int( s * 2 + 1 ) ** (i-1) ), Spin.x  ), np.identity( int(s * 2 + 1) ** (n - i) ) )
        Spin.Sy = np.kron( np.kron( np.identity( int( s * 2 + 1 ) ** (i-1) ), Spin.y  ), np.identity( int(s * 2 + 1) ** (n - i) ) )
        Spin.Sz = np.kron( np.kron( np.identity( int( s * 2 + 1 ) ** (i-1) ), Spin.z  ), np.identity( int(s * 2 + 1) ** (n - i) ) )
    else:
        Spin.Sx = np.kron( np.identity( int( s * 2 + 1 ) ** ( n - 1 ) ), Spin.x )
        Spin.Sy = np.kron( np.identity( int( s * 2 + 1 ) ** ( n - 1 ) ), Spin.y )
        Spin.Sz = np.kron( np.identity( int( s * 2 + 1 ) ** ( n - 1 ) ), Spin.z )
    return Spin

def H( s, n, j, h ):
    Spiny = []
    SumaS = [ np.zeros( (int( 2 * s + 1 ) ** n, int( 2 * s + 1 ) ** n ), dtype=complex) for i in range(3) ] # wynik[0] = Sx, wynik[1] = Sy, wynik[2] = Sz
    for i in range(1, n + 1):
        Spiny.append( S( s, i, n) )
        
    for i in range( len( Spiny ) - 1 ):
        SumaS[0] += Spiny[ i ].Sx @ Spiny[ i+1 ].Sx
        SumaS[1] += Spiny[ i ].Sy @ Spiny[ i+1 ].Sy
        SumaS[2] += Spiny[ i ].Sz @ Spiny[ i+1 ].Sz

    SumaS[0] += Spiny[ 0 ].Sx @ Spiny[ n-1 ].Sx
    SumaS[1] += Spiny[ 0 ].Sy @ Spiny[ n-1 ].Sy
    SumaS[2] += Spiny[ 0 ].Sz @ Spiny[ n-1 ].Sz

    SumaSi = SumaS[0] + SumaS[1] + SumaS[2]
    SumaHz = np.zeros( (int( 2 * s + 1 ) ** n, int( 2 * s + 1 ) ** n ), dtype=complex )

    for i in range(n):
        SumaHz += Spiny[i].Sz
    return j * SumaSi - h * SumaHz

def H2( s, n, j, h, start, stop ):
    Spiny = []
    SumaS = [ np.zeros( (int( 2 * s + 1 ) ** n, int( 2 * s + 1 ) ** n ), dtype=complex) for i in range(3) ] # wynik[0] = Sx, wynik[1] = Sy, wynik[2] = Sz
    for i in range( start, stop +1 ):#range(1, n + 1):
        print()
        Spiny.append( S( s, i, n ) )
        
    for i in range( len( Spiny ) - 1 ): #celowo krotsze o 1
        SumaS[0] += Spiny[i].Sx @ Spiny[i+1].Sx
        SumaS[1] += Spiny[i].Sy @ Spiny[i+1].Sy
        SumaS[2] += Spiny[i].Sz @ Spiny[i+1].Sz

    SumaSi = SumaS[0] + SumaS[1] + SumaS[2]
    SumaHz = np.zeros( (int( 2 * s + 1 ) ** n, int( 2 * s + 1 ) ** n ), dtype=complex )

    for i in range( len( Spiny ) ):
        SumaHz += Spiny[i].Sz
    return j * SumaSi - h * SumaHz

def hSklej( s, n, j, h, start, stop, ham ):
    Spin0 = S( s, start, n )
    SpinK = S( s, stop, n )
    return ham + j * ( Spin0.Sx @ SpinK.Sx + Spin0.Sy @ SpinK.Sy + Spin0.Sz @ SpinK.Sz )




    #print( np.sum( prod ) )
    #print(prod)

#def min_energy( H ):
#    w = sorted( np.linalg.eig(H))
#    return sorted( w )

def normalizacja( A ):
    return A / ( np.transpose( A ) * A ) ** .5

ham = H( .5, 3, 1, 1 )
hamtest = hSklej( .5, 3, 1, 1, 1, 3, H2( .5, 3, 1, 1, 1, 3 ) )#nie działa
print( ham )
print( "--------------" )
print( hamtest )
#print( ham )
#print( min_energy( ham ) )
#print( .Sz )
#print( S( .5, 1, 2 ).Sx )


    #return S()
#print(np.add(a,b))
#s1 = vec_spin(.5)
#s2 = vec_spin(.5)


#print(asdf.z)
#print( asdf.tensorProd( asdf.x, asdf.y ) )
#print(asdf.y)