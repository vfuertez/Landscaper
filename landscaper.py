name = input('What is your name? ')

print(f"{name}, welcome to the game of Landscaper")

life = {'tool': 0, 'money': 0}

tools = [
    {"x": "teeth", "profit": 1, "cost": 0},
    {"x": "rusty scissors", "profit":5 , "cost": 5},
    {"x": "lawnmower", "profit": 50, "cost": 25},
    {"x": "fancy lawnmower", "profit": 100, "cost": 250},
    {"x": "team of starving students", "profit": 250, "cost": 500},
]

def check_store():
    print("""
          Teeth -- profit: 1 , Cost: 0
          
          Rusty Scissors -- profit: 5,  Cost: 5
          
          Lawnmower -- profit: 50, Cost: 25
          
          Fancy Lawnmower -- profit, Cost: 250
          
          Team of Starving Students -- profit: 250, Cost: 500
          """)
    
def upgrade():
    if (life["tool"] >= len(tools) -1):
        print(" no more upgrades")
    next_tool = tools[life["tool"] + 1]
    if (next_tool == None):
        print("You have the max upgrade")
        return 0
    if (life["money"] < next_tool["cost"]):
        print("Not enough to upgrade")
        return 0
    print("You upgraded your service")
    life["money"] -= next_tool["cost"]
    life["tool"] += 1

def check_stats():
    tool = tools[life["tool"]]
    print(f"You currently have {life['money']} and are using a {tool['x']} ")

def win_check():
    if(life["tool"] == 4 and life["money"] >= 1000 ):
        print("You win")
        return True
    return False

def check_stats():
    tool = tools[life["tool"]]
    print(f"You currently have {life['money']} and are using a {tool['x']} ")
    
def win_check():
    if(life["tool"] == 4 and life["money"] >= 1000 ):
        print("You win")
        return True
    return False