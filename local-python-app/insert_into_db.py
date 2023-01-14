import plotly
import sys

class ExpenseType(object):
    def __init__(self, name, colour, expense=True):
        self.prices = []
        self.days = []
        self.texts = []
        self.name = name
        self.colour = colour
        self.expense = expense


expense_types = [
        ExpenseType('basic', 'rgb(0, 0, 205)'),
        ExpenseType('cadeau', 'rgb(145, 90, 225)'),
        ExpenseType('donation', 'rgb(0, 205, 205)'),
        ExpenseType('education', 'rgb(80, 180, 255)'),
        ExpenseType('energie', 'rgb(255, 255, 0)'),
        ExpenseType('fine', 'rgb(205, 0, 0)'),
        ExpenseType('foods', 'rgb(224, 157, 40)'),
        ExpenseType('fuel', 'rgb(0, 0, 0)'),
        ExpenseType('groceries', 'rgb(160, 40, 255)'),
        ExpenseType('income', 'rgb(0, 205, 0)', expense=False),
        ExpenseType('insurance', 'rgb(255, 0, 255)'),
        ExpenseType('internet', 'rgb(100, 50, 255)'),
        ExpenseType('holiday', 'rgb(205, 80, 0)'),
        ExpenseType('kleding', 'rgb(255, 98, 135)'),
        ExpenseType('lego', 'rgb(227, 0, 11)'),
        ExpenseType('luxe', 'rgb(205, 205, 0)'),
        ExpenseType('meubels', 'rgb(200, 200, 200)'),
        ExpenseType('radio', 'rgb(41, 34, 36)'),
        ExpenseType('server', 'rgb(15, 15, 15)'),
        ExpenseType('telefoon', 'rgb(210, 50, 210)'),
        ExpenseType('train', 'rgb(246, 255, 0)'),
        ExpenseType('tuin', 'rgb(30, 255, 10)'),
        ExpenseType('verwarming', 'rgb(255, 0, 25)'),
        ExpenseType('voertuig', 'rgb(80, 80, 0)'),
        ExpenseType('water', 'rgb(60, 65, 255)'),
        ExpenseType('work', 'rgb(0, 80, 0)'),
        ExpenseType('zorg', 'rgb(185, 255, 255)'),
        ]

def expense_get_all_types():
    types = []
    for expense_type in expense_types:
        types.append(expense_type.name)
    return types

def parse_file_expenditures(year):
    transactions = []
    with open('expenditures_{}'.format(year)) as input_file:      
        for item in input_file.read().rstrip().split(';'):
            try:
                data = item.split(',')            
                data_dict = {
                    'type': data[0],
                    'description': data[1],
                    'price': float(data[2]),
                    'date': data[3],
                    'time': data[4],
                    'store_name': data[5],
                    'location': data[6]
                }
                transactions.append(data_dict)
            except IndexError:
                print('ERROR - cannot parse: {}'.format(item))
                sys.exit()

    return transactions

def parse_file_savings():
    savings = []
    with open('savings') as input_file:
        for item in input_file.read().rstrip().split(';'):
            try:
                data = item.split(',')
                data_dict = {
                    'year': data[0].split('-')[0],
                    'month': data[0].split('-')[1],
                    'saving_amount': data[1],
                }
                savings.append(data_dict)
            except IndexError:
                print('ERROR - cannot parse: {}'.format(item))
                sys.exit()

    return savings

def get_year(transactions):
    return transactions[0]['date'].split('-')[0]

def expense_get_colour(expense_name):
    for expense_type in expense_types:
        if expense_type.name == expense_name:
            return expense_type.colour
    return 'rgb(0,0,0)'

def expense_is_income(expense_name):
    for expense_type in expense_types:
        if expense_type.name == expense_name:
            return not expense_type.expense

def expense_is_savings(expense_name):
    for expense_type in expense_types:
        if expense_type.name == expense_name:
            return expense_type.savings

def plot_days_per_month(month, transactions):
    expenses = get_prices_per_month(month, transactions)
    year = get_year(transactions)

    traces = []
    for expense in expenses:
        traces.append(
            plotly.graph_objs.Bar(
                x=expense.days,
                y=expense.prices,
                text=expense.texts,
                name=expense.name,
                marker=dict(
                    color=expense.colour,
                )
            )
        )
    data = traces
    layout = plotly.graph_objs.Layout(
            title=f'{year}-{month} daily expenses',
    )

    figure = plotly.graph_objs.Figure(data=data, layout=layout)
    figure.update_xaxes(categoryorder='category ascending', title_text='day')
    figure.update_yaxes(categoryorder='total ascending', tickprefix= '€', title_text='amount in Euro')
    plotly.offline.plot(figure, filename=f'days-of-month-{year}-{month}.html')
    figure = None

def plot_monthly_totals_per_year(transactions):
    months = ['01', '02', '03', '04', '05', '06', '07', '08', '09', '10', '11', '12']
    traces = []
    totals = {}
    year = get_year(transactions)

    for expense_type in expense_types:
        totals[expense_type.name] = []
    
    for month in months:
        expenses = get_totals_per_month(month, transactions)
        for key, value in expenses.items():
            totals[key].append(value)

    for key, value in totals.items():
        traces.append(
            plotly.graph_objs.Bar(
                x = months,
                y = value,
                name = key,
                marker = dict(
                    color = expense_get_colour(key)
                )
            )
        )

    data = traces
    layout = plotly.graph_objs.Layout(
                xaxis = dict(
                   tickangle = -45,
                ),
               barmode = 'group',
               title=f'{year} monthly totals',
            )
    figure = plotly.graph_objs.Figure(data=data, layout=layout)
    figure.update_xaxes(categoryorder='category ascending')
    figure.update_yaxes(categoryorder='total ascending', tickprefix= '€', title_text='amount in Euro')
    plotly.offline.plot(figure, filename='monthly-totals-{}.html'.format(year))

def plot_monthly_in_and_out_per_year(transactions, savings=None):
    months = ['01', '02', '03', '04', '05', '06', '07', '08', '09', '10', '11', '12']
    exp_in_list = []
    exp_out_list = []
    traces = []    
    year = get_year(transactions)

    for month in months:
        exp_in = 0
        exp_out = 0
        expenses = get_totals_per_month(month, transactions)
        for key, value in expenses.items():
            if expense_is_income(key):
                exp_in += value
            else:
                exp_out += value
        exp_in_list.append(exp_in)
        exp_out_list.append(exp_out)

    trace_income = plotly.graph_objs.Bar(
        x = months,
        y = exp_in_list,
        name = 'incomes',
        marker = dict(
            color = 'rgb(50,255,100)',
        )
    )
    trace_expense = plotly.graph_objs.Bar(
        x = months,
        y = exp_out_list,
        name = 'expenditures',
        marker = dict(
            color = 'rgb(255,50,100)',
        )
    )
    
    traces.append(trace_income)
    traces.append(trace_expense)
    
    if savings:
        exp_save_list = []
        
        for saving in savings:
            if saving['year'] == year:
                exp_save_list.append(saving['saving_amount'])

        trace_savings = plotly.graph_objs.Bar(
            x = months,
            y = exp_save_list,
            name = 'savings',
            marker = dict(
                color = 'rgb(0,75,255)',
            )
        )

        traces.append(trace_savings)
    
    data = traces
    layout = plotly.graph_objs.Layout(
        xaxis = dict(
            tickangle = -45,
        ),
        barmode = 'group',
        title= f'{year} monthly income & expenses',
    )
    figure = plotly.graph_objs.Figure(data=data, layout=layout)
    figure.update_xaxes(categoryorder='category ascending')
    figure.update_yaxes(categoryorder='total ascending', tickprefix= '€', title_text='amount in Euro')
    plotly.offline.plot(figure, filename='monthly-incomes-and-expenses-{}.html'.format(year))

def plot_yearly_in_and_out_per_year(savings=None):
    years = ['2018', '2019', '2020', '2021', '2022']
    exp_in_list = []
    exp_out_list = []
    traces = []

    for year in years:
        exp_in = 0
        exp_out = 0
        expenses = get_totals_per_year(year)
        for key, value in expenses.items():
            if expense_is_income(key):
                exp_in += value
            else:
                exp_out += value
        exp_in_list.append(exp_in)
        exp_out_list.append(exp_out)

    trace_income = plotly.graph_objs.Bar(
        x = years,
        y = exp_in_list,
        name = 'incomes',
        marker = dict(
            color = 'rgb(50,255,100)',
        )
    )
    trace_expense = plotly.graph_objs.Bar(
        x = years,
        y = exp_out_list,
        name = 'expenditures',
        marker = dict(
            color = 'rgb(255,50,100)',
        )
    )

    traces.append(trace_income)
    traces.append(trace_expense)

    if savings:
        exp_save_list = []

        for saving in savings:
            if saving['year'] == year:
                exp_save_list.append(saving['saving_amount'])

        trace_savings = plotly.graph_objs.Bar(
            x = years,
            y = exp_save_list,
            name = 'savings',
            marker = dict(
                color = 'rgb(0,75,255)',
            )
        )

        traces.append(trace_savings)

    data = traces
    layout = plotly.graph_objs.Layout(
        xaxis = dict(
            tickangle = -45,
        ),
        barmode = 'group',
        title= 'yearly income & expenses',
    )
    figure = plotly.graph_objs.Figure(data=data, layout=layout)
    figure.update_xaxes(categoryorder='category ascending')
    figure.update_yaxes(categoryorder='total ascending', tickprefix= '€', title_text='amount in Euro')
    plotly.offline.plot(figure, filename='yearly-incomes-and-expenses.html')


def plot_totals_per_year_categories():
    years = ['2018', '2019', '2020', '2021', '2022']
    traces = []
    totals = {}

    for expense_type in expense_types:
        totals[expense_type.name] = []

    for year in years:
        expenses = get_totals_per_year(year)
        for key, value in expenses.items():
            totals[key].append(value)

    for key, value in totals.items():
        traces.append(
            plotly.graph_objs.Bar(
                x = years,
                y = value,
                name = key,
                marker = dict(
                    color = expense_get_colour(key)
                )
            )
        )

    data = traces
    layout = plotly.graph_objs.Layout(
                xaxis = dict(
                   tickangle = -45,
                ),
               barmode = 'group',
               title='yearly totals per category',
            )
    figure = plotly.graph_objs.Figure(data=data, layout=layout)
    figure.update_xaxes(categoryorder='category ascending')
    figure.update_yaxes(categoryorder='total ascending', tickprefix= '€', title_text='amount in Euro')
    plotly.offline.plot(figure, filename='yearly-totals-categories.html')

def get_prices_per_month(month, transactions):
    days = []
    prices = []
    texts = []

    for expense_type in expense_types:
        expense_type.days = []
        expense_type.prices = []
        expense_type.texts = []

    for transaction in transactions:         
        t_day, t_month, t_year = get_day_month_year(transaction)
        if t_month == month:                      
            for expense_type in expense_types:
                if expense_type.name == transaction['type']:
                    days = expense_type.days
                    prices = expense_type.prices
                    texts = expense_type.texts
                    break

            # check if there is data already for that day
            if t_day in days:
                index = days.index(t_day)
                prices[index] = '{}'.format(round(float(prices[index]) + float(transaction['price']), 2))                
                texts[index] = '{} {},{}<br>{}'.format(
                        transaction['price'],
                        transaction['description'],
                        transaction['store_name'],
                        texts[index],
                        )
            else:
                prices.append(transaction['price'])
                days.append(t_day)
                texts.append('{} {},{}'.format(
                    transaction['price'], 
                    transaction['description'], 
                    transaction['store_name'],
                ))
    
    return expense_types

def get_day_month_year(transaction):
    try:
        dates = transaction['date'].split('-')
        year = dates[0]
        month = dates[1]
        day = dates[2]
    except IndexError as ex:
        print('Invalid transaction date format! - {}'.format(transaction))
        print(ex)
        sys.exit()

    if int(year) < 1900:
        raise Exception('invalid year: {}, transaction: {}'.format(year, transaction))
    if int(month) > 12:
        raise Exception('invalid month: {}, transaction: {}'.format(month, transaction))
    if int(day) > 31:
        raise Exception('invalid day: {}, transaction: {}'.format(day, transaction))
    return day, month, year

def get_totals_per_month(month, transactions):
    totals = {}
    year = get_year(transactions)

    for expense_type in expense_types:
        totals[expense_type.name] = 0
    
    for transaction in transactions:
        t_day, t_month, t_year = get_day_month_year(transaction)
        if t_year != year:
            print('ERROR - wrong year: {}, {}, {}, {}, expected: {}'.format(
                t_year,
                transaction['type'],
                transaction['description'],
                transaction['price'],
                year))
        if t_month == month and t_year == year:
            totals[transaction['type']] += float(transaction['price'])
    
    for key, value in totals.items():
        totals[key] = round(value, 2)

    return totals

def get_totals_per_year(year):
    totals = {}
    transactions = parse_file_expenditures(year)

    for expense_type in expense_types:
        totals[expense_type.name] = 0

    for transaction in transactions:
        t_day, t_month, t_year = get_day_month_year(transaction)
        if t_year != year:
            print('ERROR - wrong year: {}, {}, {}, {}, expected: {}'.format(
                t_year,
                transaction['type'],
                transaction['description'],
                transaction['price'],
                year))
        if t_year == year:
            totals[transaction['type']] += float(transaction['price'])

    for key, value in totals.items():
        totals[key] = round(value, 2)

    return totals


def main():
    print('{}'.format(plotly.__version__))
    transactions = parse_file_expenditures
    savings = parse_file_savings()
    
    year = '2022'

    for i in range(1,13):
        plot_days_per_month(f'{i:02d}', transactions(year))

    plot_monthly_in_and_out_per_year(transactions(year), savings=savings)
    plot_monthly_totals_per_year(transactions(year))
    plot_yearly_in_and_out_per_year()
    plot_totals_per_year_categories()


if __name__ == '__main__':
    main()


