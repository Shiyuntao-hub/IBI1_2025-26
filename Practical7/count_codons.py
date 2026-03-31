# Practical 7 Task 3: Codon Frequency Analysis for Stop Codon Upstream Regions
# Filename: count_codons.py
import re
import matplotlib.pyplot as plt
from collections import Counter

# Set matplotlib to use non-interactive backend (saves plot to file instead of displaying)
plt.switch_backend('Agg')

def parse_fasta(fasta_path):
    """
    Parse FASTA file to extract gene names and full sequences (handles multi-line sequences).
    Returns: dict {gene_name: full_DNA_sequence}
    """
    gene_data = {}
    current_gene = None
    current_seq = []

    with open(fasta_path, 'r', encoding='utf-8') as f:
        for line in f:
            line = line.strip()
            if not line:
                continue
            
            if line.startswith('>'):
                # Save previous gene data
                if current_gene and current_seq:
                    gene_data[current_gene] = ''.join(current_seq)
                
                # Extract only gene name (first token in header)
                current_gene = line.lstrip('>').split()[0]
                current_seq = []
            else:
                # Combine multi-line sequences (uppercase for consistency)
                current_seq.append(line.upper())
    
    # Add the last gene to the dictionary
    if current_gene and current_seq:
        gene_data[current_gene] = ''.join(current_seq)
    
    return gene_data

def find_longest_orf_for_stop(sequence, target_stop):
    """
    Find the longest ORF ending with the target stop codon (TAA/TAG/TGA).
    Returns: list of codons in the longest ORF (excluding the stop codon itself)
    """
    start_codon = 'ATG'
    stop_codon = target_stop
    all_valid_orfs = []

    # Find all ATG start positions
    start_positions = [m.start() for m in re.finditer(start_codon, sequence)]
    
    for start_pos in start_positions:
        # Read codons in frame from start position
        codons = []
        for i in range(start_pos, len(sequence) - 2, 3):
            codon = sequence[i:i+3]
            if codon == stop_codon:
                # Add ORF (codons before stop codon) to list if valid
                if codons:  # Ensure ORF has at least one codon before stop
                    all_valid_orfs.append(codons)
                break
            codons.append(codon)
    
    # Return the longest ORF (codons only) if any exist
    if all_valid_orfs:
        return max(all_valid_orfs, key=len)
    return []

def analyze_codon_frequency(input_fasta, target_stop):
    """
    Main analysis function:
    1. Filter genes with the target stop codon in-frame
    2. For each gene, get codons from the longest ORF ending with target stop
    3. Count codon frequencies and generate pie chart
    """
    # Step 1: Validate input stop codon
    valid_stops = {'TAA', 'TAG', 'TGA'}
    if target_stop not in valid_stops:
        print(f"Error: Invalid stop codon! Only {', '.join(valid_stops)} are allowed.")
        return None
    
    # Step 2: Parse FASTA file
    try:
        gene_dict = parse_fasta(input_fasta)
        print(f"Parsed {len(gene_dict)} genes from FASTA file")
    except FileNotFoundError:
        print(f"Error: FASTA file '{input_fasta}' not found!")
        return None
    
    # Step 3: Collect codons from genes with target stop codon
    all_codons = []
    genes_with_stop = 0

    for gene_name, sequence in gene_dict.items():
        # Get codons from longest ORF ending with target stop
        orf_codons = find_longest_orf_for_stop(sequence, target_stop)
        if orf_codons:
            genes_with_stop += 1
            all_codons.extend(orf_codons)
    
    if not all_codons:
        print(f"No genes found with in-frame {target_stop} stop codon")
        return None
    
    # Step 4: Count codon frequencies
    codon_counts = Counter(all_codons)
    print(f"\nAnalysis Results for Stop Codon: {target_stop}")
    print(f"Number of genes with {target_stop}: {genes_with_stop}")
    print(f"Total codons analyzed: {len(all_codons)}")
    print("\nTop 10 Most Frequent Codons:")
    for codon, count in codon_counts.most_common(10):
        print(f"{codon}: {count} ({count/len(all_codons)*100:.2f}%)")
    
    # Step 5: Generate and save pie chart (clear labels, readable format)
    # Limit to top 10 codons + "Other" for readability
    top_codons = codon_counts.most_common(10)
    other_count = sum(codon_counts.values()) - sum([count for _, count in top_codons])
    
    labels = [codon for codon, _ in top_codons] + ['Other']
    sizes = [count for _, count in top_codons] + [other_count]
    colors = plt.cm.Set3(range(len(labels)))  # Color palette for readability
    
    # Create plot
    plt.figure(figsize=(12, 8))
    plt.pie(sizes, labels=labels, autopct='%1.1f%%', startangle=90, colors=colors)
    plt.title(f"Codon Frequency Distribution (Upstream of {target_stop})", fontsize=14)
    plt.axis('equal')  # Ensure pie chart is circular
    
    # Save plot to file (PNG format, high resolution)
    plot_filename = f"{target_stop}_codon_frequency.png"
    plt.tight_layout()
    plt.savefig(plot_filename, dpi=300, bbox_inches='tight')
    plt.close()
    
    print(f"\nPie chart saved as: {plot_filename}")
    return codon_counts

# --------------------------
# User Input & Execution
# --------------------------
if __name__ == "__main__":
    # Update this path to your yeast cDNA FASTA file
    FASTA_FILE_PATH = "Saccharomyces_cerevisiae.R64-1-1.cdna.all.fa"
    
    # Get valid stop codon input from user
    while True:
        user_input = input("Enter a stop codon (TAA/TAG/TGA): ").strip().upper()
        if user_input in {'TAA', 'TAG', 'TGA'}:
            break
        print("Invalid input! Please enter only TAA, TAG, or TGA.")
    
    # Run the analysis
    analyze_codon_frequency(FASTA_FILE_PATH, user_input)