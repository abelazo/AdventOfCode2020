
# byr (Birth Year)
# iyr (Issue Year)
# eyr (Expiration Year)
# hgt (Height)
# hcl (Hair Color)
# ecl (Eye Color)
# pid (Passport ID)
# cid (Country ID)
optional_sections = ['cid']
required_sections = ['byr', 'iyr', 'eyr', 'hgt', 'hcl', 'ecl', 'pid']

def per_section(it, is_delimiter=lambda x: x.isspace()):
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

def getPassports(file):
    with open(file) as f:
        sections = list(per_section(f))
    return sections     

def formatPassports(raw_passports):
    passports=[]
    for passport in raw_passports:
        flat_passport = " ".join(passport)
        passports.append(dict(item.split(":") for item in flat_passport.split(" ")))
    return passports

passports=formatPassports(getPassports('Passports.txt'))

for passport in passports:
     if all(x in passport.keys() for x in required_sections):
         print('Valid: {}'.format(passport))
     else:
         print('Invalid: {}'.format(passport))
