if __name__ == '__main__':
    n = int(input())
    mrk = {}
    for i in range(n):
        string=input()
        name, m1, m2, m3 = string.split()
        mrk[name]=[float(m1), float(m2), float(m3), (float(m1)+float(m2)+float(m3))/3]
name = input()
print("{0:.2f}".format(mrk[name][-1]))