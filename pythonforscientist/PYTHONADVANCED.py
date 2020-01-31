import numpy as np
ham3 = 0
class spin:
    def __init__(self,s):

        diag_x=[0.5 * (np.sqrt((s + 1) * (2 * a - 2) - (a ** 2 - a))) for a in range(2,int(2*s)+2)]
        diag_y=[0.5 * (np.sqrt((s + 1) * (2 * a - 2) - (a ** 2 - a))) for a in range(2,int(2*s)+2)]
        diag_z=[s+1-a for a in range(1,int(2*s)+2)]

        self.x=np.diagflat([diag_x], 1) + np.diagflat([diag_x], -1)
        self.y=-1j*np.diagflat([diag_y], 1) + 1j*np.diagflat([diag_y], -1)
        self.z=np.diagflat([diag_z])

def sz(s,i,n):
    if i==1:
        return np.kron(spin(s).z, np.identity(int((2 * s + 1) ** (n - i))))
    elif i == n:
        return np.kron(np.identity(int((2 * s + 1) ** (i - 1))),spin(s).z)
    else:
        x = np.kron(np.identity(int((2 * s + 1) ** (i - 1))),spin(s).z)
        x = np.kron(x,np.identity(int((2 * s + 1) ** (n - i))))
        return x
def sx(s,i,n):
    if i==1:
        return np.kron(spin(s).x, np.identity(int((2 * s + 1) ** (n - i))))
    elif i == n:
        return np.kron(np.identity(int((2 * s + 1) ** (i - 1))),spin(s).x)
    else:
        x = np.kron(np.identity(int((2 * s + 1) ** (i - 1))),spin(s).x)
        x = np.kron(x,np.identity(int((2 * s + 1) ** (n - i))))
        return x
def sy(s,i,n):
    if i==1:
        return np.kron(spin(s).y, np.identity(int((2 * s + 1) ** (n - i))))
    elif i == n:
        return np.kron(np.identity(int((2 * s + 1) ** (i - 1))),spin(s).y)
    else:
        x = np.kron(np.identity(int((2 * s + 1) ** (i - 1))),spin(s).y)
        x = np.kron(x,np.identity(int((2 * s + 1) ** (n - i))))
        return x
def H(s,n,J,h):
    hx = np.zeros((2**n, 2**n))
    hy = np.zeros((2**n, 2**n),dtype=complex)
    hz = np.zeros((2**n, 2**n))
    hzz =np.zeros((2**n,2**n))
    for i in range(1,n):
        hx += np.dot(sx(s,i,n),sx(s,i+1,n))
    for i in range(1,n):
        hy += np.dot(sy(s,i,n),sy(s,i+1,n))
    for i in range(1,n):
        hz += np.dot(sz(s,i,n),sz(s,i+1,n))
    for i in range(1,n+1):
        hzz+=sz(s,i,n)
    # hz += np.dot(sz(s,1,n),sz(s,n,n))
    # hx += np.dot(sx(s, 1, n), sx(s, n, n))
    # hy += np.dot(sy(s, 1, n), sy(s, n, n))
    return J*(hx+hy+hz)-h*hzz

def min_energy(ham1,ham2):
    global ham3
    ham3 = np.kron(ham1, np.identity(int((2 * 0.5 + 1) ** 6))) + np.kron(np.identity(int((2 * 0.5 + 1) ** 6)), ham2) + np.dot(sx(0.5,4,10),sx(0.5,5,10)) + np.dot(sx(0.5,5,10),sx(0.5,6,10)) + np.dot(sx(0.5, 6, 10), sx(0.5, 7, 10)) - 0*(sz(0.5,5,10) + sz(0.5,6,10)) + np.dot(sy(0.5,4,10),sy(0.5,5,10)) + np.dot(sy(0.5,5,10),sy(0.5,6,10)) + np.dot(sy(0.5, 6, 10), sy(0.5, 7, 10)) + \
np.dot(sz(0.5, 4, 10), sz(0.5, 5, 10)) + np.dot(sz(0.5, 5, 10), sz(0.5, 6, 10)) + np.dot(sz(0.5, 6, 10), sz(0.5, 7, 10))
    w,v = np.linalg.eig(ham3)
    ind = np.argsort(np.real(w))[0]
    return (v[ :, ind],np.real(w[ind]))
def laczenieS(i1, i2):
    suma=0.
    for j in range(32):
        suma += L1[i1*32+j]*L2[i2*32+j]
    return suma
def laczenieE(i1, i2):
    suma=0.
    for j in range(32):
        suma += L1[j*32+i1]*L2[j*32+i2]
    return suma
x = H(0.5,4,1,0)
y = H(0.5,4,1,0)
#print(x)
tak = H(0.5,4,1,1)
print(tak)
for i in range(50):
    temp = min_energy(x,y)
    L1 = temp[0]
    L2 = np.conjugate(L1)
    ham4 = np.kron(x, np.identity(int((2 * 0.5 + 1) ** 1))) + np.dot(sx(0.5,4,5),sx(0.5,5,5)) + np.dot(sy(0.5,4,5),sy(0.5,5,5)) + np.dot(sz(0.5, 4, 5), sz(0.5, 5, 5))
    macierz = np.zeros((32, 32), dtype=complex)
    for i1 in range(32):
        for i2 in range(32):
            macierz[i1][i2] = laczenieS(i1,i2)
    wm, vm = np.linalg.eig(macierz)
    ind = np.argsort(np.real(wm))[:15:-1]
    print(ind)
    T = np.transpose(np.array([vm[:, k] for k in ind]))
    T2 = np.conjugate(np.transpose(T))
    x = np.matmul(np.matmul(T2,ham4),T)
    ham4 = np.kron(np.identity(int((2 * 0.5 + 1) ** 1)), y) + np.dot(sx(0.5, 1, 5), sx(0.5, 2, 5)) + np.dot(sy(0.5, 1, 5), sy(0.5, 2, 5)) + np.dot(sz(0.5, 1, 5), sz(0.5, 2, 5))
    macierz = np.zeros((32, 32), dtype=complex)
    for i1 in range(32):
        for i2 in range(32):
            macierz[i1][i2] = laczenieE(i1, i2)
    wm, vm = np.linalg.eig(macierz)
    ind = np.argsort(np.real(wm))[:15:-1]
    T = np.transpose(np.array([vm[:, k] for k in ind]))
    T2 = np.conjugate(np.transpose(T))
    y = np.matmul(np.matmul(T2,ham4),T)
    print(temp[1]/(10+2*i))

min_energy(x,y)
#https://journals.aps.org/prl/pdf/10.1103/PhysRevLett.61.463
