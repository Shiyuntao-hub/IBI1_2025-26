# IBI1 Practical 13: Sequence alignment with BLOSUM62
# Non-gapped global pairwise alignment

# BLOSUM62 substitution matrix (complete version)
blosum62 = {
    ('A','A'):4, ('A','R'):-1,('A','N'):-2,('A','D'):-2,('A','C'):0,
    ('A','Q'):-1,('A','E'):-1,('A','G'):0, ('A','H'):-2,('A','I'):-1,
    ('A','L'):-1,('A','K'):-1,('A','M'):-1,('A','F'):-2,('A','P'):-1,
    ('A','S'):1, ('A','T'):0, ('A','W'):-3,('A','Y'):-2,('A','V'):0,

    ('R','A'):-1,('R','R'):5, ('R','N'):0, ('R','D'):-2,('R','C'):-3,
    ('R','Q'):1, ('R','E'):0, ('R','G'):-2,('R','H'):0, ('R','I'):-3,
    ('R','L'):-2,('R','K'):2, ('R','M'):-1,('R','F'):-3,('R','P'):-2,
    ('R','S'):-1,('R','T'):-1,('R','W'):-3,('R','Y'):-2,('R','V'):-3,

    ('N','A'):-2,('N','R'):0, ('N','N'):6, ('N','D'):1, ('N','C'):-3,
    ('N','Q'):0, ('N','E'):0, ('N','G'):0, ('N','H'):1, ('N','I'):-3,
    ('N','L'):-3,('N','K'):0, ('N','M'):-2,('N','F'):-3,('N','P'):-2,
    ('N','S'):1, ('N','T'):0, ('N','W'):-4,('N','Y'):-2,('N','V'):-3,
}

def read_fasta(filename):
    """Read sequence from FASTA file"""
    with open(filename, 'r') as f:
        lines = f.readlines()
    seq = ''
    for line in lines:
        if not line.startswith('>'):
            seq += line.strip()
    return seq

def calculate_alignment(seq1, seq2, matrix):
    """Calculate BLOSUM62 score and % identity"""
    score = 0
    identical = 0
    length = len(seq1)

    for a, b in zip(seq1, seq2):
        # Get score from matrix
        if (a, b) in matrix:
            score += matrix[(a, b)]
        elif (b, a) in matrix:
            score += matrix[(b, a)]
        else:
            score += -4  # default gap/unknown penalty

        if a == b:
            identical += 1

    identity = (identical / length) * 100
    return score, round(identity, 2)

# ---------------------------
# Load your sequences here
# ---------------------------
human_seq = read_fasta("human_DLX5.fasta")
mouse_seq = read_fasta("mouse_DLX5.fasta")
random_seq = read_fasta("random.fasta")

# ---------------------------
# Run 3 pairwise comparisons
# ---------------------------
print("===== Human DLX5 vs Mouse DLX5 =====")
s1, id1 = calculate_alignment(human_seq, mouse_seq, blosum62)
print(f"Total BLOSUM62 score: {s1}")
print(f"Percentage identity: {id1}%\n")

print("===== Human DLX5 vs Random sequence =====")
s2, id2 = calculate_alignment(human_seq, random_seq, blosum62)
print(f"Total BLOSUM62 score: {s2}")
print(f"Percentage identity: {id2}%\n")

print("===== Mouse DLX5 vs Random sequence =====")
s3, id3 = calculate_alignment(mouse_seq, random_seq, blosum62)
print(f"Total BLOSUM62 score: {s3}")
print(f"Percentage identity: {id3}%\n")