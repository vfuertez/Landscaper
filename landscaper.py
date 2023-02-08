

work = {'tool': 0, 'bank': 0}

equipment = [
    {"name": "teeth", "income": 1, "cost": 0},
    {"name": "rusty scissors", "income":5 , "cost": 5},
    {"name": "lawnmower", "income": 50, "cost": 25},
    {"name": "fancy lawnmower", "income": 100, "cost": 250},
    {"name": "team of starving students", "income": 250, "cost": 500},
]

def landscape():
    tool = equipment[work[tool]]
    print(f'You made an income of {equipment["income"]} using your {equipment["name"]}')
    work["bank"] += equipment["income"]
    
def status():
    tool = equipment[work['tool']]
    print(f"Your current equipment is {tool['name']} and have a bank account of {work['bank']} ")
    
def buy():
    equipment_upgrade = equipment[work['tool']+1]
    if (equipment_upgrade == None):
        print("You can't upgrade anymore")
        return 0
    if (equipment_upgrade < equipment['cost']):
        print("Not enough money")
        return 0
    if (work['bank'] < equipment_upgrade['cost']):
        print('not enough money') 