import random
from typing import Optional


def generate_table_question(qtype: int, cell: str, other: Optional[str]) -> str:
    if qtype == 1:
        templates = [
            'Do you know the adjacent cell directly above cell [{0}]?',
            'What is the neighboring cell located above cell [{0}]?',
            'Could you identify the adjacent cell positioned above cell [{0}]?',
            'Which cell is immediately adjacent to cell [{0}] above it?',
        ]
        return random.choice(templates).format(cell)

    if qtype == 2:
        templates = [
            'Do you know which cells are located above cell [{0}]?',
            'Could you tell me which cells are above cell [{0}]?',
            'What are the cells located above cell [{0}]?',
            'Can you identify which cells are located above cell [{0}]?',
        ]
        return random.choice(templates).format(cell)

    if qtype == 3:
        templates = [
            'Do you know the adjacent cell directly below cell [{0}]?',
            'What is the neighboring cell located below cell [{0}]?',
            'Could you identify the adjacent cell positioned below cell [{0}]?',
            'Which cell is immediately adjacent to cell [{0}] below it?',
        ]
        return random.choice(templates).format(cell)

    if qtype == 4:
        templates = [
            'Do you know which cells are located below cell [{0}]?',
            'Could you tell me which cells are below cell [{0}]?',
            'What are the cells located below cell [{0}]?',
            'Can you identify which cells are located below cell [{0}]?',
        ]
        return random.choice(templates).format(cell)

    if qtype == 5:
        templates = [
            'Do you know the adjacent cell directly to the left of cell [{0}]?',
            'What is the neighboring cell located to the left of cell [{0}]?',
            'Could you identify the adjacent cell positioned to the left of cell [{0}]?',
            'Which cell is immediately adjacent to cell [{0}] on its left?',
        ]
        return random.choice(templates).format(cell)

    if qtype == 6:
        templates = [
            'Do you know which cells are located to the left of cell [{0}]?',
            'Could you tell me which cells are to the left of cell [{0}]?',
            'What are the cells located to the left of cell [{0}]?',
            'Can you identify which cells are located to the left of cell [{0}]?',
        ]
        return random.choice(templates).format(cell)

    if qtype == 7:
        templates = [
            'Do you know the adjacent cell directly to the right of cell [{0}]?',
            'What is the neighboring cell located to the right of cell [{0}]?',
            'Could you identify the adjacent cell positioned to the right of cell [{0}]?',
            'Which cell is immediately adjacent to cell [{0}] on its right?',
        ]
        return random.choice(templates).format(cell)

    if qtype == 8:
        templates = [
            'Do you know which cells are located to the right of cell [{0}]?',
            'Could you tell me which cells are to the right of cell [{0}]?',
            'What are the cells located to the right of cell [{0}]?',
            'Can you identify which cells are located to the right of cell [{0}]?',
        ]
        return random.choice(templates).format(cell)

    if qtype == 9:
        templates = [
            'Could you tell me which cells are located next to cell [{0}]?',
            'Can you identify the cells that are adjacent to cell [{0}]?',
            'What are the cells that are immediately next to cell [{0}]?',
            'Could you list all the cells that are adjacent to cell [{0}]?',
        ]
        return random.choice(templates).format(cell)

    if qtype == 10:
        templates = [
            'Which cells are in the same row as [{0}] in the table?',
            'Within the table, which cells are horizontally aligned with [{0}]?',
            'Which cells occupy the identical row as [{0}] within the table?',
            'In the table, which cells share the same row as [{0}]?',
        ]
        return random.choice(templates).format(cell)

    if qtype == 11:
        templates = [
            'Which cells are in the same column as [{0}] in the table?',
            'Within the table, which cells are vertically aligned with [{0}]?',
            'Which cells occupy the identical column as [{0}] within the table?',
            'In the table, which cells share the same column as [{0}]?',
        ]
        return random.choice(templates).format(cell)

    if qtype == 12:
        templates = [
            'Could you tell me which header cells are associated with [{0}]?',
            'What are the header cells that correspond to [{0}]?',
            'Which cells serve as the headers for [{0}] in the table?',
            'Which cells act as the headers for [{0}] within the table?',
        ]
        return random.choice(templates).format(cell)

    if qtype == 13:
        templates = [
            'Could you tell me which row header cells are associated with [{0}]?',
            'What are the row header cells that correspond to [{0}]?',
            'Which cells serve as the row headers for [{0}] in the table?',
            'Which cells act as the row headers for [{0}] within the table?',
        ]
        return random.choice(templates).format(cell)

    if qtype == 14:
        templates = [
            'Could you tell me which column header cells are associated with [{0}]?',
            'What are the column header cells that correspond to [{0}]?',
            'Which cells serve as the column headers for [{0}] in the table?',
            'Which cells act as the column headers for [{0}] within the table?',
        ]
        return random.choice(templates).format(cell)

    if qtype == 15:
        templates = [
            'Could you list all the non-header cells that are in the same row as [{0}]?',
            'What are the non-header cells located in the same row as [{0}]?',
            "Can you provide all the non-header cells in [{0}]'s row?",
            'Do you know which non-header cells exist in the row of [{0}]?',
        ]
        return random.choice(templates).format(cell)

    if qtype == 16:
        templates = [
            'Could you list all the non-header cells that are in the same column as [{0}]?',
            'What are the non-header cells located in the same column as [{0}]?',
            "Can you provide all the non-header cells in [{0}]'s column?",
            'Do you know which non-header cells exist in the column of [{0}]?',
        ]
        return random.choice(templates).format(cell)

    if qtype == 17:
        templates = [
            'Between cell [{0}] and cell [{1}], which one comes earlier in the row?',
            'In the row, which cell is positioned before the other: [{0}] or [{1}]?',
            'Which cell is located earlier in the row, cell [{0}] or cell [{1}]?',
            'In the row, is cell [{0}] or cell [{1}] positioned closer to the beginning?',
        ]
        return random.choice(templates).format(cell, other)

    if qtype == 18:
        templates = [
            'Between cell [{0}] and cell [{1}], which one comes later in the row?',
            'In the row, which cell is positioned after the other: [{0}] or [{1}]?',
            'Which cell is located later in the row, cell [{0}] or cell [{1}]?',
            'In the row, is cell [{0}] or cell [{1}] positioned closer to the end?',
        ]
        return random.choice(templates).format(cell, other)

    if qtype == 19:
        templates = [
            'Between cell [{0}] and cell [{1}], which one comes earlier in the column?',
            'In the column, which cell is positioned before the other: [{0}] or [{1}]?',
            'Which cell is located earlier in the column, cell [{0}] or cell [{1}]?',
            'In the column, is cell [{0}] or cell [{1}] positioned closer to the top?',
        ]
        return random.choice(templates).format(cell, other)

    if qtype == 20:
        templates = [
            'Between cell [{0}] and cell [{1}], which one comes later in the column?',
            'In the column, which cell is positioned after the other: [{0}] or [{1}]?',
            'Which cell is located later in the column, cell [{0}] or cell [{1}]?',
            'In the column, is cell [{0}] or cell [{1}] positioned closer to the bottom?',
        ]
        return random.choice(templates).format(cell, other)
