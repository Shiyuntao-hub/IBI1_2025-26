#Practical 7: Finding the largest opening reading frame (ORF) in a DNA sequence

def find_longest_orf(sequence):
    """
    Find the largest opening reading frame (ORF) in a given mRNA sequence.
    ORF starts with a start codon (AUG) and ends with a stop codon (UAA, UAG, UGA).
    """
    start_codon = "AUG"
    stop_codons = {"UAA", "UAG", "UGA"}
    longest_orf = ""

   # Search all possible start positions
    for i in range(len(sequence) - 2):
        if sequence[i:i+3] == start_codon:
            current_orf = ""
            # Read codons in triplets
            for j in range(i, len(sequence) - 2, 3):
                codon = sequence[j:j+3]
                current_orf += codon
                # Stop when a stop codon is found
                if codon in stop_codons:
                    if len(current_orf) > len(longest_orf):
                        longest_orf = current_orf
                    break
    return longest_orf, len(longest_orf)

# Define the given mRNA sequence
seq = 'AAGAUACAUGCAAGUGGUGUGUCUGUUCUGAGAGGGCCUAAAAG'

# Run the function
longest_orf, orf_length = find_longest_orf(seq)

# Display results
print("Original mRNA sequence:", seq)
print("-" * 60)
print("Longest ORF sequence:", longest_orf)
print("Length of the longest ORF (nucleotides):", orf_length)

