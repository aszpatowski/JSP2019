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
