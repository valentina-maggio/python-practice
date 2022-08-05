
logo = '''
                         ___________
                         \         /
                          )_______(
                          |"""""""|_.-._,.---------.,_.-._
                          |       | | |               | | ''-.
                          |       |_| |_             _| |_..-'
                          |_______| '-' `'---------'` '-'
                          )"""""""(
                         /_________\\
                       .-------------.
                      /_______________\\
'''

print(logo)
print("Welcome to the secret auction program!")

clearConsole = lambda: print('\n' * 150)

end_bid = False

bids = {}
winner_name = ''
winner_bid = 0

def reveal_the_winner():
    winner_name = max(bids.keys(), key=(lambda new_key: bids[new_key]))
    winner_bid = bids[winner_name]
    print(f"The winner is {winner_name} with a bid of ${winner_bid}")

while not end_bid:
    name = input("What is your name?\n")
    bid = int(input("What\'s your bid?\n$"))

    bids[name] = bid
    others = input("Are there any other bidders? Type 'yes' or 'no'.\n")
    clearConsole()

    if others == 'no':
        end_bid = True
        reveal_the_winner()

