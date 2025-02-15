

def get_options_ratio (options, total):
    result = options % total
    
    return result


def get_faculty_rating(result):
    if (result <= 1 and result >= .9):
        return 'Excellent'
    if (result < .9 and result >= .8):
        return 'Very Good'
    if (result < .8 and result >= .7):
        return 'Good'
    if (result < .7 and result >= .6):
        return 'Needs Improvement'
    if (result < .6 and result >= 0):
        return 'Unacceptable'