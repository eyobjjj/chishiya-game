import random
import os
import getpass
os.system('cls')

def bot(bot):
  bot_no = []
  for i in range(bot):
    n = random.randint(0,101)
    bot_no.append(n)
  return bot_no

def calculator(*args):
  closest_value = None
  closest_difference = float('inf')
  average = sum(args) / len(args)
  for num in args:
    difference = abs(num - average * 0.8)
    if difference < closest_difference:
        closest_value = num
        closest_difference = difference
  return closest_value


def resultPrint(lists, result):
  # print like banner
  average = sum(lists) / len(lists)
  print(lists)
  print(f"{average} * 0.8 ==== {average*0.8}")
  print(result)


players = []
def player_info(*args):
  bot_names = ["Ninja", "Jon", "Abe", "Alice"]
  args = (list(args))
  args.extend(bot_names)
  for i in args[:5]:
    players.append({"name":i, "life":10, "select":0})
  printPlayer()
  print("\n-------- Game Start ---------\n")


def printPlayer():
  print("------------------------------------")
  for i in players:
    print(f"|  {i['name']} |   {i['life']}  |  {i['select']}")
    print("------------------------------------")

def resultMaker(player):
  for i in players:
    if i['select'] == player:
      player = i['name']
  print(f"{player} win!")
  for i in players:
    if i['name'] == player:
      continue
    i['life']-=1



def run(player_count,cr_pl,*args):
  bots = 5 - player_count
  # global lists  
  lists = bot(bots)
  args = (list(args))
  args.extend(lists)
  # global result
  result = calculator(*args)
  resultPrint(args, result)
  for i in range(cr_pl):
    player1 = players[i]['select'] = args[i]
    if result == player1:
      resultMaker(player1)
 
  # player1 = players[0]['select'] = args[0]
  # player2 = players[1]['select'] = args[1]
  # player3 = players[2]['select'] = args[2]
  # player4 = players[3]['select'] = args[3]
  # player5 = players[4]['select'] = args[4]
    
  # if result == player1:
  #   resultMaker(player1)
  # elif result == player2:
  #   resultMaker(player2)
  # elif result == player3:
  #   resultMaker(player3)
  # elif result == player4:
  #   resultMaker(player4)
  # elif result == player5:
  #   resultMaker(player5)
  printPlayer()

def nameInput(player_count):
    players = []
    for i in range(1, player_count + 1):
        player_name = input(f"player {i} name: ")
        players.append(player_name)
    player_info(*players)

def noInput(player_count):
    no = []
    for i in range(player_count):
        player1no = int(getpass.getpass(f"{players[i]['name']} (1-100): "))
        no.append(player1no)
    return no
    

def runn(player_count):
  nameInput(player_count)
  user = player_count
  uu = player_count
  playerc = player_count
  cr_pl = 5
  while True:
    for i in players:
      if i["life"] <= 0:
        cr_pl = cr_pl - 1
        
        for u in range(user): 
          if i == players[u]:
            user = user - 1
            uu = uu + 1
            print("*"*50)
        if playerc == uu:
          playerc = playerc + 1
        uu = playerc
        
        players.remove(i)
        print(f"lose {i['name']}")
    
    if len(players) == 1:
      print("*"*50)
      print("*"*50)
      print(f"            {players[0]['name']} win")
      print("*"*50)
      print("*"*50)
      break
    no = noInput(user)
    run(playerc,cr_pl,*no)



print("""   Alice in the borderland

      [ chishiya game ]       created by jj
      """)
player_count=int(input("how many player (1-5): "))
if player_count == 1:
  runn(player_count)
elif player_count == 2:
  runn(player_count)
elif player_count == 3:
  runn(player_count)
elif player_count == 4:
  runn(player_count)
elif player_count == 5:
  runn(player_count)
else:
  print('please select 1-5 only')











