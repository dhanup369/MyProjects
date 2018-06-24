def mymean():
    s=0
    a = input("Enter the numbers: ").split()
    for i in a:
        s=s+int(i)
    return s/len(a)
