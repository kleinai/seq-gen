"""
Inverse codon map. Synonymous codons should be in a list
"""
inverse_codon_map = {
    "T": ["ACA"]
}


class UnmappedProteinError(Exception):
    pass


"""
Returns the probability of a given codon in the sequence given the entire sequence
"""
def compute_codon_probability(index, protein_sequence):
    return 1


"""
Returns the number of possible sequences
"""
def count_possible_sequences(sequence):
    num_possible = 1
    for i, p in enumerate(sequence):
        if p not in inverse_codon_map:
            raise UnmappedProteinError('{} has no mapping or is invalid'.format(p))
        entry = inverse_codon_map[p]
        if type(entry) is str:
            continue
        num_possible *= len(inverse_codon_map[p])
    return num_possible


"""
Generates a DNA sequence from a given protein sequence and the sequence possibility number
"""
def generate_sequence(sequence, num):
    return []


if __name__ == '__main__':
    proteins = input("Proteins (single letter notation)> ")
    proteins = [p for p in list(proteins.upper()) if p in inverse_codon_map.keys()]
    num_possible = count_possible_sequences(proteins)
    print("Found {} possible DNA sequences".format(num_possible))
    for sequence_num in range(num_possible):
        print(generate_sequence(proteins, sequence_num))
