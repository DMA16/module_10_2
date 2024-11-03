import multiprocessing
from datetime import datetime


def read_info(name: str):
    all_data = []

    with open(name, 'r') as file:
        while True:
            line = file.readline()

            if not line:
                break




if __name__ == '__main__':
    file_names =  [f'files/file {number}.txt' for number in range(1, 5)]

    #линейный вызов
    start_time = datetime.now()

    for file_name in file_names:
        read_info(file_name)

    end_time = datetime.now()
    print('Время выполнениния линейно:', (end_time - start_time))

    #Многопроссный вызов
    start_proc_time = datetime.now()

    with multiprocessing.Pool() as pool:
        pool.map(read_info, file_names)


    end_proc_time = datetime.now()
    print('Время выполнениния процессов:', (end_proc_time - start_proc_time))