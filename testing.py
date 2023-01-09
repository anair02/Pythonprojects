
def grades(tests):
    x = sum(tests)
    y = x/len(tests)
    if y >= 80:
      print ("You get a A")
    elif y >= 60 and y < 80:
      print ("You get a B")
    elif y < 60 and y >= 50:
      print("You get a C")
    else:
        print("You get an F")

marks = [55,65,75,80,65]
grades(marks)

