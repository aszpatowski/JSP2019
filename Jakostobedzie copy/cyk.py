import numpy as np
ham3=[]
class vec_spin:
    def __init__(self,s):
        self.s = s
        self.x = np.diag([0.5 * np.sqrt((a - 1) * (2 * s + 2 - a)) for a in range(2, int((2 * s) + 2))], k=1) + np.diag([0.5 * np.sqrt((a - 1) * (2 * s + 2 - a)) for a in range(2, int((2 * s) + 2))], k=-1)
        self.y = np.diag([-0.5j * np.sqrt((a - 1) * (2 * s + 2 - a)) for a in range(2, int((2 * s) + 2))], k=1) + np.diag([0.5j * np.sqrt((a - 1) * (2 * s + 2 - a)) for a in range(2, int((2 * s) + 2))], k=-1)
        self.z = np.diagflat([s+1-a for a in range(1,int(2*s)+2)])
    def SpinX(self,i,n):
        if i==1:
            return np.kron(vec_spin(self.s).x, np.identity(int((2 *self.s+ 1) ** (n - i))))
        elif i == n:
            return np.kron(np.identity(int((2 *self.s+ 1) ** (i - 1))),vec_spin(self.s).x)
        else:
            return np.kron(np.kron(np.identity(int((2 *self.s+ 1) ** (i - 1))),vec_spin(self.s).x),np.identity(int((2 *self.s+ 1) ** (n - i))))
    def SpinY(self,i,n):
        if i==1:
            return np.kron(vec_spin(self.s).y, np.identity(int((2 *self.s+ 1) ** (n - i))))
        elif i == n:
            return np.kron(np.identity(int((2 *self.s+ 1) ** (i - 1))),vec_spin(self.s).y)
        else:
            return np.kron(np.kron(np.identity(int((2 *self.s+ 1) ** (i - 1))),vec_spin(self.s).y),np.identity(int((2 *self.s+ 1) ** (n - i))))
    def SpinZ(self,i,n):
        if i==1:
            return np.kron(vec_spin(self.s).z, np.identity(int((2 *self.s+ 1) ** (n - i))))
        elif i == n:
            return np.kron(np.identity(int((2 *self.s+ 1) ** (i - 1))),vec_spin(self.s).z)
        else:
            return np.kron(np.kron(np.identity(int((2 *self.s+ 1) ** (i - 1))),vec_spin(self.s).z),np.identity(int((2 *self.s+ 1) ** (n - i))))
    def H(self,n,J,h):
        n = int(n)
        hx = np.zeros((int(2*self.s+1)**n, int(2*self.s+1)**n))
        hy = np.zeros((int(2*self.s+1)**n, int(2*self.s+1)**n),dtype=complex)
        hz = np.zeros((int(2*self.s+1)**n, int(2*self.s+1)**n))
        hzz =np.zeros((int(2*self.s+1)**n, int(2*self.s+1)**n))
        for i in range(1,n):
            hx += np.dot(vec_spin(self.s).SpinX(i,n),vec_spin(self.s).SpinX(i+1,n))
        for i in range(1,n):
            hy += np.dot(vec_spin(self.s).SpinY(i,n),vec_spin(self.s).SpinY(i+1,n))
        for i in range(1,n):
            hz += np.dot(vec_spin(self.s).SpinZ(i,n),vec_spin(self.s).SpinZ(i+1,n))
        for i in range(1,n+1):
            hzz+=vec_spin(self.s).SpinZ(i,n)
        return J*(hx+hy+hz)-h*hzz
s = 0.5 #float(input("Podaj wartość spinu: "))
spin = vec_spin(s)
N = 10
nmini = int((int(N/2))-1)
potega = int(N-nmini)
J = 1
h = 0
xnay = int((2*s+1)**int(int(N/2)))
print(spin.H(2,1,1))
def min_energy(ham1,ham2):
    global ham3
 #   ham3 = np.kron(ham1,np.identity((int(2*s+1)**potega))) + np.kron(np.identity((int(2*s+1)**potega)),ham2) +\
  #  np.dot(spin.SpinX(nmini,N),spin.SpinX(nmini+1,N)) + np.dot(spin.SpinX(nmini+1,N),spin.SpinX(nmini+2,N))+\
   # np.dot(spin.SpinX(nmini+2,N),spin.SpinX(nmini+3,N)) - h*(spin.SpinZ(nmini+1,N),spin.SpinZ(nmini+2,N)) +\
  #  np.dot(spin.SpinY(nmini,N),spin.SpinY(nmini+1,N)) + np.dot(spin.SpinY(nmini+1,N),spin.SpinY(nmini+2,N)) +\
  #  np.dot(spin.SpinY(nmini+2,N),spin.SpinY(nmini+3,N)) + np.dot(spin.SpinZ(nmini,N),spin.SpinZ(nmini+1,N)) +\
  #  np.dot(spin.SpinZ(nmini+1,N),spin.SpinZ(nmini+2,N)) + np.dot(spin.SpinZ(nmini+2,N),spin.SpinZ(nmini+3,N))
    ham3 = np.kron(ham1, np.identity(int((2 * s + 1) ** potega))) + np.kron(np.identity(int((2 * s + 1) ** potega)), ham2) + np.dot(spin.SpinX(nmini,N),spin.SpinX(nmini+1,N)) + np.dot(spin.SpinX(nmini+1,N),spin.SpinX(nmini+2,N)) + np.dot(spin.SpinX(nmini+2,N), spin.SpinX(nmini+3,N)) - 0*(spin.SpinZ(nmini+1,N) + spin.SpinX(nmini+2,N)) + np.dot(spin.SpinY(nmini,N),spin.SpinY(nmini+1,N)) + np.dot(spin.SpinY(nmini+1,N),spin.SpinY(nmini+2,N)) + np.dot(spin.SpinY(nmini+2,N), spin.SpinY(nmini+3,N)) + np.dot(spin.SpinZ(nmini,N), spin.SpinZ(nmini+1,N)) + np.dot(spin.SpinZ(nmini+1,N), spin.SpinZ(nmini+2,N)) + np.dot(spin.SpinZ(nmini+2,N),spin.SpinZ(nmini+3,N))
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
for i in range(50):
    temp = min_energy(x,y)
    L1 = temp[0]
    L2 = np.conjugate(L1)
    ham4 = np.kron(x,np.identity(int((2*s+1)))) + np.dot(spin.SpinX(nmini,int(N/2)),spin.SpinX(nmini+1,int(N/2))) + np.dot(spin.SpinY(nmini,int(N/2)),spin.SpinY(nmini+1,int(N/2))) + np.dot(spin.SpinZ(nmini,int(N/2)),spin.SpinZ(nmini+1,int(N/2)))
    matrixy = np.zeros((xnay,xnay),dtype=complex)
    for i1 in range(xnay):
        for i2 in range(xnay):
            matrixy[i1][i2]=connectSystem(i1,i2)
    wm,vm = np.linalg.eig(matrixy)
    ind = np.argsort(np.real(wm))[:int((N/2)-1):-1] #może byc źle (15)
    print(ind)
    T = np.transpose(np.array([vm[:,k]for k in ind]))
    T2 =np.conjugate(np.transpose(T))
    x = np.matmul(np.matmul(T2,ham4),T)
    ham4 = np.kron(np.identity(int((2*s+1))),y) + np.dot(spin.SpinX(1,int(N/2)),spin.SpinX(2,int(N/2))) + np.dot(spin.SpinY(1,int(N/2)),spin.SpinY(2,int(N/2))) + np.dot(spin.SpinZ(1,int(N/2)),spin.SpinZ(2,int(N/2)))
    matrixy = np.zeros((xnay,xnay),dtype=complex)
    for i1 in range(xnay):
        for i2 in range(xnay):
            matrixy[i1][i2]=connectEnviroment(i1,i2)
    wm, vm = np.linalg.eig(matrixy)
    ind = np.argsort(np.real(wm))[:int((N/2)-1):-1] # moze być źle
    T = np.transpose(np.array([vm[:,k]for k in ind]))
    T2 =np.conjugate(np.transpose(T))
    y = np.matmul(np.matmul(T2,ham4),T)
    
    print(temp[1]/(N+((2*s+1)*i)))

min_energy(x,y)

     
