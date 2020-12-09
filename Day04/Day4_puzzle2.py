import re

# byr (Birth Year)
# iyr (Issue Year)
# eyr (Expiration Year)
# hgt (Height)
# hcl (Hair Color)
# ecl (Eye Color)
# pid (Passport ID)
# cid (Country ID)
optional_sections = ['cid']

class ValidatedField:

    def __init__(self, value):
        self._value = value
        
    def __repr__(self):
        return self._value
    def __str__(self):
        return self._value

    def validate(self) -> bool:
        pass

class BirthYear(ValidatedField):
    def validate(self) -> bool:
        """byr (Birth Year) - four digits; at least 1920 and at most 2002."""
        try:
            int_value=int(self._value)
        except ValueError:
            return False

        res = (1920 <= int_value) and (int_value <= 2020)
        #print("  - {}: {}".format(self._value,res))
        return res

class IssueYear(ValidatedField):
    def validate(self) -> bool:
        """iyr (Issue Year) - four digits; at least 2010 and at most 2020"""
        try:
            int_value=int(self._value)
        except ValueError:
            return False

        res = (2010 <= int_value) and (int_value <= 2020)
        #print("  - {}: {}".format(self._value,res))
        return res

class ExpirationYear(ValidatedField):
    def validate(self) -> bool:
        """eyr (Expiration Year) - four digits; at least 2020 and at most 2030."""
        try:
            int_value=int(self._value)
        except ValueError:
            return False

        res = (2020 <= int_value) and (int_value <= 2030)
        #print("  - {}: {}".format(self._value,res))
        return res

class Height(ValidatedField):
    def validate(self) -> bool:
        """hgt (Height) - a number followed by either cm or in: """
        """ If cm, the number must be at least 150 and at most 193."""
        """ If in, the number must be at least 59 and at most 76."""
        res = False
        if self._value.endswith("cm"):
            try:
                number=int(self._value[0:-2:])
            except ValueError:
                return False
            res = (150 <= number) and (number <= 193)
        elif (self._value.endswith("in")):
            try:
                number=int(self._value[0:-2:])
            except ValueError:
                return False
            res = (59 <= number) and (number <= 76)
        #print("  - {}: {}".format(self._value,res))
        return res
    
class HairColor(ValidatedField):
    def validate(self) -> bool:
        """hcl (Hair Color) - a # followed by exactly six characters 0-9 or a-f."""
        p = re.compile('^#([0-9]|[a-f]){6}$')
        res = (p.match(self._value) != None)
        #print("  - {}: {}".format(self._value,res))
        return res

class EyeColor(ValidatedField):
    def validate(self) -> bool:
        """ecl (Eye Color) - exactly one of: amb blu brn gry grn hzl oth."""
        res = self._value in ['amb', 'blu', 'brn', 'gry', 'grn', 'hzl', 'oth']
        #print("  - {}: {}".format(self._value,res))
        return res

class PassportId(ValidatedField):
    def validate(self) -> bool:
        """pid (Passport ID) - a nine-digit number, including leading zeroes."""
        res = (len(self._value) == 9) and (self._value.isnumeric())
        #print("  - {}: {}".format(self._value,res))
        return res

class CountryId(ValidatedField):
    def validate(self) -> bool:
        """cid (Country ID) - valid."""
        res = True
        #print("  - {}: {}".format(self._value,res))
        return res
    
class Parser:

    def __init__(self, filename):
        self.filename = filename
        self.__optional_sections = {
            'cid': CountryId
        }
        self.__required_sections = {
            'byr': BirthYear,
            'iyr': IssueYear,
            'eyr': ExpirationYear,
            'hgt': Height,
            'hcl': HairColor,
            'ecl': EyeColor,
            'pid': PassportId
        }
    
    def getPassports(self):
        with open(self.filename) as f:
            sections = list(self.__per_section(f))
            return self.__formatPassports(sections)

    def catalog(self) -> list:
        complete_passports = []
        for passport in passports:
            if all(x in passport.keys() for x in self.__required_sections.keys()):
                #print('Valid for catalog: {}'.format(passport))
                complete_passports.append([self.__make(key,value) for key,value in passport.items()])
                #complete_passports.append([self.__make(i) for i in passport.keys()])
            else:
                pass
                #print('Invalid for catalog: {}'.format(passport))
        return complete_passports
        
    def __make(self,key,value):
        choices = {**self.__required_sections, **self.__optional_sections}
        cls = choices[key]
        return cls(value)

    def __per_section(self, it, is_delimiter=lambda x: x.isspace()):
        ret = []
        for line in it:
            if is_delimiter(line):
                if ret:
                    yield ret  # OR  ''.join(ret)
                    ret = []
            else:
                ret.append(line.rstrip())  # OR  ret.append(line)
        if ret:
            yield ret

    def __formatPassports(self, raw_passports):
        passports=[]
        for passport in raw_passports:
            flat_passport = " ".join(passport)
            passports.append(dict(item.split(":") for item in flat_passport.split(" ")))
        return passports

parser=Parser('Passports.txt')
passports=parser.getPassports()

for passport in parser.catalog():
    if all(field.validate() for field in passport):
        print("Valid - {}".format(passport))
    else:
        print("Invalid - {}".format(passport))

