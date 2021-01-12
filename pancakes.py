from kitchen import Rosemary
from kitchen.utensils import Pan, Plate, Bowl
from kitchen.ingredients import Egg, Flour, Milk, Salt, Butter

#Putting 2 eggs in a bowl and mixing
bowl=Bowl.use(name='Pancake')
for i in range(2):
    egg = Egg.take()
    egg.crack()
    bowl.add(egg)
bowl.mix()
bowl.add(Salt.take('Dash'))

#Mixing in the flour in batches 
for i in range(5):
    bowl.add (Flour.take(grams=50))
    bowl.mix()

#mixing in the milk in batches

for i in range (2):
    bowl.add (Milk.take(ml=250))
    bowl.mix()

#making the actual pancakes
pan = Pan.use(name='pancake')
plate = Plate.use()

for i in range(8):
    pan.add(Butter.take('slice'))
    pan.add(bowl.take('1/8'))
    pan.cook(minutes=1)
    pan.flip()
    pan.cook(minutes=1)
    pancake = pan.take()
    plate.add(pancake)

Rosemary.serve(plate)
