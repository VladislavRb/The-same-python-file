A = int(input("A: "))
B = int(input("B: "))
C = int(input("C: "))
if B*B - 4*A*C > 0:
    X1 = (-B + (B*B - 4*A*C)**0.5)/(2*A)
    X2 = (-B - (B*B - 4*A*C)**0.5)/(2*A)
    print(str(X1) + "\n" + str(X2))
elif B*B - 4*A*C == 0:
    print(-0.5 * (B/A))
else:
    print("No roots.")
