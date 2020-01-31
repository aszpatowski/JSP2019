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
print(sx(0.5,2,3))
print(sy(0.5,2,3))
print(sz(0.5,2,3))
print(H(0.5,2,1,1))