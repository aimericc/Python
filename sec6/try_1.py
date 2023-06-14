def myfunc(x):
    out = []
    for i_1 in range(len(x)):
        if i_1 % 2 == 0:
            out.append(x[i_1].lower())
        else:
            out.append(x[i_1].upper())
    return ''.join(out)


results = myfunc("how to solve this")
print(results)
