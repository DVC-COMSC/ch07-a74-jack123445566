number = list(map(int, input().split()))
print (number)
# number is sorted

delnum = int(input())

cnt = number.count(delnum)
# for i in range(cnt):
# 	number.remove(delnum)

while True:
	try:
		number.remove(delnum)
	except: 
		break
