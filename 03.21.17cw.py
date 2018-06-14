def hanoi(n, start, temp, end):
    if n > 0:
        hanoi (n-1, start, end, temp)
        print "move from " + start + " to " + end
        hanoi (n-1, temp, start, end)
