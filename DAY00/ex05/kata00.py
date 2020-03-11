t = (19, 42, 21)
j = 0
while (j < len(t)):
    if not isinstance(t[j], int):
        exit(print("Not a number: %s" % t[j]))
    j += 1
if (isinstance(t, int)):
    exit(print("The number is: {}".format(t)))
else:
    s = "{}".format(t[0])
    i = 1
    while (i < len(t)):
        s = s + ", {}".format(t[i])
        i += 1
(print("The", len(t), "numbers are:", "%s" % s))
