class PhoneNumber:
    def __init__(self, number):
        remove = [" ","(",")","-",".","+"]
        output = number
        for character in remove:
            output = output.replace(character,"")
        if len(output)==11 and output[0]=="1":
            output = output[1:]
        if len(output)>10:
            raise ValueError("More than 10 digits supplied (or 11 digit number where first digit is not 1)")
        if output[0]=="0" or output[0]=="1":
            raise ValueError("First digit of area code cannot be 0 or 1.")
        if output[3]=="0" or output[3]=="1":
            raise ValueError("First digit of exchange code cannot be 0 or 1.")
        self.number = output
        self.area_code = output[0:3]
    def pretty(self):
        return f"({self.area_code}) {self.number[3:6]}-{self.number[6:]}"