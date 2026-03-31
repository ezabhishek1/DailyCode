Approach
I used Dynamic Programming with only two variables.

hold stores the best profit possible while holding a stock.

cash stores the best profit possible while not holding a stock.

Initially:

hold = -arr[0]

Because if I buy the stock on day 1, my profit becomes negative.

cash = 0

Because if I do nothing, profit is 0.


Now for every next day:

Either I continue holding the stock.

Or I buy the stock today.

So:

hold = max(hold, cash - arr[i])
Similarly:

Either I continue without stock.

Or I sell the stock today and pay the fee.

So:

cash = max(cash, hold + arr[i] - k)
At the end, cash will contain the maximum possible profit because I should not end while still holding a stock.