# write a function that accepts an encoded string as a parameter. This string will contain a first name, last name and an id. Values in the string can be separated by any number of zeros. The function should parse the string and return a Python dictionary that contains the first name, last name and id values. An example input would be "Rovert000Smith000123". The function should return the following using that input:
# {"first_name":"Robert","last_name":"Smith", "id":"123"}

txt = "Robert000Smith000123"


def decodd(txt):
    x = txt.split("0")
    for i in x:
        if i == '':
            x.remove('')
        if i == '':
            x.remove('')

    # return x
    basic_li = ["First_name", "Last_name", "id"]
    store1 = {}
    for key in basic_li:
        for value in x:
            store1[key] = value
            x.remove(value)
            break
    
    print(store1)



decodd(txt)
