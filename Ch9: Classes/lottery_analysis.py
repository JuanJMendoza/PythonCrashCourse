from lottery import winning_draw, new_ticket

my_ticket = new_ticket()
winning_ticket = winning_draw()

count = 0

while my_ticket != winning_ticket:
    count +=1

    # buys new ticket
    my_ticket = new_ticket()

# prob = float(1.0)/count 

# print(f"The chances of winning this lottery is {'%.2f'%(prob)}%.")
print(f"It took {count} tries before you won.")
