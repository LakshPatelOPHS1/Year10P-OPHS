rhyme = str(input("Enter a nursery rhyme "))
length = len(rhyme)

print(f"This has {length} of letters in it")

start = int(input("Enter a starting number "))
end = int(input("Enter an ending number "))

rhyme = rhyme[start:end]

print(rhyme)
