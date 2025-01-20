"""Main entry point for the applciation for Task 1"""

import generator

if __name__ == "__main__":
    ROW_TYPES = ["INT", "STRING", "DATE", "BOOLEAN"]
    CNT_LINES = 25
    FILE_NAME = "generated_file"

    generator.generate_file(FILE_NAME, CNT_LINES, ROW_TYPES)
