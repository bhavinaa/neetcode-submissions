class Seniors:
    
    def __init__(phoneNumber, gender, age, seat):
        self.phoneNumber = phoneNumber
        self.gender = gender 
        self.age = int(age)
        self.seat = seat
    
    
class Solution:
    def countSeniors(self, details: List[str]) -> int:
        count = 0 
        # 10 c = phone number
        # 1 c = gender
        # 2 c = age
        # 2 c = seat
        for i in range(0, len(details)):
            age = details[i][11:13]
          
            if int(age) > 60:
                count = count + 1
        return count

