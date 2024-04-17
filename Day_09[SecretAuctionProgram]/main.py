from art import logo

 
# Clearing the Screen

print(logo)

auction_dict = {}
flag = "yes"
while(flag =="yes"):
  name = input("What is your name?: ")
  bid = int(input("What is your bid?: $"))
  auction_dict[name] = bid
  flag = input("Are there any other bidders? Type 'yes or 'no'.")
  if flag=="yes":
    clear()

maxi = 0
winner_name = ""
winner_res = 0
for key in auction_dict:
  bid = auction_dict[key]
  if bid > maxi:
    winner_res = bid
    winner_name = key

print(f"The winner is {winner_name} with a bid of ${winner_res}") 
print("game over!!")