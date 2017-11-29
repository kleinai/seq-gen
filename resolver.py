"""
Inverse codon map. Synonymous codons should be in a list
"""
inverse_codon_map = {
    "T": ["ACA"]
}


class UnmappedProteinError(Exception):
    pass


def generate_sequences(sequence: list) -> list:
    """
    Generates a list of DNA sequences from a given protein sequence
    """
    sub_sequences = ['']
    if len(sequence) > 1:
        sub_sequences = generate_sequences(sequence[:-1])
    gen_sequences = []
    for codon in inverse_codon_map[sequence[0]]:
        for sub_sequence in sub_sequences:
            gen_sequences.append(codon + sub_sequence)
    return gen_sequences

if __name__ == '__main__':
    proteins = input("Proteins (single letter notation)> ")
    proteins = [p for p in list(proteins.upper()) if p in inverse_codon_map.keys()]
    possible_sequences = generate_sequences(proteins)
    for i in range(len(possible_sequences)):
        print(possible_sequences[i-1])
