A_beat_B=int(input("A beat B="))
B_beat_C=int(input("B beat C="))
A=int(input("Winner distance of A= "))
B=A-A_beat_B
b=int(input("Winning distance of B="))
C=b-B_beat_C
c=(A/B*b/C)
print(c)
A_beat_C=A-(A/c)
print("A_beat_C="+str(A_beat_C))
