from random import choice

nums_alphs = [ str(i) for i in range(1,11)]

nums_alphs += ["a", "b", "c", "d"]

def winning_draw():
    winning_lot = [choice(nums_alphs) for i in range(0,4)]
    return winning_lot


def new_ticket():
    new_ticket = [ choice(nums_alphs) for i in range(0,4)]
    return new_ticket

print(f"The winning lottery ticket is: {' '.join(winning_draw())}")