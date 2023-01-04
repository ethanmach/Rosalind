def dna_to_rna(sequence):
    """
    This function converts a DNA sequence into an RNA sequence.
    :param sequence: DNA sequence (str) to be converted into RNA
    :return rna_seq: RNA sequence (str)
    """
    rna_seq = sequence.replace("T", "U")
    return rna_seq


if __name__ == '__main__':
    print("Please input the DNA sequence to be converted to RNA: ")
    dna_seq = str(input())
    print(dna_to_rna(dna_seq))
