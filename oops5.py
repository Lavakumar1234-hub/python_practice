class Temperature:
    def __init__(self,celsius):
        self.celsius=celsius
    @staticmethod
    def to_fahrenheit(celsius):
        return (celsius*(9/5)+32)
    def show_conversion(self):
        fahrenheit=Temperature.to_fahrenheit(self.celsius)
        print(f"{self.celsius}C")
        print(f"{fahrenheit}F")
ob=Temperature(25)
ob.show_conversion()
