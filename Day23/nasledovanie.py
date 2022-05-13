data = {

"markers": [

{

"name": "Rixos The Palm Dubai",

"location": [25.1212, 55.1535],

},

{

"name": "Shangri-La Hotel",

"location": [25.2084, 55.2719]

},

{

"name": "Grand Hyatt",

"location": [25.2285, 55.3273]

}

]

}


class Hotels:

    def __init__(self, name, locations):
        self.name = name
        self.locations = locations

    def get_name(self): #Метод который вернёт все имена отелей.
        return self.name

    def get_nam_loc(self):  #Метод который из собирает все name в один Tuple и locations в другой и возвращает
        # dictionary c двумя ключами списками со всеми значениями.

        # dct = dict()
        #
        # for name, loc in zip(self.name, self.locations):
        #     dct[name] = loc

        return dict(zip(self.name, self.locations))

    def add_new_mark(self): #3.Метод который добавит к каждому элементу в markers поле status_id: 1
        pass


names = [i['name'] for i in data['markers']]
loc = [i['location'] for i in data['markers']]
hotel = Hotels(names, loc)
print(hotel.get_name())
print(hotel.get_nam_loc())
