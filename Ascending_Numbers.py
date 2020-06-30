def ascending(txt):
    for i in range(1, len(txt)):
        numbers = int(txt[:i])
        new_numbers = str(numbers)
        if len(txt) % len(new_numbers):
            continue
        while len(new_numbers) < len(txt):
            numbers += 1
            new_numbers += str(numbers)
            if new_numbers == txt:
                return True
    return False

print(ascending("57585960616263"))
