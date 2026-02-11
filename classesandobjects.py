class Car:
      def __init__(self,brand,engine,speed):
        self.brand = brand
        self.engine = engine
        self.speed = speed
      def display(self):
        print(self.brand, self.engine, self.speed)
        
      def start(self):
        print(self.brand,"started")
        
car1 = Car("BMW","abc","233")
car2 = Car("abg","wer","234")
car1.display()
car2.display()
car1.start()