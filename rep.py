
def rego():
    input_str, consecuitive_runs = input().split()
    consecuitive_runs = int(consecuitive_runs)


    # char can repeat consecuitive_runs times continuously
    char_under_review = ''
    times_encountered = 0
    new_str = ''
    for current in input_str:
        if times_encountered == 0:  # initial case
            char_under_review = current
            times_encountered += 1
        elif char_under_review == current:
            times_encountered += 1
        else:
            char_under_review = current
            times_encountered = 1  # reset
        if times_encountered <= consecuitive_runs:
            new_str += char_under_review


    print(new_str)

rego()

    










#aban 2