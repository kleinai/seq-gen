def create_inv_codon_map():
    """
    Creates a dictionary:
    keys = 1-letter protein code
    entries = corresponding codons
    Written by Jennifer Pfaff
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


def get_seq(inverse_codon_map):
    """
    Asks user for input of a string with 1-letter protein codes, saved in variable proteins.
    Goes through protein string and makes a list with just the valid protein codes.
    If list is empty, either an empty string or invalid characters were entered, so it calls itself to ask for new input
    :param inverse_codon_map: dictionary with inverse codons
    :return: list of valid protein 1-letter codes
    """
    proteins = input("Proteins (single letter notation)> ")
    proteins = [p for p in list(proteins.upper()) if p in inverse_codon_map.keys()]
    if len(proteins) == 0:
        print("Error: Either all characters were invalid or empty string was entered.")
        get_seq(inverse_codon_map)
    return proteins

def generate_sequences(sequence: list, inverse_codon_map) -> list:
    """
    Generates a list of DNA sequences from a given protein sequence
    Contrib.: Aidan K.
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
    Mostly written by Patrick with help cleaning up the code by Aidan
    """
    from os import linesep
    text_file = open("output.txt", mode='w') # Creates text file to store the RNA sequence
    string_output = linesep.join(outputsequence) # turns the array input into a string that can be written to the text file
    text_file.write(string_output) # Writes the output to the output text file
    text_file.close()

def main():
    """
    Runs all the methods in sequence and then display the number of possible sequences of RNA found
    Contrib.: Aidan K.
    """
    inverse_codon_map = create_inv_codon_map()
    proteins = get_seq(inverse_codon_map)
    possible_sequences = generate_sequences(proteins, inverse_codon_map)
    output(possible_sequences)
    print("Wrote {} sequences".format(len(possible_sequences)))

    
if __name__ == '__main__':
    main()
