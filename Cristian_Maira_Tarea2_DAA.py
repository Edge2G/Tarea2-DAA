def notBruteforce_threeSum(array):
	array.sort()
	if array[0] >= 0:
		print("Array only has positives") 
		return
	elif array[len(array)-1] <= 0:
		print("Array only has negatives") 
		return
	elif len(array) < 3:
		print("Not Enough elements")
	else:
		indicator=1
		for x in range(0,len(array)):
			forward=x+1
			backward=len(array)-1
			num1=array[x]
			while(forward < backward):
				num2=array[forward]
				num3=array[backward]
				if num1+num2+num3 == 0:
					print(indicator,")",num1,"+",num2,"+",num3," = ", "0")
					indicator=indicator+1
					backward=backward-1
			
				elif num1+num2+num3 > 0:
					backward=backward-1
			
				else:
					forward=forward+1