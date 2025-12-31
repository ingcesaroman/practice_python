dna_1 = "ACCGTT"
dna_2 = "CCAGCA"

def longest_common_subsequence(string_1, string_2):
    print("Finding longest common subsequence of {0} and {1}".format(string_1, string_2))

    # Initialize a grid with dimensions (len(string_2) + 1) x (len(string_1) + 1)
    grid = [[0 for _ in range(len(string_1) + 1)] for _ in range(len(string_2) + 1)]

    # Fill the grid
    for row in range(1, len(string_2) + 1):
        for col in range(1, len(string_1) + 1):
            if string_1[col - 1] == string_2[row - 1]:
                grid[row][col] = grid[row - 1][col - 1] + 1
            else:
                grid[row][col] = max(grid[row - 1][col], grid[row][col - 1])

    # Print the completed grid
    print("\nCompleted Grid:")
    for row_line in grid:
        print(row_line)

    # Reconstruct the LCS
    lcs_string = ""
    row = len(string_2)
    col = len(string_1)

    while row > 0 and col > 0:
        if string_1[col - 1] == string_2[row - 1]:
            lcs_string = string_1[col - 1] + lcs_string
            row -= 1
            col -= 1
        elif grid[row - 1][col] > grid[row][col - 1]:
            row -= 1
        else:
            col -= 1
            
    # The length of the LCS is at grid[-1][-1]
    print(f"\nLCS length: {grid[-1][-1]}")
    print(f"LCS string: {lcs_string}")
    return lcs_string

# Call the function with the defined DNA strings
result_lcs = longest_common_subsequence(dna_1, dna_2)
print(f"Result for dna_1 and dna_2: {result_lcs}")

# Test with the example from the problem description: "ABAZDC" and "BACBAD"
print("\nTesting with example strings: 'ABAZDC' and 'BACBAD'")
longest_common_subsequence("ABAZDC", "BACBAD")

