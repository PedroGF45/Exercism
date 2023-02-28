def to_rna(dna_strand):
    rna_strand = ''
    for item in dna_strand:
        if item == 'G':
            rna_strand += 'C'
        elif item == 'C':
            rna_strand += 'G'
        elif item == 'T':
            rna_strand += 'A'
        else:
            rna_strand += 'U'
    return rna_strand
