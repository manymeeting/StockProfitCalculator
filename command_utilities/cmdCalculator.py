def formatTwoDecimalPoints(floatNum):
    """Return a string of the float number with only two decimal points."""
    return "%.2f" % floatNum

def calcProceeds(finalSharePrice, allotment):
    """Return Final Share Price * Allotment."""
    return finalSharePrice * allotment

def calcPurchasePrice(initialSharePrice, allotment):
    """Return Initial Share Price * Allotment."""
    return initialSharePrice * allotment

def calRawProfit(initialSharePrice, finalSharePrice, allotment, buyCommission, sellCommission):
    """Return (Final Share Price - Initial Share Price) * Allotment - Buy Commission - Sell Commission)."""
    return (finalSharePrice - initialSharePrice) * allotment  - buyCommission - sellCommission

def calcTax(rawProfit, taxRate):
    """Return Raw Profit * Tax Rate%."""
    return rawProfit * taxRate / 100

def calcToBreakEvenPrice(initialSharePrice, allotment, buyCommission, sellCommission):
    """Return (Buy Commission + Sell Commission) / Allotment +  Initial Share Price."""
    return (buyCommission + sellCommission) / allotment + initialSharePrice

CURRENCY = "$"

# prompt for inputs
print "Compute Your Profit:\n\n"
ticketSymbol = raw_input("Ticket Symbol:\n")

allotment = int(raw_input("Allotment:\n"))

finalSharePrice = float(raw_input("Final Share Price:\n"))
# print formatTwoDecimalPoints(finalSharePrice) + "\n\n"

sellCommission = float(raw_input("Sell Commission:\n"))

initialSharePrice = float(raw_input("Initial Share Price:\n"))

buyCommission = float(raw_input("Buy Commission:\n"))

taxRate = float(raw_input("Capital Gain Tax Rate:\n"))


# calculate values
purchasePrice = calcPurchasePrice(initialSharePrice, allotment)
rawProfit = calRawProfit(initialSharePrice, finalSharePrice, allotment, buyCommission, sellCommission)
tax = calcTax(rawProfit, taxRate)
cost = purchasePrice + buyCommission + sellCommission + tax
netProfit = rawProfit - tax

# display result
print "\n"
print "PROFIT REPORT:\n"
print "Proceeds\n"
print CURRENCY + formatTwoDecimalPoints(calcProceeds(finalSharePrice, allotment)) + "\n\n"
print "Cost\n"
print CURRENCY + str(cost) + "\n\n"
print "Cost details:\n"
print "Total Purchase Price:\n"
print str(allotment) + " x " + CURRENCY + str(allotment) + " = " + str(purchasePrice) + "\n"
print "Buy Commission = " + formatTwoDecimalPoints(buyCommission) + "\n"
print "Sell Commission = " + formatTwoDecimalPoints(sellCommission) + "\n"
print "Tax on Capital Gain = " + str(taxRate) + "%" + " of " + CURRENCY + formatTwoDecimalPoints(rawProfit) + " = " + formatTwoDecimalPoints(tax) + "\n\n"
print "Net Profit:\n"
print CURRENCY + formatTwoDecimalPoints(netProfit) + "\n\n"
print "Return on Investment:\n"
print formatTwoDecimalPoints(100 + (netProfit - cost) / cost * 100) + "%" + "\n"
print "To break even, you should have a final share price of \n"
print CURRENCY + formatTwoDecimalPoints(calcToBreakEvenPrice(initialSharePrice, allotment, buyCommission, sellCommission))






