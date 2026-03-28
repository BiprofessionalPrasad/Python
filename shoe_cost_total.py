data=input()
# Split into lines
lines = data.strip().split("\n")

# Line 3 contains how many rows to process
num_lines = int(lines[2])

# Start from line 4, collect the 2nd number from each row for `num_lines` rows
total = 0
for i in range(3, 3 + num_lines):  # lines[3] ... lines[3+num_lines-1]
    parts = lines[i].split()
    total += int(parts[1])

print("Sum =", total)