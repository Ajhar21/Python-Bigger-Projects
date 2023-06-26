import random

class BRTA:
    def __init__(self) -> None:
        self.__license={}
    
    def take_driving_test(self, email):
        self.email=email
        score=random.randint(0,100)
        if score >= 33:
            # print('Congrats! You have passed', score)
            license_number=random.randint(5000,9999)
            self.__license[self.email]=license_number
            return license_number
        else:
            # print('Sorry! You have failed', score)
            return False
    
    def validate_license(self, email, license_num):
        for mail, l_num in self.__license.items():
            if email==mail and license_num==l_num:
                # print('Valid Driver')
                return True
        return False
    
# license_authority=BRTA()
# result=license_authority.validate_license('kuber', 3456)
# print(result)


