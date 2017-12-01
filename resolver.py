def create_inv_codon_map():
    """
    Creates a dictionary:
    keys = 1-letter protein code
    entries = corresponding codons
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
    return inverse_codon_map


class UnmappedProteinError(Exception):
    """
    class handles anytime something is passed as a protein that isn't really a protein
    """
    pass


def generate_sequences(sequence: list, inverse_codon_map) -> list:
    """
    Generates a list of DNA sequences from a given protein sequence
    """
    sub_sequences = ['']
    if len(sequence) > 1:
        sub_sequences = generate_sequences(sequence[1:], inverse_codon_map) # Breaks the sequence down recursively into subsequences
    gen_sequences = []  
    for codon in inverse_codon_map[sequence[0]]: # Builds each sequence into an array of output sequences
        for sub_sequence in sub_sequences:
            gen_sequences.append(codon + sub_sequence)
    return gen_sequences

   

def output(outputsequence):
    """
    Outputs the sequences to a text file
    """
    from os import linesep
    text_file = open("output.txt", mode='w') # Creates text file to store the RNA sequence
    string_output = linesep.join(outputsequence) # turns the array input into a string that can be written to the text file
    text_file.write(string_output) # Writes the output to the output text file
    text_file.close()

def main():
    """
    Runs all the methods in sequence and then display the number of possible sequences of RNA found
    """
    inverse_codon_map = create_inv_codon_map()
    proteins = input("Proteins (single letter notation)> ")
    proteins = [p for p in list(proteins.upper()) if p in inverse_codon_map.keys()]
    possible_sequences = generate_sequences(proteins, inverse_codon_map)
    output(possible_sequences)
    print("Wrote {} sequences".format(len(possible_sequences)))

    
if __name__ == '__main__':
    main()
