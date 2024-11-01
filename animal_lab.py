class Animal:
    def __init__(self, name, habitat, sound):
        self._name = name         
        self._habitat = habitat   
        self._sound = sound      
   
    def get_name(self):
        return self._name

    def get_habitat(self):
        return self._habitat
    
    def speak(self):
        return f"{self._name} makes a sound: {self._sound}"
    
class Dog(Animal):
        def __init__(self, name, habitat):
            super().__init__(name,habitat,"woolf!")
        def speak(self):
            return f"{self.get_name()} says: {self._sound} loudly in {self.get_habitat()}"
        def fetch(self):
            return f"{self.get_name()} is fetching the ball!"
    
class Cat(Animal):
        def __init__(self, name, habitat):
            super().__init__(name, habitat,"MEOOO!")
        def speak(self):
            return f"{self.get_name()} says: {self._sound} loudly in {self.get_habitat()}"
        def climb(self):
             f"{self._name} climbs the tree for fun while makeing {self._sound}"

def main():
     Airous = Dog("Airous", "the backyard")
     Spooky = Cat("Spooky", "the livingroom")

     print (Airous.speak())
     print(Airous.fetch())

     print (Spooky.speak())
     print (Spooky.climb())
    
if __name__ == "__main__":
     main()