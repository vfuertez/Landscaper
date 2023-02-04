

work = {'tool': 0, 'cash': 0}

equipment = [
    {"name": "teeth", "income": 1, "cost": 0},
    {"name": "rusty scissors", "income":5 , "cost": 5},
    {"name": "lawnmower", "income": 50, "cost": 25},
    {"name": "fancy lawnmower", "income": 100, "cost": 250},
    {"name": "team of starving students", "income": 250, "cost": 500},
]

def do_work():
    tool = equipment[work[tool]]
    print(f'You made an income of {equipment["income"]} using your {equipment["name"]}')
    work["cash"] += equipment["income"]