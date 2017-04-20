start = input("What number should I start on?: ")
end = input("What number should I end on?: ")
count = int(start) - 1
for x in range(int(start), int(end)):
    while count < int(end):
        count += 1
        print(count)
