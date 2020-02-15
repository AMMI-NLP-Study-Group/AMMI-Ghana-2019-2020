
import os


def read_file(file_path):
        x = []
        y = []
        lines = open(file_path).readlines()

        for i in range(len(lines)):
                reading = lines[i].strip().split(';')
                x.append(reading[0])
                y.append(reading[1])

        return {'input':x, 'output': y}

# def get_vocab

print(read_file("./Data/worked_example.train"))