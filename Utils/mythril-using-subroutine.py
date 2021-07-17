import subprocess
import time
import os
import concurrent.futures
start_time = time.time()

input_folder = r'/home/shepard/Project/bc_project/mythril/Input/'
output_accepted = os.path.join(input_folder, 'Accepted')
output_rejected = os.path.join(input_folder, 'Rejected')

try:
    os.mkdir(output_accepted)
    os.mkdir(output_rejected)
except:
    print('Folder already created.')


def call_mythril(fn):
    base_name = os.path.basename(fn)
    result = subprocess.run(['python3', '-m', 'mythril', 'a', '-f', fn], stdout=subprocess.PIPE).stdout.decode('utf-8')
    if 'No issues were detected.' in result:
        os.replace(fn, os.path.join(output_accepted, base_name))
        print(base_name, 'is fine.')
    elif  'Transaction Sequence' in result:
        os.replace(fn, os.path.join(output_rejected, base_name))
        print(base_name, 'has some error.')
    else:
        print(base_name, result, '--------------------------------------------------------------------------------', sep='\n')

def intify(i):
    res = int(i.split('.')[0])
    return res


def main():
    temp_list = [i for i in os.listdir(input_folder)[:2000] if i.endswith('.txt')]
    temp_list.sort(key=intify)

    with concurrent.futures.ProcessPoolExecutor(max_workers=None) as executor:
        Futures = {executor.submit(
            call_mythril, os.path.join(input_folder, i)) for i in temp_list}

    concurrent.futures.wait(Futures)


if __name__ == "__main__":
    main()
    print("--- %s seconds ---" % (time.time() - start_time))
