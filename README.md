# cryptocurrencies-report-generator
Cryptocurrency report generator that collect and store currencies's data every day in a JSON file. The system get the data through the Coinmarketcap APIs and stores 5 types of information:

1. The cryptocurrency with the largest volume (in $) of the last 24 hours
2. The best and worst 10 cryptocurrencies (by percentage increase in the last 24 hours)
3. The amount of money required to purchase one unit of each of the top 20 cryptocurrencies in order of capitalization
4. The amount of money required to purchase one unit of all cryptocurrencies whose last 24-hour volume exceeds $ 76,000,000
5. The percentage of gain or loss you would have made if you had bought one unit of each of the top 20 cryptocurrencies (in order of capitalization) the day before (assuming the      rank has not changed)
6. The best and worst 10 cryptocurrencies (by percentage increase over the last 7d)
7. Cryptocurrencies whose percentage in the last 24 hours is greater than 10% with their price
8. Cryptocurrencies whose percentage in the last 7d is greater than 10% and the price equal to or less than $10
9. Cryptocurrencies that have returned 5% in both 24 hours and 7 days
10. Cryptocurrencies with a price equal to or less than $1 that have returned 10% in the last 24 hours
