"""
Inverse codon map. Synonymous codons should be in a list 
"""

inverse_codon_map = {
    'K': ["AAA", "AAG"],
    'N': ["AAC", "AAU"],
    'T': ["ACA", "ACC", "ACG", "ACU"],
    'R': ["AGA", "AGG", "CGA", "CGC", "CGG", "CGU"],
    'S': ["AGC", "AGU", "UCA", "UCC", "UCG", "UCU"],
    'I': ["AUA", "AUC", "AUU"],
    'M': ["AUG"],
    'Q': ["CAA", "CAG"],
    'H': ["CAC", "CAU"],
    'P': ["CCA", "CCC", "CCG", "CCU"],
    'L': ["CUA", "CUC", "CUG", "CUU", "UUA", "UUG"],
    'E': ["GAA", "GAG"],
    'D': ["GAC", "GAU"],
    'A': ["GCA", "GCC", "GCG", "GCU"],
    'G': ["GGA", "GGC", "GGG", "GGU"],
    'V': ["GUA", "GUC", "GUG", "GUU"],
    '_': ["UAA", "UAG", "UGA"],
    'Y': ["UAC", "UAU"],
    'C': ["UGC", "UGU"],
    'F': ["UUC", "UUU"],
    'W': ["UGG"]
    }

"""
class handles anytime something is passed as a protein that isn't really a protein
"""
class UnmappedProteinError(Exception):
    pass


def generate_sequences(sequence: list) -> list:
    """
    Generates a list of DNA sequences from a given protein sequence
    """
    sub_sequences = ['']
    if len(sequence) > 1:
        sub_sequences = generate_sequences(sequence[1:]) # Breaks the sequence down recursively into subsequences
    gen_sequences = []  
    for codon in inverse_codon_map[sequence[0]]: # Builds each sequence into an array of output sequences
        for sub_sequence in sub_sequences:
            gen_sequences.append(codon + sub_sequence)
    return gen_sequences
    output(gen_sequences)
   
"""
Outputs the sequences to a text file
"""
def output(outputsequence):
    from os import linesep
    text_file = open("output.txt", mode='w') # Creates text file to store the RNA sequence
    string_output = linesep.join(outputsequence) # turns the array input into a string that can be written to the text file
    text_file.write(string_output) # Writes the output to the output text file
    text_file.close()
"""
Runs all the methods in sequence and then display the number of possible sequences of RNA found
"""

if __name__ == '__main__':
    proteins = input("Proteins (single letter notation)> ")
    proteins = [p for p in list(proteins.upper()) if p in inverse_codon_map.keys()]
    possible_sequences = generate_sequences(proteins)
    output(possible_sequences)
    print("Wrote {} sequences".format(len(possible_sequences)))
