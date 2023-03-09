def proteins(strand):
    
    codons = {
        'AUG': 'Methionine',
        ('UUU', 'UUC'): 'Phenylalanine',
        ('UUA', 'UUG'): 'Leucine',
        ('UCU', 'UCC', 'UCA', 'UCG'): 'Serine',
        ('UAU', 'UAC'): 'Tyrosine',
        ('UGU', 'UGC'): 'Cysteine',
        'UGG': 'Tryptophan',
        ('UAA', 'UAG', 'UGA'): 'STOP'
    }

    STOP_LIST = ['UAA', 'UAG', 'UGA']

    codons_list = []
    i = 0

    # form a codon list
    while i < len(strand):
        codons_list += [strand[i:i+3]]
        i += 3
    translation = []

    for codon_strand in codons_list:
        for codon, protein in codons.items():
            if codon_strand in STOP_LIST:
                return translation
            elif codon_strand in codon:
                translation += [protein]

    return translation