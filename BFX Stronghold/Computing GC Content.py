from decimal import Decimal

def compute_GC(seq):
    pass


if __name__ == "__main__":
    with open("sample.txt", "r") as file:
        fasta_list = []
        dna_list = []
        percent_list = []

        dna_seq = ''
        line = file.readline()
        while line != '':
            if line[0] == '>':
                fasta_list.append(line[1:-1])
                if dna_seq != '':
                    dna_list.append(dna_seq)
                    dna_seq = ''
            else:
                dna_seq += line[0:-1]

            line = file.readline()

        dna_list.append(dna_seq)

        for i in range(len(dna_list)):
            cg_count = 0
            for j in range(len(dna_list[i])):
                if dna_list[i][j] == 'C' or dna_list[i][j] == 'G':
                    cg_count += 1

            dna_length = len(dna_list[i])
            cg_percent = cg_count / dna_length * 100
            percent_list.append(cg_percent)

    print(fasta_list)
    print(dna_list)
    print(percent_list)