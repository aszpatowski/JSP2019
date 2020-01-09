import numpy as np
class vec_spin:
    def __init__(self,s):
            Vectorx =[0.5* np.sqrt((a - 1) * (2 *s + 2 - a))for a in range(2, int((2 * s) + 2))]
            Vectory = [0.5j * np.sqrt((a - 1) * (2 * s + 2 - a))for a in range(2, int((2 * s) + 2))]
            Vectorz = [(s+1 -a) for a in range(1, int((2 * s)+2))]
            self.x =np.diag(Vectorx,k=1)+np.diag(Vectorx,k=-1)
            self.y = (np.diag(Vectory, k=1) - np.diag(Vectory, k=-1))*-1
            self.z = np.diag(Vectorz, k=0)
def ABCD(s,i,N):
        if i==1:
                Sx= np.kron(a1.x,np.identity(int(s*2+1)**(N-1)))
                Sy = np.kron(a1.y, np.identity(int(s * 2 + 1) ** (N - 1)))
                Sz = np.kron(a1.z, np.identity(int(s * 2 + 1) ** (N - 1)))
        elif (i<N):
                Sx = np.kron(np.kron(np.identity(int(s*2+1)**(i-1)),a1.x),np.identity(int(s*2+1)**(N-1)))
                Sy = np.kron(np.kron(np.identity(int(s * 2 + 1) ** (i - 1)), a1.y),np.identity(int(s * 2 + 1) ** (N - 1)))
                Sz = np.kron(np.kron(np.identity(int(s * 2 + 1) ** (i - 1)), a1.z),np.identity(int(s * 2 + 1) ** (N - 1)))
        else:
                Sx = np.kron( np.identity(int(s * 2 + 1) ** (N - 1)),a1.x)
                Sy = np.kron(np.identity(int(s * 2 + 1) ** (N - 1)), a1.y)
                Sz = np.kron(np.identity(int(s * 2 + 1) ** (N - 1)), a1.z)
        #print("\n")
        #print(Sx,"\n\n")
        #print(Sy, "\n\n")
        #print(Sz, "\n\n")
        return Sz
N =3
s =0.5
a1 = vec_spin(s)
print(a1.x)
print(a1.y)
print(a1.z)
spins = []
#zera = [np.zeros(int(s*2+1)**N,int(s*2+1)**N) for i in range]
     #   ABCD(s,2,N)
spins= ABCD(s,1,N) @ ABCD(s,1,N)
print(spins)



#s =5
#rozmiar= 10
#Sx =[]
#for a in range(2,2*s+2):
 #   Sx.append([0.5*np.sqrt((a-1)*(2*(s+1)-a))])
#print(Sx)