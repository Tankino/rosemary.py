from kitchen import Rosemary
from kitchen.utensils import Pan, Plate, Bowl, Oven, BakingTray
from kitchen.ingredients import Egg, Flour, Milk, Salt, Butter, Sugar, ChocolateChips, BakingPowder

oven=Oven.use()
oven.preheat(degrees=175)

#Start making the batter
bowl=Bowl.use(name='Batter')
bowl.add(Butter.take(grams=200))

#adding sugar
for i in range(5):
    bowl.add(Sugar.take(grams=40))
    bowl.mix

#Adding eggs
egg = Egg.take()
for i in range(2):
    
    egg.crack()
    bowl.add(egg)
    bowl.mix()
bowl.add(Salt.take('Dash'))

#Adding flour choclate chips and baking powder
for i in range(4):
    bowl.add(Flour.take(grams=75))
    bowl.add(ChocolateChips.take(grams=50))
    bowl.mix()

bowl.add(BakingPowder.take(grams=5))


 #putting cookies on baking tray

bakingtray = BakingTray.use(name='ChoclateChipCookieBatter')
for i in range (16):
    bakingtray.add(bowl.take('1/16'))

#baking and taking cookies off baking tray
oven.add(bakingtray)
oven.bake(minutes=10)    

plate = Plate.use(name='cookies')
cookies=bakingtray.take()
plate.add(cookies)

Rosemary.serve(plate)
