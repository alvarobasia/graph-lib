from typing import List


def get_correct_values(values: List[str]):
    result = []

    for value in values:
        new_line = []
        for number_in_string in value.split(" "):
            new_line.append(int(number_in_string))
        result.append(new_line)

    obj = {}
    obj['nodes'] = result[0][0]
    obj['edges'] = result[0][1]
    obj['values'] = result[1:]
    return obj
