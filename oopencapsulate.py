from oopcorganitem import Item

item1 = Item("MyItem", 750, 23)
item1.name = "OtherItem" #SETTING AN ATTRIBUTE  using @name.setters
print(item1.name)  #GETTING AN ATTRIBUTE

#item1.price = "OtherItem" #SETTING AN ATTRIBUTE  using @name.setters
print(item1.price)  #GETTING AN ATTRIBUTE
item1.apply_increment(0.2)
item1.apply_discount()
print(item1.price)

