symbol = raw_input("Enter a stock symbol: ")
allotment = raw_input("Enter allotment (number of shares): ")
final_share = raw_input("Enter final share price (in dollars): ")
sell_commission = raw_input("Enter sell commission (in dollars): ")
initial_share = raw_input("Enter initial share price (in dollars): ")
buy_commission = raw_input("Enter buy commission (in dollars): ")
tax_rate = raw_input("Enter capital gain tax rate (in %): ")

proceeds = int(allotment) * float(final_share)
tax_total = (((float(final_share) - float(initial_share)) * int(allotment) - float(buy_commission) - float(sell_commission))) 
tax = tax_total * float(tax_rate) / 100
total_purchase_price = int(allotment) * float(initial_share)
cost = total_purchase_price + float(buy_commission) + float(sell_commission) + tax
net_profit = proceeds - cost
return_on_investment = net_profit / cost * 100
break_even = (total_purchase_price + float(buy_commission) + float(sell_commission)) / int(allotment)

print("Compute Your Profit: \n")
print("Ticker Symbol:")
print(symbol + '\n')
print("Allotment:")
print(allotment + '\n')
print("Final Share Price:")
print(final_share + '\n')
print("Sell Commission:")
print(sell_commission + '\n')
print("Initial Share Price:")
print(initial_share + '\n')
print("Buy Commission:")
print(buy_commission + '\n')
print("Capital Gain Tax Rate(%):")
print(tax_rate + '\n')
print("PROFIT REPORT: ")
print("Proceeds")
print("$%.2f" % proceeds)
print
print("Cost")
print("$%.2f" % cost)
print
print("Cost details:")
print("Total Purchase Price")
print(allotment + " x $" + initial_share + " = " + "%.2f" % total_purchase_price)
print("Buy Commission = %.2f" % float(buy_commission))
print("Sell Commission = %.2f" % float(sell_commission))
print("Tax on Capital Gain = " + tax_rate + "% of $" + "%.2f" % tax_total + " = " + "%.2f" % tax + '\n')
print("Net Profit")
print("$" + "%.2f" % net_profit + '\n')
print("Return on Investment")
print("%.2f" % return_on_investment + "%" + '\n')
print("To break even, you should have a final share price of ")
print("$" + "%.2f" % break_even + '\n')
