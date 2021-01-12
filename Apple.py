from kitchen.ingredients.Ingredient import Water
from kitchen import Rosemary
from kitchen.utensils import Plate, Bowl, Oven, PieDish
from kitchen.ingredients import Egg, Flour, Salt, Butter, Sugar, Apple, Lemon, Cornstarch, Cinnamon

oven=Oven.use()
oven.preheat(degrees=175)
#Making the dough
bowl=Bowl.use(name='Dough')

bowl.add(Flour.take(grams=300))
bowl.add(Salt.take('Dash'))
bowl.mix()

for i in range(5):
    bowl.add(Butter.take(grams=50))
    bowl.mix()

bowl.add(Water.take(ml=100))

#Making the pie filling
filling=Bowl.use(name='Filling')
apple = Apple.take()
for i in range(6):
    apple.peel
    filling.add(apple)

lemon= Lemon.take()
lemon.zest()
lemon.squeeze()
filling.add(lemon)
filling.mix()
filling.add(Sugar.take(grams=150))
filling.add(Salt.take ('pinch'))
filling.add(Cornstarch.take('spoonful'))
filling.add(Cinnamon.take('teaspoon'))
filling.mix()

#making the topping
topping=Bowl.use(name='Topping')
egg = Egg.take()
egg.crack()
topping.add(egg)
topping.mix()
    

#putting everything together in a cake
piedish = PieDish.use(name='Applepie')
piedish.add(bowl.take('3/4'))
piedish.add(filling.take())
piedish.add(bowl.take('1/4'))
piedish.add(topping.take())

#baking and taking applepie off baking tray
oven.add(piedish)
oven.bake(minutes=60)    

plate = Plate.use(name='Applepie')
applepie=piedish.take()
plate.add(applepie)

Rosemary.serve(plate)