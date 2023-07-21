## Take from Fluent Python, 2nd Edition (https://www.oreilly.com/library/view/fluent-python-2nd/9781492056348/)


class TwilightBusWrong:
    def __init__(self, passengers=None):
        if passengers is None:
            self.passengers = []  
        else:
            # create a aliases for list passed
            self.passengers = passengers  

    def pick(self, name):
        self.passengers.append(name)

    def drop(self, name):
        self.passengers.remove(name)


class TwilightBusRight:
    def __init__(self, passengers=None):
        if passengers is None:
            self.passengers = []
        else:
			# create a new LIST, making a copy from list passed
            self.passengers = list(passengers) 

    def pick(self, name):
        self.passengers.append(name)

    def drop(self, name):
        self.passengers.remove(name)