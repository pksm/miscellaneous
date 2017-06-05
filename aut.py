for i in range(1,6):
	for j in range(1,6):
		k = 1
		if i==j:
			print ("$A_{"+str(i)+str(j)+"} \\to \\: \\varepsilon \\:|\\:A_{"+str(i)+str(k)+"}A_{"+str(k)+str(j)+"}\\:|\\: A_{"+str(i)+str(k+1)+"}A_{"+str(k+1)+str(j)+"}\\:|\\:A_{"+str(i)+str(k+2)+"}A_{"+str(k+2)+str(j)+"}\\:|\\:A_{"+str(i)+str(k+3)+"}A_{"+str(k+3)+str(j)+"}\\:|\\:A_{"+str(i)+str(k+4)+"}A_{"+str(k+4)+str(j)+"}$\\\\")
		else:
			print ("$A_{"+str(i)+str(j)+"} \\to \\: A_{"+str(i)+str(k)+"}A_{"+str(k)+str(j)+"}\\:|\\: A_{"+str(i)+str(k+1)+"}A_{"+str(k+1)+str(j)+"}\\:|\\:A_{"+str(i)+str(k+2)+"}A_{"+str(k+2)+str(j)+"}\\:|\\:A_{"+str(i)+str(k+3)+"}A_{"+str(k+3)+str(j)+"}\\:|\\:A_{"+str(i)+str(k+4)+"}A_{"+str(k+4)+str(j)+"}$\\\\")