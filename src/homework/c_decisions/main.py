from c_decisions import decision
from c_decisions.decision import get_faculty_rating, get_options_ratio

def main():
    result = decision.get_options_ratio(float(input('enter a value:')),float(input('enter a value')))
    print (result)

    print (get_faculty_rating(result))

main()
