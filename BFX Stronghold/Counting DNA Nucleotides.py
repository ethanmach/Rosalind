def bp_count(seq: str):
    """
    This function counts the amount of DNA nucleotides in a DNA sequence and outputs the base pairs in A C T G format
    :param seq:
    :return:
    """
    # Exception handling for sequences over 1000 base pairs
    if len(seq) > 1000:
        raise Exception("The DNA sequence input is too long to be analyzed!")

    if "A" in seq or "C" in seq or "T" in seq or "G" in seq:
        # Initialize list in order of ACGT
        bp_list = [0, 0, 0, 0]

        # main algo
        for base_pair in seq:
            if base_pair == "A":
                bp_list[0] += 1
            elif base_pair == 'C':
                bp_list[1] += 1
            elif base_pair == 'G':
                bp_list[2] += 1
            elif base_pair == 'T':
                bp_list[3] += 1

    # Exception Handling for RNA
    else:
        raise Exception("There are inappropriate letters in the sequence data!")

    return f'{bp_list[0]} {bp_list[1]} {bp_list[2]} {bp_list[3]}'


if __name__ == '__main__':
    print("Please enter a DNA sequence. Its nucleotides will be counted and outputted in A C G T format: ")
    sample_seq = str(input())
    print(bp_count(sample_seq))
