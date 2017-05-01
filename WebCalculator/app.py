from flask import Flask, render_template, request

app = Flask(__name__)

@app.route('/', methods=['GET', 'POST'])
def index():
    if request.method == 'GET':
        return render_template('index.html')
    elif request.method == 'POST':
        symbol = request.form['symbol']
        allotment = request.form['allotment']
        final_share = request.form['final_share']
        sell_commission = request.form['sell_commission']
        initial_share = request.form['initial_share']
        buy_commission = request.form['buy_commission']
        tax_rate = request.form['tax_rate']

        proceeds = int(allotment) * float(final_share)
        tax_total = (((float(final_share) - float(initial_share)) * int(allotment) - float(buy_commission) - float(sell_commission))) 
        tax = tax_total * float(tax_rate) / 100
        total_purchase_price = int(allotment) * float(initial_share)
        cost = total_purchase_price + float(buy_commission) + float(sell_commission) + tax
        net_profit = proceeds - cost
        return_on_investment = net_profit / cost * 100
        break_even = (total_purchase_price + float(buy_commission) + float(sell_commission)) / int(allotment)

        reproceeds = "$%.2f" % proceeds
        recost = "$%.2f" % cost
        retotal = allotment + " x $" + initial_share + " = " + "%.2f" % total_purchase_price
        gain = tax_rate + "% of $" + "%.2f" % tax_total + " = " + "%.2f" % tax
        renet_profit = "$" + "%.2f" % net_profit
        rereturn_on_investment = "%.2f" % return_on_investment + "%"
        rebreak_even = "$" + "%.2f" % break_even

        tmpData = {'displaySymbol': symbol, 'allot': allotment,
                   'fshare': final_share, 'scomm':sell_commission,
                   'ishare':initial_share, 'bcomm':buy_commission,
                   'crate':tax_rate, 'proceeds':reproceeds, 'gain':gain,
                   'cost':recost, 'total_purchase': retotal, 'net_profit':renet_profit,
                   'return_invest':rereturn_on_investment, 'break_even':rebreak_even}
        return render_template('index.html', **tmpData)

if __name__ == '__main__':
    app.run(debug=True, host='0.0.0.0')
