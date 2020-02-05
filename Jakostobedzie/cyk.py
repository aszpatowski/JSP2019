import numpy as np
class vec_spin:
    def __init__(self,s):
        self.s = s
        self.x = np.diag([0.5 * np.sqrt((a - 1) * (2 * s + 2 - a)) for a in range(2, int((2 * s) + 2))], k=1) + np.diag([0.5 * np.sqrt((a - 1) * (2 * s + 2 - a)) for a in range(2, int((2 * s) + 2))], k=-1)
        self.y = np.diag([-0.5j * np.sqrt((a - 1) * (2 * s + 2 - a)) for a in range(2, int((2 * s) + 2))], k=1) + np.diag([0.5j * np.sqrt((a - 1) * (2 * s + 2 - a)) for a in range(2, int((2 * s) + 2))], k=-1)
        self.z = np.diagflat([s+1-a for a in range(1,int(2*s)+2)])
    def SpinX(self,i,n):
        din = 2 *self.s+1
        if i==1:
            return np.kron(vec_spin(self.s).x, np.identity(int((din) ** (n - i))))
        elif i == n:
            return np.kron(np.identity(int((din) ** (i - 1))),vec_spin(self.s).x)
        else:
            return np.kron(np.kron(np.identity(int((din) ** (i - 1))),vec_spin(self.s).x),np.identity(int((din) ** (n - i))))
    def SpinY(self,i,n):
        if i==1:
            return np.kron(vec_spin(self.s).y, np.identity(int((din) ** (n - i))))
        elif i == n:
            return np.kron(np.identity(int((din) ** (i - 1))),vec_spin(self.s).y)
        else:
            return np.kron(np.kron(np.identity(int((din) ** (i - 1))),vec_spin(self.s).y),np.identity(int((din) ** (n - i))))
    def SpinZ(self,i,n):
        if i==1:
            return np.kron(vec_spin(self.s).z, np.identity(int((din) ** (n - i))))
        elif i == n:
            return np.kron(np.identity(int((din) ** (i - 1))),vec_spin(self.s).z)
        else:
            return np.kron(np.kron(np.identity(int((din) ** (i - 1))),vec_spin(self.s).z),np.identity(int((din) ** (n - i))))
    def H(self,n,J,h):
        din = 2*self.s+ 1
        n = int(n)
        Hsx = np.zeros((int(din)**n, int(din)**n))
        Hsy = np.zeros((int(din)**n, int(din)**n),dtype=complex)
        Hsz = np.zeros((int(din)**n, int(din)**n))
        HZadd =np.zeros((int(din)**n, int(din)**n))
        for i in range(1,n):
            Hsx += np.dot(vec_spin(self.s).SpinX(i,n),vec_spin(self.s).SpinX(i+1,n))
        for i in range(1,n):
            Hsy += np.dot(vec_spin(self.s).SpinY(i,n),vec_spin(self.s).SpinY(i+1,n))
        for i in range(1,n):
            Hsz += np.dot(vec_spin(self.s).SpinZ(i,n),vec_spin(self.s).SpinZ(i+1,n))
        for i in range(1,n+1):
            HZadd+=vec_spin(self.s).SpinZ(i,n)
        return J*(Hsx+Hsy+Hsz)-h*HZadd
s = 0.5 #float(input("Podaj wartość spinu: "))
spin = vec_spin(s)
N = 10
nmini = int((int(N/2))-1)
potega = int(N-nmini)
J = 1
h = 0
din = int(2*s+1)
xnay = int((din)**int(int(N/2)))
tamto = int(((din**((N/2)-1))*2*s)-1)
count = 0
ile = 100
def min_energy(ham1,ham2):
    ham3 = np.kron(ham1, np.identity(int((din) ** potega))) + np.kron(np.identity(int((din) ** potega)), ham2) + np.dot(spin.SpinX(nmini,N),spin.SpinX(nmini+1,N)) + np.dot(spin.SpinX(nmini+1,N),spin.SpinX(nmini+2,N)) + np.dot(spin.SpinX(nmini+2,N), spin.SpinX(nmini+3,N)) - h*(spin.SpinZ(nmini+1,N) + spin.SpinX(nmini+2,N)) + np.dot(spin.SpinY(nmini,N),spin.SpinY(nmini+1,N)) + np.dot(spin.SpinY(nmini+1,N),spin.SpinY(nmini+2,N)) + np.dot(spin.SpinY(nmini+2,N), spin.SpinY(nmini+3,N)) + np.dot(spin.SpinZ(nmini,N), spin.SpinZ(nmini+1,N)) + np.dot(spin.SpinZ(nmini+1,N), spin.SpinZ(nmini+2,N)) + np.dot(spin.SpinZ(nmini+2,N),spin.SpinZ(nmini+3,N))
    w,v = np.linalg.eig(ham3)
    ind = np.argsort(np.real(w))[0]
    return (v[ :,ind],np.real(w[ind]))
def connectSystem(i1,i2):
    suma = 0.
    for j in range(xnay):
        suma +=L1[i1*xnay+j]*L2[i2*xnay+j]
    return suma
def connectEnviroment(i1,i2):
    suma = 0.
    for j in range(xnay):
        suma +=L1[j*xnay+i1]*L2[j*xnay+i2]
    return suma
x = spin.H(nmini,J,h)
y = spin.H(nmini,J,h)
ListX = [x]
listY = [y]
plik = open("resultsS{}N{}J{}H{}.txt".format(s,N,J,h),"w")
plik.write("s = "+ str(s) + "\n")
plik.write("N = "+ str(N) + "\n")
plik.write("J = "+ str(J) + "\n")
plik.write("h = "+ str(h) + "\n\n")
for i in range(ile):
    temp = min_energy(x,y)
    L1 = temp[0]
    L2 = np.conjugate(L1)
    ham4 = np.kron(x,np.identity(int(din))) + np.dot(spin.SpinX(nmini,int(N/2)),spin.SpinX(nmini+1,int(N/2))) + np.dot(spin.SpinY(nmini,int(N/2)),spin.SpinY(nmini+1,int(N/2))) + np.dot(spin.SpinZ(nmini,int(N/2)),spin.SpinZ(nmini+1,int(N/2)))
    matrixy = np.zeros((xnay,xnay),dtype=complex)
    for i1 in range(xnay):
        for i2 in range(xnay):
            matrixy[i1][i2]=connectSystem(i1,i2)
    firstside,secondside = np.linalg.eig(matrixy)
    ind = np.argsort(np.real(firstside))[:tamto:-1] #może byc źle (15)
    T = np.array([secondside[:,k]for k in ind]).T
    T2 =np.conjugate(T.T)
    x = np.matmul(np.matmul(T2,ham4),T)
    ListX.append(x)
    ham4 = np.kron(np.identity(int((din))),y) + np.dot(spin.SpinX(1,int(N/2)),spin.SpinX(2,int(N/2))) + np.dot(spin.SpinY(1,int(N/2)),spin.SpinY(2,int(N/2))) + np.dot(spin.SpinZ(1,int(N/2)),spin.SpinZ(2,int(N/2)))
    matrixy = np.zeros((xnay,xnay),dtype=complex)
    for i1 in range(xnay):
        for i2 in range(xnay):
            matrixy[i1][i2]=connectEnviroment(i1,i2)
    firstside, secondside = np.linalg.eig(matrixy)
    ind = np.argsort(np.real(firstside))[:tamto:-1] # moze być źle (15)
    T = np.array([secondside[:,k]for k in ind]).T
    T2 =np.conjugate(T.T)
    y = np.matmul(np.matmul(T2,ham4),T)
    listY.append(y)
    plik.write(str(i+1)+". "+str(temp[1]/(N+(2*i)))+"\n")
    plik.flush()
plik.write("BRRRRUSH...\n\n")
dane = open("daneS{}N{}J{}H{}.txt".format(s,N,J,h),"w")
#Zaczynamy zamiatanie
while count<1000:
    count+=1
    plik.write("\n"+str(count)+"\n")
    for i in range(ile):
        temp = min_energy(x,y)
        L1 = temp[0]
        L2 = np.conjugate(L1)
        ham4 = np.kron(x,np.identity(int(din))) + np.dot(spin.SpinX(nmini,int(N/2)),spin.SpinX(nmini+1,int(N/2))) + np.dot(spin.SpinY(nmini,int(N/2)),spin.SpinY(nmini+1,int(N/2))) + np.dot(spin.SpinZ(nmini,int(N/2)),spin.SpinZ(nmini+1,int(N/2)))
        matrixy = np.zeros((xnay,xnay),dtype=complex)
        for i1 in range(xnay):
            for i2 in range(xnay):
                matrixy[i1][i2]=connectSystem(i1,i2)
        firstside,secondside = np.linalg.eig(matrixy)
        ind = np.argsort(np.real(firstside))[:tamto:-1] #może byc źle (15)
        T = np.array([secondside[:,k]for k in ind]).T
        T2 =np.conjugate(T.T)
        x = np.matmul(np.matmul(T2,ham4),T)
        ListX.append(x)
        y = listY[ile-i-1]
        plik.write(str(i+1)+". "+str(temp[1]/(N+(2*(ile-1))))+"\n")
        plik.flush()
    listY = [y]
    for i in range(2*ile):
        temp = min_energy(x,y)
        L1 = temp[0]
        L2 = np.conjugate(L1)
        x = ListX[2*ile-i-1]
        ham4 = np.kron(np.identity(int((din))),y) + np.dot(spin.SpinX(1,int(N/2)),spin.SpinX(2,int(N/2))) + np.dot(spin.SpinY(1,int(N/2)),spin.SpinY(2,int(N/2))) + np.dot(spin.SpinZ(1,int(N/2)),spin.SpinZ(2,int(N/2)))
        matrixy = np.zeros((xnay,xnay),dtype=complex)
        for i1 in range(xnay):
            for i2 in range(xnay):
                matrixy[i1][i2]=connectEnviroment(i1,i2)
        firstside, secondside = np.linalg.eig(matrixy)
        ind = np.argsort(np.real(firstside))[:tamto:-1] # moze być źle (15)
        T = np.array([secondside[:,k]for k in ind]).T
        T2 =np.conjugate(T.T)
        y = np.matmul(np.matmul(T2,ham4),T)
        listY.append(y)
        plik.write(str(i+1)+". "+str(temp[1]/(N+(2*(ile-1))))+"\n")
        plik.flush()
    ListX = [x]
    for i in range(ile):
        temp = min_energy(x,y)
        L1 = temp[0]
        L2 = np.conjugate(L1)
        ham4 = np.kron(x,np.identity(int(din))) + np.dot(spin.SpinX(nmini,int(N/2)),spin.SpinX(nmini+1,int(N/2))) + np.dot(spin.SpinY(nmini,int(N/2)),spin.SpinY(nmini+1,int(N/2))) + np.dot(spin.SpinZ(nmini,int(N/2)),spin.SpinZ(nmini+1,int(N/2)))
        matrixy = np.zeros((xnay,xnay),dtype=complex)
        for i1 in range(xnay):
            for i2 in range(xnay):
                matrixy[i1][i2]=connectSystem(i1,i2)
        firstside,secondside = np.linalg.eig(matrixy)
        ind = np.argsort(np.real(firstside))[:tamto:-1] #może byc źle (15)
        T = np.array([secondside[:,k]for k in ind]).T
        T2 =np.conjugate(T.T)
        x = np.matmul(np.matmul(T2,ham4),T)
        ListX.append(x)
        y = listY[2*ile-i-1]
        plik.write(str(i+1)+". "+str(temp[1]/(N+(2*(ile-1))))+"\n")
        plik.flush()
    plik.write("MAIN "+str(count)+". "+str(temp[1]/(N+(2*(ile-1))))+"\n")
    plik.flush()
    dane.write(str(temp[1]/(N+(2*(ile-1))))+"\n")
    dane.flush()
    listY = listY[0:ile]
plik.close()


     
