from kitchen import Rosemary
from kitchen.utensils import Pan, Plate, Bowl, Oven, BakingTray
from kitchen.ingredients import Egg, Flour, Milk, Salt, Butter, Sugar, ChocolateChips, BakingPowder

oven=Oven.use()
oven.preheat(degrees=175)

Number_of_cookies = x

#Start making the batter
bowl=Bowl.use(name='Batter')
bowl.add(Butter.take(grams=12.5*Number_of_cookies))

#adding sugar
for i in range(5):
    bowl.add(Sugar.take(grams=2.5*Number_of_cookies))
    bowl.mix

#Adding eggs
egg = Egg.take()
for i in range(int(Number_of_cookies/8)):
    
    egg.crack()
    bowl.add(egg)
    bowl.mix()
bowl.add(Salt.take('Dash'))

#Adding flour choclate chips and baking powder
for i in range(4):
    bowl.add(Flour.take(grams=75/16*Number_of_cookies))
    bowl.add(ChocolateChips.take(grams=50/16*Number_of_cookies))
    bowl.mix()

bowl.add(BakingPowder.take(grams=5/16*Number_of_cookies))


 #putting cookies on baking tray

bakingtray = BakingTray.use(name='ChoclateChipCookieBatter')
for i in range (Number_of_cookies):
    bakingtray.add(bowl.take(f'1/{Number_of_cookies}'))

#baking and taking cookies off baking tray
oven.add(bakingtray)
oven.bake(minutes=10)    

plate = Plate.use(name='cookies')
cookies=bakingtray.take()
plate.add(cookies)

Rosemary.serve(plate)
