class HotelRoom:
    base_price=2500
    def __init__(self,room_number,guest_name,nights_booked):
        self.room_number=room_number
        self.guest_name=guest_name
        if HotelRoom.is_valid_nights(nights_booked):
            self.nights_booked=nights_booked
        else:
            print("INVALID NUMBER OF NIGHTS! SETTING NIGHTS TO 1")
            self.nights_booked=1
    def total_bill(self):
        return self.nights_booked*HotelRoom.base_price
    @classmethod
    def updating_base_price(cls,new_price):
        cls.base_price=new_price
        print(f"BASE PRICE UPDATED TO {cls.base_price} PER NIGHT")
        print()
    @staticmethod
    def is_valid_nights(nights):
        return isinstance(nights,int) and nights>0
    def display(self):
        print("ROOM NUMBER:",self.room_number)
        print("GUEST NAME:",self.guest_name)
        print("TOTAL NIGHTS:",self.nights_booked)
        print("TOTAL BILL:",self.total_bill())
        print()
s1=HotelRoom(101,"JACKS",5)
s2=HotelRoom(102,"GANESH",4)
s3=HotelRoom(103,"TARUN",-2)
print("INITIAL BOOKINGS:")
print()
s1.display()
s2.display()
s3.display()
HotelRoom.updating_base_price(4000)
print("UPDATED BILLS AFTER BASE PRICE CHANGE:")
print()
s1.display()
s2.display()
s3.display()
print("CHECKING VALID NIGHTS OR NOT:")
print("IS 4 VALID NIGHTS:",HotelRoom.is_valid_nights(4))
print("IS 8 VALID NIGHTS:",HotelRoom.is_valid_nights(8))
print("IS -2 VALID NIGHTS",HotelRoom.is_valid_nights(-2))
