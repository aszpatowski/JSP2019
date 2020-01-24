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
        Spin = vec_spin(s)
        if i==1:
                Sx= np.kron(Spin.x, np.identity(int(s * 2 + 1) ** (N - 1)))
                Sy = np.kron(Spin.y, np.identity(int(s * 2 + 1) ** (N - 1)))
                Sz = np.kron(Spin.z, np.identity(int(s * 2 + 1) ** (N - 1)))
        elif (i<N):
                Sx = np.kron(np.kron(np.identity(int(s*2+1)**(i-1)), Spin.x), np.identity(int(s * 2 + 1) ** (N - 1)))
                Sy = np.kron(np.kron(np.identity(int(s * 2 + 1) ** (i - 1)), Spin.y), np.identity(int(s * 2 + 1) ** (N - 1)))
                Sz = np.kron(np.kron(np.identity(int(s * 2 + 1) ** (i - 1)), Spin.z), np.identity(int(s * 2 + 1) ** (N - 1)))
        else:
                Sx = np.kron(np.identity(int(s * 2 + 1) ** (N - 1)), Spin.x)
                Sy = np.kron(np.identity(int(s * 2 + 1) ** (N - 1)), Spin.y)
                Sz = np.kron(np.identity(int(s * 2 + 1) ** (N - 1)), Spin.z)
        #print("\n")
        #print(Sx,"\n\n")
        #print(Sy, "\n\n")
        #print(Sz, "\n\n")
        Spins = [Sx,Sy,Sz]
        return Spins
def Hamil(s,N,j,h):
        spiny=[]
        wynik = [np.zeros((int((2*s+1)**N), int((2*s+1)**N)), dtype = complex) for i in range(3)]
        for i in range(0,N+1):
                spiny.append(ABCD(s,1,N))
        for i in range (len(spiny)-1):
                wynik[0] += spiny[i].x @ spiny[i+1].x
                wynik[1] += spiny[i].y @ spiny[i+1].y
                wynik[2] += spiny[i].z @ spiny[i+1].z
        wynik[0] += spiny[N - 1].x @ spiny[0].x
        wynik[1] += spiny[N - 1].y @ spiny[0].y
        wynik[2] += spiny[N - 1].z @ spiny[0].z
        ostateczny = []
        for i in range(0,3):
                ostateczny = wynik[i]
        zmienna = np.zeros((int((s * 2 + 1) ** N),int( (s * 2 + 1) ** N)), dtype=complex)
        Suma_H_Z = []
        for i in range(N):
                Suma_H_Z +=spiny[i].z
        return (j*ostateczny)-(h*Suma_H_Z)
def MIN_energy(H): ## minimum energii punkt 2
        A = np.linalg.eig(Hamil(s,N,1,1))


N =3
s =0.5
print(ABCD(s,1,N))
#Spin = vec_spin(s)
##print(a1.x)
##print(a1.y)
##print(a1.z)
#spins= ABCD(s,1,N)
#print(spins)
#print(Hamil(s,N,1,1))
