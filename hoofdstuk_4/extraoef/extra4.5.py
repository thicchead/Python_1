eerste_term = 1
tweede_term = 1

maximum = 1500

while tweede_term < maximum:
    print(eerste_term)
    print(tweede_term)

    eerste_term += tweede_term
    tweede_term += eerste_term
