#If structure

canvas_size=float(input("What is the longest side of your canvas?"))
if canvas_size<12:
    print("You have a small sized canvas. ")
elif canvas_size>=12 and canvas_size<=23:
    print("You have a medium sized canvas. ")
else:
    print("You have a large sized canvas. ")