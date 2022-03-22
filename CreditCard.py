import datetime

class CreditCardValidator:
    
    def validate_card_num(self, card_num):

        def checkLuhn(cardNo):

            nDigits = len(cardNo)
            nSum = 0
            isSecond = False
            
            for i in range(nDigits - 1, -1, -1):
                d = ord(cardNo[i]) - ord('0')

                if (isSecond == True):
                    d = d * 2
                
                nSum += d // 10
                nSum += d % 10
                isSecond = not isSecond

            if (nSum % 10 == 0):
                return True
            else:
                return False

        return checkLuhn(card_num)


    def validate_card_holder_name(self, card_holder_name):
        
        #Name should not startwith or ends with space.
        if card_holder_name.endswith(" ") or card_holder_name.startswith(" "):
            return False
        
        #Name should not contain special character or number.
        for char in card_holder_name:
            if not char.isalpha() and not char.isspace():
                return False
        
        return True


    def validate_card_validity(self, card_validity):

        #Validity date must be less than the today date.

        today = datetime.datetime.now()

        mon = int(card_validity[:2])
        year = int("20" + card_validity[-2:])

        if today.year > year:
            return False
        if today.year == year and today.month > mon:
            return False
        return True

    def validate_card_cvv(self, cvv):

        #CVV num should be of length 3 or 4.
        #Should contain only numbers.
        if not cvv.isdecimal():
            return False
        
        if len(cvv) != 3 and len(cvv) != 4:
            return False
        
        return True


    def validate(self, card_num, name, validity, cvv):

        #Card is valid card if all above validations are true.
        if not self.validate_card_num(card_num) or not self.validate_card_holder_name(name) or not self.validate_card_validity(validity) or not self.validate_card_cvv(cvv):
            return False
        
        return True

    