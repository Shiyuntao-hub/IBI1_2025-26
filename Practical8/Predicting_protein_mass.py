def calculate_protein_mass(sequence):
    # Create a dictionary for amino acid mass values
    aa_mass = {
        'G': 57.02, 'A': 71.04, 'S': 87.03, 'P': 97.05,
        'V': 99.07, 'T': 101.05, 'C': 103.01, 'I': 113.08,
        'L': 113.08, 'N': 114.04, 'D': 115.03, 'Q': 128.06,
        'K': 128.09, 'E': 129.04, 'M': 131.04, 'H': 137.06,
        'F': 147.07, 'R': 156.10, 'Y': 163.06, 'W': 186.08
    }

    total_mass = 0.0

    # Loop through each character in the sequence
    for aa in sequence:
        # Check if the amino acid is valid
        if aa not in aa_mass:
            raise ValueError(f"Invalid amino acid detected: {aa}")
        # Add mass to total
        total_mass += aa_mass[aa]

    return total_mass

# Example usage
if __name__ == "__main__":
    test_sequence = "GASPV"
    result = calculate_protein_mass(test_sequence)
    print(f"Sequence: {test_sequence}")
    print(f"Total mass: {result:.2f} amu")