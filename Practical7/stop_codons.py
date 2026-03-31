# Practical 7 Task 2: Stop Codon Analysis (Strict Header Format)
# Filename: stop_codons.py
def parse_fasta(fasta_path):
    """
    Parse FASTA file to extract gene names (only the first token in header) and full sequences.
    Returns: dict {gene_name: full_sequence}
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
                
                # Extract ONLY the gene name (first element after >, no extra info)
                header = line.lstrip('>')
                current_gene = header.split()[0]  # Strict: only gene name (e.g., YAL001C)
                current_seq = []
            else:
                # Combine multi-line sequences (uppercase for consistency)
                current_seq.append(line.upper())
    
    # Add the last gene
    if current_gene and current_seq:
        gene_data[current_gene] = ''.join(current_seq)
    
    return gene_data

def get_in_frame_stop_codons(dna_seq):
    """
    Find ALL unique stop codons (TAA/TAG/TGA) present in-frame (after ATG start).
    Returns: sorted list of stop codons (empty if none)
    """
    start_codon = 'ATG'
    stop_codons = {'TAA', 'TAG', 'TGA'}
    found_stops = set()

    # Find all ATG start positions
    for start_pos in range(len(dna_seq) - 2):
        if dna_seq[start_pos:start_pos+3] == start_codon:
            # Read codons in frame (3 nucleotides per step)
            for i in range(start_pos, len(dna_seq) - 2, 3):
                codon = dna_seq[i:i+3]
                if codon in stop_codons:
                    found_stops.add(codon)
    
    return sorted(found_stops)  # Sorted for consistent output

def generate_stop_genes_fasta(input_fasta, output_fasta='stop_genes.fa'):
    """
    Main function: Filter genes with in-frame stop codons and write to output FASTA.
    Headers contain ONLY gene name + stop codons (no extra text).
    """
    # Step 1: Parse input FASTA
    try:
        gene_dict = parse_fasta(input_fasta)
    except FileNotFoundError:
        print(f"Error: Input file '{input_fasta}' not found!")
        return
    
    # Step 2: Filter genes with stop codons
    filtered_genes = {}
    for gene, seq in gene_dict.items():
        stop_list = get_in_frame_stop_codons(seq)
        if stop_list:  # Only keep genes with at least one stop codon
            filtered_genes[gene] = stop_list
    
    # Step 3: Write output (strict header format)
    with open(output_fasta, 'w', encoding='utf-8') as f:
        for gene, stops in filtered_genes.items():
            # Header: ONLY gene name + stop codons (comma-separated)
            header = f">{gene} {' '.join(stops)}"  # e.g., >YAL001C TAA or >YAL002W TAG TGA
            # Write header and sequence (wrap to 80 chars for FASTA standard)
            f.write(f"{header}\n")
            for i in range(0, len(gene_dict[gene]), 80):
                f.write(f"{gene_dict[gene][i:i+80]}\n")
    
    print(f"Success! Output file: {output_fasta}")
    print(f"Number of genes with stop codons: {len(filtered_genes)}")

# Run the script (update the input path to your FASTA file)
if __name__ == "__main__":
    INPUT_FASTA = "Saccharomyces_cerevisiae.R64-1-1.cdna.all.fa"  # Replace with your file path
    generate_stop_genes_fasta(INPUT_FASTA)