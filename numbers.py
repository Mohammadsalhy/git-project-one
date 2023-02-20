class Masin_Aval():
    def __init__(self,x):
        self.x = x
        print('Number ',self.x)
    def prime_numbers(self):
        if self.x != 1:
            a = []
            for i in range(1,self.x+1):
                if self.x % i == 0:
                    a.append(i)
                    if i == self.x:
                        if len(a) == 2:
                            print('Number Aval')
                        else:
                            print('Number Composite')
        else:
            print('ahdad = 1')
    def get_retrun_aval(self):
        magmoe_aval = []
        for i in range(1,self.x+1):
            y = []    
            for num in range(1,i+1):
                if i % num == 0:
                    y.append(num)
                    if num == i:
                        if len(y) == 2:
                            magmoe_aval.append(num)
                    if num == self.x:
                        print(magmoe_aval[::-1],', Tedad Ragam Aval %i' % len(magmoe_aval))
    def tedad_argam(self):
        print('tedad argam %i'% (len(str(self.x))))
    def maglob_ahdad(self):
        x = str(self.x)
        reverse_x = int(x[::-1])
        print('Maglob ahdad ',reverse_x)                    