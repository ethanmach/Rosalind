def dna_complement(sequence: str):
    """
    This function takes an inputted DNA sequence and outputs the reverse complement version of the sequence
    eg: a 5' -> 3' DNA sense strand is input, a 3' -> 5' DNA anti-sense strand is output
    :param sequence: An inputted DNA sequence
    :return: Reverse complement
    """
    # Initialize empty list
    dna_list = []

    # Add each nucleotide into a list
    for bp in sequence:
        dna_list.append(bp)

    # Convert each nucleotide to complementing nucleotide
    for i in range(len(dna_list)):
        if dna_list[i] == 'A':
            dna_list[i] = 'T'
        elif dna_list[i] == 'C':
            dna_list[i] = 'G'
        elif dna_list[i] == 'T':
            dna_list[i] = 'A'
        elif dna_list[i] == 'G':
            dna_list[i] = 'C'

    # Reverse nucleotides in list, then convert list into string
    dna_list.reverse()
    output = "".join(dna_list)
    return output


if __name__ == '__main__':
    print("What is the DNA sequence to be complemented?")
    dna_seq = str(input())
    print(dna_complement(dna_seq))
