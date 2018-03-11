#program to find birthday based on name
birthdate ={
    'pink':'24-4-2000',
    'xxx':'23-4-5000'
}

# print (birthdate)             #{'xxx': '23-4-5000', 'pink': '24-4-2000'}

#print (birthdate['xxx'])        # 23-4-5000

name= raw_input("Please enter:")

if name in birthdate:
    print(birthdate[name])

