# Exercise Three (Lists)

# - List show number of lemonades sold per day
# - Profit for each lemonade sold is $1.5
# - Add another day to week 2 with an input
# - Combine the two lists into sales
# - Calculate your best day, worst day, separately and in Total 

sales_w1 = [7,3,42,19,15,35,9]
sales_w2 = [12,4,26,10,7,28]
sales = []

new_w2_day = input('Choose a number from 1-45:')

new_day = int(new_w2_day)

sales_w2.append(new_day)
sales = sales_w1 + sales_w2

bd_w1 = max(sales_w1) * 1.50
wd_w1 = min(sales_w1) * 1.50
combined_bw_w1 = bd_w1 + wd_w1

bd_w2 = max(sales_w2) * 1.50
wd_w2 = min(sales_w2) * 1.50
combined_bw_w2 = bd_w2 + wd_w2

bd_overall = max(sales) * 1.50
wd_overall = min(sales) * 1.50
combined_bw_overall = bd_overall + wd_overall

print(f'Your best day for week one was ${bd_w1} in profits!')
print(f'Your worst day for week one was ${wd_w1} in profits...')
print(f'Your combined profit for your best and worst day for week one was ${combined_bw_w1} in profits!')

print(f'Your best day for week two was ${bd_w2} in profits!')
print(f'Your worst day for week two was ${wd_w2} in profits...')
print(f'Your combined profit for your best and worst day for week two was ${combined_bw_w2} in profits!')

print(f'Your best day from both weeks was ${bd_overall} in profits!')
print(f'Your worst day from both weeks was ${wd_overall} in profits...')
print(f'Your combined profit for your best and worst day from both weeks was ${combined_bw_overall} in profits!')