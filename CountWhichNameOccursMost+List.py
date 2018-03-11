#['sun','mon','tue','wed','thu','fri','sun','mon','mon']    ('wed', 3)

def mostOccurance(list):
    d={}
    for day in weekdays:
        if day in d:
            d[day] +=1
        else:
            d[day] = 1

    for k, v in d.items():
        return k,max(d.values())


weekdays = ['sun','mon','tue','wed','thu','fri','sun','mon','mon']

print mostOccurance(weekdays)

