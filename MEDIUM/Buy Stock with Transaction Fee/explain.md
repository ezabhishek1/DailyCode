Approach
I used Dynamic Programming with only two variables.

hold stores the best profit possible while holding a stock.

cash stores the best profit possible while not holding a stock.

Initially:

hold = -arr[0]

Because if I buy the stock on day 1, my profit becomes negative.

cash = 0

Because if I do nothing, profit is 0.