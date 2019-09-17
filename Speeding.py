class HighSpeed(object):
    
    def Speeding(self, x):
        if x <= 50:
            return "Pass"
            print("Pass")
        elif x <= 55:
            return "10 euros"
            print("10 euros")
        elif x <= 60:
            return "20 euros"
            print("20 euros")
        elif x <= 65:
            print("30 euros")
            return "30 euros"
        elif x <= 70:
            print("40 euros")
            return "40 euros"
        elif x <= 75:
            print("50 euros")
            return "50 euros"
        elif x <= 80:
            print("60 euros")
            return "60 euros"
        else:
            return "Goodbye License"
            print("Goodbye License")
            

