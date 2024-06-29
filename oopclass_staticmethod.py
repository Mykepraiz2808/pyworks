# when to use class method and when to use to use static method

class Item:
    @staticmethod
    def is_integer():
        '''
        THIS SHOULD DO SOMETHING THAT HAS A RELATIONSHIP WITH THE CLASS,
         BUT NOT SOMETHING THAT MUST BE UNIQUE PER INSTANCE !
        :return:
        '''


    @classmethod
    def instantiate_from_something(cls):

        '''
        THIS SHOULD ALSO DO SOMETHING THAT HAS A RELATIONSHIP WITH THE CLASS,
        BUT USUALLY, THOSE ARE USED TO MANIPULATE DIFFERENT STRUCTURES OF DATA TO
        INSTANTIATE OBJECTS, LIKE WE HAVE DONE WITH CSV. 
        '''

        '''THE CLASS METHOD AND INSTANCE METHOD CAN ONLY BE CALLED FROM CLASS LEVEL BUT HOWEVER
        THOSE ALSO COULD BE CALLED FROM INSTANCES, BUT THERE IS NOT A REASON TO CALL BOTH OF
        THEM FROM INSTANCE LEVEL(IT IS JUST AN OPTION THAT IS AVAILABLE)
 e.g.
       '''
item1 = Item()
item1.is_integer(5)
item1.instantiate_from_something()