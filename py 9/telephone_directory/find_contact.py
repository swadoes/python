def find_contact(word, data):

    if len(data) != 0:

        dat = []
        for item in data:
            if word in item:
                temp = item
                dat.append(temp)
        return dat
    else:
        return None
    return dat
