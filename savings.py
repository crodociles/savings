import datetime
from datetime import date

#declare vars
total = 0
now = datetime.date(date.today().year, date.today().month, date.today().day)
yearStart = datetime.date(date.today().year, 1, 1)
dayNum = ((now - yearStart).days)
dayNum += 1

#get total from adding all days previous up to today together
for x in range(1,dayNum):
	total = total + x
	pass

#function for finding smallest number of coins to make total
def coins():
	#declare vars
	coinsStr = ""
	coinsTotal = total + dayNum
	coinsList = [200, 100, 50, 20, 10, 5, 2, 1]
	coinNames = ["£2", "£1", "50p", "20p", "10p", "5p", "2p", "1p"]
	coinNums = [0,0,0,0,0,0,0,0]
	
	#for all coins
	for x in range(0,len(coinsList)):
		#if total greater than coin add one to appropriate column
		if coinsTotal/coinsList[x] > 0:
			coinNums[x]=int(coinsTotal/coinsList[x])
			coinsTotal = coinsTotal - coinNums[x] * coinsList[x]
		pass
	pass

	#create string for each coin
	for x in range(0,len(coinNums)):
		if coinNums[x] > 0:
			coinsStr += "\n"
			coinsStr += coinNames[x]
			coinsStr += " x"
			coinsStr += str(coinNums[x])
		pass
	#print string
	print("The easiest way to make this is to use the following coins:", coinsStr)


print("Today's date is ", now.strftime('%b %d %Y'), "which means its day", dayNum, "of this year")
print("You should add £",'{0:.2f}'.format(dayNum / 100), "to your savings today, meaning your total should be £", '{0:.2f}'.format((total + dayNum)/100))
coins()
