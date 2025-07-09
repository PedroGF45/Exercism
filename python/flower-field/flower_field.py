def annotate(garden):
    # Validate the input
    if not garden:
        return []

    row_length = len(garden[0])
    for row in garden:
        if len(row) != row_length:
            raise ValueError("The board is invalid with current input.")
        if any(char not in " *" for char in row):
            raise ValueError("The board is invalid with current input.")

    # Helper function to count adjacent flowers
    def count_flowers(x, y):
        directions = [
            (-1, -1), (-1, 0), (-1, 1),
            (0, -1),          (0, 1),
            (1, -1), (1, 0), (1, 1)
        ]
        return sum(
            1
            for dx, dy in directions
            if 0 <= x + dx < len(garden)
            and 0 <= y + dy < len(garden[0])
            and garden[x + dx][y + dy] == "*"
        )

    # Annotate the garden
    return [
        "".join(
            "*" if char == "*" else str(count_flowers(i, j)) if count_flowers(i, j) > 0 else " "
            for j, char in enumerate(row)
        )
        for i, row in enumerate(garden)
    ]

