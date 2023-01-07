def compute_gc(input_file):
    # initialize empty lists
    fasta_list = []
    dna_list = []
    percent_list = []

    # initialize empty string
    dna_seq = ''

    # line parse
    line = input_file.readline()
    while line != '':
        # append FASTA ID to list
        if line[0] == '>':
            fasta_list.append(line[1:-1])
            # append dna_seq to list
            if dna_seq != '':
                dna_list.append(dna_seq)
                dna_seq = ''

        # concatenate DNA sequence to dna_seq
        else:
            dna_seq += line[0:-1]
        line = input_file.readline()

    dna_list.append(dna_seq)

    # calculate CG percentages of each DNA sequence in dna_list; append to percent_list
    for i in range(len(dna_list)):
        cg_count = 0
        for j in range(len(dna_list[i])):
            if dna_list[i][j] == 'C' or dna_list[i][j] == 'G':
                cg_count += 1

        dna_length = len(dna_list[i])
        cg_percent = cg_count / dna_length * 100
        percent_list.append(cg_percent)

    # find and return minimum CG percentage along with Rosalind ID
    for k in range(len(percent_list)):
        min_percent = percent_list[k]
        min_id = fasta_list[k]
        if percent_list[k] < min_percent:
            min_percent = percent_list[k]
            min_id = fasta_list[k]

    return min_id, min_percent
