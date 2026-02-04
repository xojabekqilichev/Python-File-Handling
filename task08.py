input_f = "Input/numbers.txt"
output = "Output/output08.txt"
with open(input_f, 'r') as file:
        data = file.read().split()
with open(output, 'w') as out_file:
    count = 0
    for item in data:
        number = int(item)
        if number % 5 == 0:
            out_file.write(f"{number}\n")
            print(f"Topildi: {number}")
            count += 1
        print(count)