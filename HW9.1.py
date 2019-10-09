print("")
print ("  Program pretvarja število km v milje  ")
print("-----------------------------------------")

print("")
kilometri = input("Vnesi število km: ")

print("")
print("REZULTAT:")
print(kilometri + " km je " + str(int(kilometri) * 2) + " milj.")
dela = input("Želiš nadaljevati [d/n]: ")

if dela == "n":
    print("")
    print("*** END ***")
else:
    while dela == "d":
        print("")
        kilometri = input("Vnesi število km: ")
        print("")
        print("REZULTAT:")
        print(kilometri + " km je " + str(int(kilometri) * 2) + " milj.")
        print("")
        dela = input("Želiš nadaljevati [d/n]: ")
    print("")
    print("*** END ***")