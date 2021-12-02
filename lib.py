import os

def get_input_lines(name, cast_to):
    with open(os.path.join("inputs", name), "r") as f:
        return [cast_to(x) for x in f.readlines()]

