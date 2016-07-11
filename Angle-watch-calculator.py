# Calculator of angle between hour and minute needle

print("This program indicates the angle between hour and minute needle!. "
      "This program works with 12 hour clock !")

# Error handling code block.
H = 0
M = 0
while 1 >= H <= 12 and 1 >= M <= 60:

    try:
        H = int(input("Please introduce the hour between 1 and 12:"))
        M = int(input("Please introduce the minute between 1 and 60:"))
    except ValueError:
        print("A corresponding number wasn't introduced !")
        continue
    else:
        # everything is ok, even negative numbers can exit the loop ;)
        break
# Check if angle of both is 0 degrees and print it.

H_angle = 360 / 12 * (H % 12)
M_angle = 360 / 60 * (M % 60)
H_angle += (M % 60) / 60 * 360 / 12
angle = (360 + H_angle - M_angle) % 360
if 180 - angle < 0:
    angle = 360 - angle
r = "The angle is: %d" % angle + " degrees !"
print(r)