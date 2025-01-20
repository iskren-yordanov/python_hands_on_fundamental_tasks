"""Generative functions depending on the type needed"""

import gen_functions

def generate_line(lst: list) -> str:
    """Generate a string line based on a list of types"""
    final_output = ""
    for s in lst:
        if s == "BOOLEAN":
            final_output += f'"{gen_functions.generate_boolean()}"'

        if s == "INT":
            final_output += f'"{gen_functions.generate_int(100, False)}"'

        if s == "STRING":
            final_output += f'"{gen_functions.generate_string(45)}"'

        if s == "FLOAT":
            final_output += f'"{gen_functions.generate_float(4)}"'

        if s == "DATE":
            final_output += f'"{gen_functions.generate_date()}"'

        final_output += ","

    final_output = final_output[::-1].replace(",","",1)
    final_output = final_output[::-1]

    return final_output

def generate_file(f_name: str, lines_cnt: str, line_struture: list) -> None:
    """Generate a file with random data"""
    with open(f"task1/{f_name}.csv", "w",encoding="UTF8") as f:

        for _ in range(lines_cnt):
            f.write(generate_line(line_struture))
            f.write("\n")
