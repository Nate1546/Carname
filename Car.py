class Car(object):
    def __init__ (self,model,carcolor,speed_limit,company):
        self.carcolor = carcolor 
        self.speed_limit= speed_limit
        self.company = company
        self.model = model
        
    def start(self):
        print('started') 
    
    def stop(self):
        print('stop')

    def accelerate(self):
        print('accelerate')

    def changegear(self):
        print('gear changed')

audi = Car('A6','black','5','audi')
Mac = Car('Macantosh','blue','sdd','disk_bandwidth 1tb')

audi.start()
Mac.start()
    