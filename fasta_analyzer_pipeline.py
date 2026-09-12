file_name=input("Enter the file name: ")
open_file=open(file_name)

use_sequence=""
collection={}

complement={"A":"U", "T":"A", "C":"G", "G":"C"}

protein={"GCU":"A","GCC":"A","GCA":"A","GCG":"A",
         "CGU":"R","CGC":"R","CGA":"R","CGG":"R","AGA":"R","AGG":"R",
         "AAU":"N","AAC":"N",
         "GAU":"D","GAC":"D",
         "UGU":"C","UGC":"C",
         "GAA":"E","GAG":"E",
         "CAA":"Q","CAG":"Q",
         "GGU":"G","GGC":"G","GGA":"G","GGG":"G",
         "CAU":"H","CAC":"H",
         "AUU":"I","AUC":"I","AUA":"I",
         "UUA":"L","UUG":"L","CUU":"L","CUC":"L","CUA":"L","CUG":"L",
         "AAA":"K","AAG":"K",
         "AUG":"M",
         "UUU":"F","UUC":"F",
         "CCU":"P","CCC":"P","CCA":"P","CCG":"P",
         "UCU":"S","UCC":"S","UCA":"S","UCG":"S","AGU":"S","AGC":"S",
         "ACU":"T","ACC":"T","ACA":"T","ACG":"T",
         "UGG":"W",
         "UAU":"Y","UAC":"Y",
         "GUU":"V","GUC":"V","GUA":"V","GUG":"V",
         "UAA":"*","UAG":"*","UGA":"*"}


for line in open_file:
    
    sequence=line.strip().upper().replace("\n", "")

    
    if sequence.startswith(">"):
        current_header=sequence
        use_sequence=""
    else:
        use_sequence+=sequence
    collection[current_header]=use_sequence


for header, sequence in collection.items():
    A_count=sequence.count("A")
    T_count=sequence.count("T")
    C_count=sequence.count("C")
    G_count=sequence.count("G")

    if len(sequence) > 0:
        GC_content= (G_count + C_count) / len(sequence) * 100
    else:
        GC_content=0
        
    total_bases=A_count + T_count + C_count + G_count

    if total_bases != len(sequence):
        print("Warning: The DNA sequence contains invalid characters.")
    else:
        print("The DNA sequence is valid.")

    complement_sequence=""

    for base in sequence:
        complement_base=complement.get(base.upper(), base)
        complement_sequence+=complement_base

    reverse_complement_sequence=complement_sequence[::-1]

    protein_sequence=""
    for i in range(0, len(complement_sequence), 3):
        codon=complement_sequence[i:i+3]
        amino_acid=protein.get(codon, "N/A")
        protein_sequence+=amino_acid

    print(header)
    print("Number of A's:", A_count)    
    print("Number of T's:", T_count)
    print("Number of C's:", C_count)
    print("Number of G's:", G_count)
    print("GC content percentage:", round(GC_content, 2), "%")
    print("The complementary RNA sequence is:", complement_sequence)
    print("The reverse complementary RNA sequence is:", reverse_complement_sequence)
    print("The protein sequence is:", protein_sequence)