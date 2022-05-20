def get_declension_year(age):
    if age % 10 == 1 and age % 100 != 11:
        return "год"
    elif age % 10 == 1 or age % 10 == 2 or age % 10 == 3 or age % 10 == 4:
        if age % 100 // 10 == 1:
            return "лет"
        else:
            return "года"
    else:
        return "лет"
        