def get_options_ratio (options,total):
    result = options % total
    return result

def main():
    options = input('Enter a Number')
    total = input('Enter a Number')
    result = get_options_ratio(options,total)
    return result
    
main()
    