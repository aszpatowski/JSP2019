import numpy as np

id =0
class vec_spin:
    def __init__(self, s):
        Vectorx = [0.5 * np.sqrt((a - 1) * (2 * s + 2 - a)) for a in range(2, int((2 * s) + 2))]
        Vectory = [0.5j * np.sqrt((a - 1) * (2 * s + 2 - a)) for a in range(2, int((2 * s) + 2))]
        Vectorz = [(-a+1+s) for a in range(1, int((2 * s + 2)))]
        self.x = np.diag(Vectorx, k=1) + np.diag(Vectorx, k=-1)
        self.y = (np.diag(Vectory, k=1) + np.diag(Vectory, k=-1))
        self.z = np.diag(Vectorz, k=0)


def ABCD(s, i, N):
    Spin = vec_spin(s)
    if( i == 1 ):
        Spin.Sx = np.kron( Spin.x, np.identity( int( s * 2 + 1 ) ** ( N - 1 ) ) )
        Spin.Sy = np.kron( Spin.y, np.identity( int( s * 2 + 1 ) ** ( N - 1 ) ) )
        Spin.Sz = np.kron( Spin.z, np.identity( int( s * 2 + 1 ) ** ( N - 1 ) ) )
    elif( i < N ):
        Spin.Sx = np.kron( np.kron( np.identity( int( s * 2 + 1 ) ** (i-1) ), Spin.x  ), np.identity( int(s * 2 + 1) ** (N - i) ) )
        Spin.Sy = np.kron( np.kron( np.identity( int( s * 2 + 1 ) ** (i-1) ), Spin.y  ), np.identity( int(s * 2 + 1) ** (N - i) ) )
        Spin.Sz = np.kron( np.kron( np.identity( int( s * 2 + 1 ) ** (i-1) ), Spin.z  ), np.identity( int(s * 2 + 1) ** (N - i) ) )
    else:
        Spin.Sx = np.kron( np.identity( int( s * 2 + 1 ) ** ( N - 1 ) ), Spin.x )
        Spin.Sy = np.kron( np.identity( int( s * 2 + 1 ) ** ( N - 1 ) ), Spin.y )
        Spin.Sz = np.kron( np.identity( int( s * 2 + 1 ) ** ( N - 1 ) ), Spin.z )
    return Spin


def Hamil(s, N, j, h):
    spiny = []
    wynik = [ np.zeros( (int( 2 * s + 1 ) ** N, int( 2 * s + 1 ) ** N ), dtype=complex) for i in range(3) ]

    for i in range(1, N+1):#range(1, n + 1):

        spiny.append(ABCD(s, i, N))

    for i in range (len(spiny)-1):

        wynik[0] += spiny[i].Sx @ spiny[i+1].Sx
        wynik[1] += spiny[i].Sy @ spiny[i+1].Sy
        wynik[2] += spiny[i].Sz @ spiny[i+1].Sz

    wynik[0] += spiny[0].Sx @ spiny[N-1].Sx
    wynik[1] += spiny[0].Sy @ spiny[N-1].Sy
    wynik[2] += spiny[0].Sz @ spiny[N-1].Sz

    ostateczny = wynik[0]+wynik[1]+wynik[2]
    Suma_H_Z = [np.zeros((int(2*s+1)**N, int(2*s+1)**N), dtype = complex) for i in range(3)]
    for i in range(0,N):
        Suma_H_Z +=spiny[i].Sz
    return j*ostateczny-h*Suma_H_Z
#def Klejenie(s,n,j,h,start,stop,ham):
 #   Spin0 = ABCD( s, start, n )
  #  SpinK = ABCD( s, stop, n )
   # return ham + j * ( Spin0.Sx @ SpinK.Sx + Spin0.Sy @ SpinK.Sy + Spin0.Sz @ SpinK.Sz )

#def MIN_energy(H): ## minimum energii punkt 2
 #   global id
  #  w,h = np.linalg.eig(H)
   # id = np.argsort(w)[0]
    #return h[id]
    #   ham3 = np.tensordot(H[0][0:100],np.identity(len(H[1])))
     #   G = np.linalg.eig(ham3)
      #  print(G)
#def normalizIt( A ):
 #   normalize = A / ( np.transpose( A ) * A ) ** .5
  #  return normalize
#def rho(v):
 #   ilosc = int((2*s+1)**5)
  #  rho =[]
   # for j in range(0,32):
    #    for iprim in range(0,32):
     #       for i in range(0,32):
      #          rho +=v[ilosc][i*2**5+j]*v[id][iprim*2**5+j]
    #return rho
N = 4
s = 0.5
j = 1
h = 1
print(Hamil(s,N,j,h))
# print(ABCD(s,1,N))
# Spin = vec_spin(s)
# print(Spin.x)
# print(Spin.y)
# print(Spin.z) ###np.conjugate - sprzezenie
# spins= ABCD(s,1,N)
# print(spins)
#print(Hamil(s, N, 1, 1,start,stop))
#print(Klejenie(s,N,j,h,start,stop,Hamil(s, N, 1, 1,start,stop)))
#Klejeto = Hamil(s, N, j, h,1,4) + Klejenie(s,N,j,h,5,6) 
#print(MIN_energy(Klejenie(s,N,j,h,start,stop,Hamil(s, N, 1, 1,start,stop))))
#print(rho(MIN_energy(Klejenie(s,N,j,h,start,stop,Hamil(s, N, 1, 1,start,stop)))))
