import numpy as np

ham5 = 0
ham3 = 0
spin1 = 0.5
n1 = 10
petla = 10

class spin:
    def __init__(self, s):
        diag_x = [0.5 * (np.sqrt((s + 1) * (2 * a - 2) - (a ** 2 - a))) for a in range(2, int(2 * s) + 2)]
        diag_y = [0.5 * (np.sqrt((s + 1) * (2 * a - 2) - (a ** 2 - a))) for a in range(2, int(2 * s) + 2)]
        diag_z = [s + 1 - a for a in range(1, int(2 * s) + 2)]

        self.x = np.diagflat([diag_x], 1) + np.diagflat([diag_x], -1)
        self.y = -1j * np.diagflat([diag_y], 1) + 1j * np.diagflat([diag_y], -1)
        self.z = np.diagflat([diag_z])


def sz(s, i, n):
    if i == 1:
        return np.kron(spin(s).z, np.identity(int((2 * s + 1) ** (n - i))))
    elif i == n:
        return np.kron(np.identity(int((2 * s + 1) ** (i - 1))), spin(s).z)
    else:
        x = np.kron(np.identity(int((2 * s + 1) ** (i - 1))), spin(s).z)
        x = np.kron(x, np.identity(int((2 * s + 1) ** (n - i))))
        return x


def sx(s, i, n):
    if i == 1:
        return np.kron(spin(s).x, np.identity(int((2 * s + 1) ** (n - i))))
    elif i == n:
        return np.kron(np.identity(int((2 * s + 1) ** (i - 1))), spin(s).x)
    else:
        x = np.kron(np.identity(int((2 * s + 1) ** (i - 1))), spin(s).x)
        x = np.kron(x, np.identity(int((2 * s + 1) ** (n - i))))
        return x


def sy(s, i, n):
    if i == 1:
        return np.kron(spin(s).y, np.identity(int((2 * s + 1) ** (n - i))))
    elif i == n:
        return np.kron(np.identity(int((2 * s + 1) ** (i - 1))), spin(s).y)
    else:
        x = np.kron(np.identity(int((2 * s + 1) ** (i - 1))), spin(s).y)
        x = np.kron(x, np.identity(int((2 * s + 1) ** (n - i))))
        return x


def H(s, n, J, h):
    hx = np.zeros((int((2 * s + 1) ** n), int((2 * s + 1) ** n)))
    hy = np.zeros((int((2 * s + 1) ** n), int((2 * s + 1) ** n)), dtype=complex)
    hz = np.zeros((int((2 * s + 1) ** n), int((2 * s + 1) ** n)))
    hzz = np.zeros((int((2 * s + 1) ** n), int((2 * s + 1) ** n)))
    for i in range(1, n):
        hx += np.dot(sx(s, i, n), sx(s, i + 1, n))
    for i in range(1, n):
        hy += np.dot(sy(s, i, n), sy(s, i + 1, n))
    for i in range(1, n):
        hz += np.dot(sz(s, i, n), sz(s, i + 1, n))
    for i in range(1, n + 1):
        hzz += sz(s, i, n)
    # hz += np.dot(sz(s,1,n),sz(s,n,n))
    # hx += np.dot(sx(s, 1, n), sx(s, n, n))
    # hy += np.dot(sy(s, 1, n), sy(s, n, n))
    return J * (hx + hy + hz) - h * hzz


def min_energy(ham1, ham2, spin1, n1):
    global ham3
    ham3 = np.kron(ham1, np.identity(int((2 * spin1 + 1) ** ((n1/2)+1)))) + np.kron(np.identity(int((2 * spin1 + 1) ** ((n1/2)+1))), ham2) + np.dot(sx(spin1, ((n1/2)-1), n1), sx(spin1, ((n1/2)), n1)) + \
           np.dot(sx(spin1, ((n1/2)), n1), sx(spin1, ((n1/2)+1), n1)) + np.dot(sx(spin1, ((n1/2)+1), n1), sx(spin1, ((n1/2)+2), n1)) - 0 * (sz(spin1, ((n1/2)), n1) + sz(spin1, ((n1/2)+1), n1)) + np.dot(sy(spin1, ((n1/2)-1), n1), sy(spin1, ((n1/2)), n1)) + \
           np.dot(sy(spin1, ((n1/2)), n1), sy(spin1, ((n1/2)+1), n1)) + np.dot(sy(spin1, ((n1/2)+1), n1), sy(spin1, ((n1/2)+2), n1)) + np.dot(sz(spin1, ((n1/2)-1), n1), sz(spin1, ((n1/2)), n1)) + np.dot(sz(spin1, ((n1/2)), n1), sz(spin1, ((n1/2)+1), n1)) + \
           np.dot(sz(spin1, ((n1/2)+1), n1), sz(spin1, ((n1/2)+2), n1))
    w, v = np.linalg.eig(ham3)
    ind = np.argsort(np.real(w))[0]
    return (v[:, ind], np.real(w[ind]))


def laczenieS(i1, i2, spin1, n1):
    suma = 0.
    for j in range(int((2 * spin1 + 1)**((n1/2)))):
        suma += L1[i1 * int((2 * spin1 + 1)**((n1/2))) + j] * L2[i2 * int((2 * spin1 + 1)**((n1/2))) + j]
    return suma


def laczenieE(i1, i2, spin1, n1):
    suma = 0.
    for j in range(int((2 * spin1 + 1)**((n1/2)))):
        suma += L1[j * int((2 * spin1 + 1)**((n1/2))) + i1] * L2[j * int((2 * spin1 + 1)**((n1/2))) + i2]
    return suma


x = H(spin1, int((n1/2)-1), 1, 0)
y = H(spin1, int((n1/2)-1), 1, 0)
tabx = [x]
taby = [y]
for i in range(petla):
    temp = min_energy(x, y, spin1, n1)
    L1 = temp[0]
    L2 = np.conjugate(L1)
    ham4 = np.kron(x, np.identity(int((2 * spin1 + 1) ** 1))) + np.dot(sx(spin1, ((n1/2)-1), ((n1/2))), sx(spin1, ((n1/2)), ((n1/2)))) + np.dot(
        sy(spin1, ((n1/2)-1), ((n1/2))), sy(spin1, ((n1/2)), ((n1/2)))) + np.dot(sz(spin1, ((n1/2)-1), ((n1/2))), sz(spin1, ((n1/2)), ((n1/2))))
    macierz = np.zeros((int((2 * spin1 + 1) ** ((n1/2))), int((2 * spin1 + 1) ** ((n1/2)))), dtype=complex)
    for i1 in range(int((2 * spin1 + 1) ** ((n1/2)))):
        for i2 in range(int((2 * spin1 + 1) ** ((n1/2)))):
            macierz[i1][i2] = laczenieS(i1, i2, spin1, n1)
    wm, vm = np.linalg.eig(macierz)
    ind = np.argsort(np.real(wm))[:int(2*spin1*(2 * spin1 + 1) ** ((n1/2)-1))-1:-1]
    T = np.transpose(np.array([vm[:, k] for k in ind]))
    T2 = np.conjugate(np.transpose(T))
    x = np.matmul(np.matmul(T2, ham4), T)
    tabx.append(x)
    ham4 = np.kron(np.identity(int((2 * spin1 + 1) ** 1)), y) + np.dot(sx(spin1, 1, ((n1/2))), sx(spin1, 2, ((n1/2)))) + np.dot(
            sy(spin1, 1, ((n1/2))), sy(spin1, 2, ((n1/2)))) + np.dot(sz(spin1, 1, ((n1/2))), sz(spin1, 2, ((n1/2))))
    macierz = np.zeros((int((2 * spin1 + 1) ** ((n1/2))), int((2 * spin1 + 1) ** ((n1/2)))), dtype=complex)
    for i1 in range(int((2 * spin1 + 1) ** ((n1/2)))):
        for i2 in range(int((2 * spin1 + 1) ** ((n1/2)))):
            macierz[i1][i2] = laczenieE(i1, i2, spin1, n1)
    wm, vm = np.linalg.eig(macierz)
    ind = np.argsort(np.real(wm))[:int(2*spin1*(2 * spin1 + 1) ** ((n1/2)-1))-1:-1]
    T = np.transpose(np.array([vm[:, k] for k in ind]))
    T2 = np.conjugate(np.transpose(T))
    y = np.matmul(np.matmul(T2, ham4), T)
    taby.append(y)
    plik = open('plik222n', 'a')
    plik.write(" "+str(temp[1] / (n1 + 2 * i)))
    plik.close()
    plik = open('plik333n', 'a')
    plik.write(" " + str((n1 + 2 * i)))
    plik.close()
    print(temp[1] / (n1 + 2 * i))
print("przemiatanie")
z = 0
if __name__ == '__main__':
    while z < 20:
        print(z)
        z += 1
        for i in range(petla):
            temp = min_energy(x, y, spin1, n1)
            L1 = temp[0]
            L2 = np.conjugate(L1)
            ham4 = np.kron(x, np.identity(int((2 * spin1 + 1) ** 1))) + np.dot(sx(spin1, ((n1 / 2) - 1), (n1 / 2)),
                                                                               sx(spin1, (n1 / 2), (n1 / 2))) + np.dot(
                sy(spin1, ((n1 / 2) - 1), (n1 / 2)), sy(spin1, (n1 / 2), (n1 / 2))) + np.dot(
                sz(spin1, ((n1 / 2) - 1), (n1 / 2)), sz(spin1, (n1 / 2), (n1 / 2)))
            macierz = np.zeros((int((2 * spin1 + 1) ** ((n1 / 2))), int((2 * spin1 + 1) ** ((n1 / 2)))), dtype=complex)
            for i1 in range(int((2 * spin1 + 1) ** ((n1 / 2)))):
                for i2 in range(int((2 * spin1 + 1) ** ((n1 / 2)))):
                    macierz[i1][i2] = laczenieS(i1, i2, spin1, n1)
            wm, vm = np.linalg.eig(macierz)
            ind = np.argsort(np.real(wm))[:int(2 * spin1 * (2 * spin1 + 1) ** ((n1 / 2) - 1)) - 1:-1]
            T = np.transpose(np.array([vm[:, k] for k in ind]))
            T2 = np.conjugate(np.transpose(T))
            x = np.matmul(np.matmul(T2, ham4), T)
            tabx.append(x)
            y = taby[petla-i-1]
            print(temp[1] / (n1 + 2 * (petla - 1)))
        taby = [y]
        for i in range(2*petla):
            temp = min_energy(x, y, spin1, n1)
            L1 = temp[0]
            L2 = np.conjugate(L1)
            x = tabx[2*petla-i-1]
            ham4 = np.kron(np.identity(int((2 * spin1 + 1) ** 1)), y) + np.dot(sx(spin1, 1, ((n1 / 2))),
                                                                               sx(spin1, 2, ((n1 / 2)))) + np.dot(
                sy(spin1, 1, ((n1 / 2))), sy(spin1, 2, ((n1 / 2)))) + np.dot(sz(spin1, 1, ((n1 / 2))), sz(spin1, 2, ((n1 / 2))))
            macierz = np.zeros((int((2 * spin1 + 1) ** ((n1 / 2))), int((2 * spin1 + 1) ** ((n1 / 2)))), dtype=complex)
            for i1 in range(int((2 * spin1 + 1) ** ((n1 / 2)))):
                for i2 in range(int((2 * spin1 + 1) ** ((n1 / 2)))):
                    macierz[i1][i2] = laczenieE(i1, i2, spin1, n1)
            wm, vm = np.linalg.eig(macierz)
            ind = np.argsort(np.real(wm))[:int(2 * spin1 * (2 * spin1 + 1) ** ((n1 / 2) - 1)) - 1:-1]
            T = np.transpose(np.array([vm[:, k] for k in ind]))
            T2 = np.conjugate(np.transpose(T))
            y = np.matmul(np.matmul(T2, ham4), T)
            taby.append(y)
            print(temp[1] / (n1 + 2 * (petla - 1)))
        tabx = [x]
        for i in range(petla):
            temp = min_energy(x, y, spin1, n1)
            L1 = temp[0]
            L2 = np.conjugate(L1)
            ham4 = np.kron(x, np.identity(int((2 * spin1 + 1) ** 1))) + np.dot(sx(spin1, ((n1 / 2) - 1), ((n1 / 2))),
                                                                               sx(spin1, ((n1 / 2)), ((n1 / 2)))) + np.dot(
                sy(spin1, ((n1 / 2) - 1), ((n1 / 2))), sy(spin1, ((n1 / 2)), ((n1 / 2)))) + np.dot(
                sz(spin1, ((n1 / 2) - 1), ((n1 / 2))), sz(spin1, ((n1 / 2)), ((n1 / 2))))
            macierz = np.zeros((int((2 * spin1 + 1) ** ((n1 / 2))), int((2 * spin1 + 1) ** ((n1 / 2)))), dtype=complex)
            for i1 in range(int((2 * spin1 + 1) ** ((n1 / 2)))):
                for i2 in range(int((2 * spin1 + 1) ** ((n1 / 2)))):
                    macierz[i1][i2] = laczenieS(i1, i2, spin1, n1)
            wm, vm = np.linalg.eig(macierz)
            ind = np.argsort(np.real(wm))[:int(2 * spin1 * (2 * spin1 + 1) ** ((n1 / 2) - 1)) - 1:-1]
            T = np.transpose(np.array([vm[:, k] for k in ind]))
            T2 = np.conjugate(np.transpose(T))
            x = np.matmul(np.matmul(T2, ham4), T)
            tabx.append(x)
            y = taby[2*petla - i - 1]
            print(temp[1] / (n1 + 2 * (petla - 1)))
        plik = open('plikzzz', 'a')
        plik.write(" " + str(temp[1] / (n1 + 2 * (petla - 1))))
        print(" " + str(temp[1] / (n1 + 2 * (petla - 1))))
        plik.close()
        plik = open('plikzzz1', 'a')
        plik.write(" " + str(z))
        plik.close()
        taby = taby[0:petla]
        # wykres eneria/n efektywne ktore zaczyna sie od 10 dla 10 spinow i potem idzie 12,14,16..
        # wykres eneria/ n efektywne maxymalne na kolejne przemiatania
