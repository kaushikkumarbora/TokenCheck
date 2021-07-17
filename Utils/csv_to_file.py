import os

j=0
csvfile = '/home/shepard/Project/2.csv'
# csvfile = str(i+1) + '.csv'
with open(csvfile, 'r') as csvfile:
    # reader = csv.DictReader(csvfile)
    reader = csvfile.read().splitlines()


for row in reader:
    if row != 'bytecode':
        file_name = '{0}.txt'.format(j)
        file_name = os.path.join('/home/shepard/Project/bc_project/mythril/Input', file_name)
        print(file_name)

        with open(file_name, 'w') as f:
            f.write(row)
        j += 1
