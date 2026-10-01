file_name=input("Enter the file name: ")
open_file=open(file_name)

use_sequence=""
collection={}

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

complement={"A":"T", "T":"A", "C":"G", "G":"C"}

for line in open_file:
    
    sequence=line.strip().upper().replace("\n", "")

    
    if sequence.startswith(">"):
        current_header=sequence
        use_sequence=""
    else:
        use_sequence+=sequence
    collection[current_header]=use_sequence


for header, sequence in collection.items():

    complement_sequence=""

    for base in sequence:
        complement_base=complement.get(base.upper(), base)
        complement_sequence+=complement_base

    reverse_complement_sequence=complement_sequence[::-1]

    stop_codon=("TAA","TAG","TGA")

    print(header)

    def to_find_orf(sequence,start_codon,frame_start):
        orf=""
        found_start=False
        found_stop=False
        orf_list=[]
        

        for i in range (frame_start,len(sequence),3):
            
            codon=sequence[i:i+3]

            if codon==start_codon:
                found_start=True

            if found_start:
                orf+=codon
                if codon in stop_codon:
                    found_stop=True
                    orf_list.append(orf)
                    orf=""
                    found_start=False

        print("The found ORF of:",frame_start,":",orf_list if orf_list!=[] else "No ORF was found")
        
        if orf_list:
            return max(orf_list,key=len)
        else:
            return ""

    orf_frame_1=to_find_orf(use_sequence,"ATG",0)
    orf_frame_2=to_find_orf(use_sequence,"ATG",1)
    orf_frame_3=to_find_orf(use_sequence,"ATG",2)

    orf_frame_4=to_find_orf(reverse_complement_sequence,"ATG",0)
    orf_frame_5=to_find_orf(reverse_complement_sequence,"ATG",1)
    orf_frame_6=to_find_orf(reverse_complement_sequence,"ATG",2)

    print("Frame 1 ORF:", orf_frame_1 if orf_frame_1 else "No valid ORF")
    print("Frame 2 ORF:",orf_frame_2 if orf_frame_2 else "No valid ORF")
    print("Frame 3 ORF:", orf_frame_3 if orf_frame_3 else "No valid ORF")

    print("Frame 4 ORF:",orf_frame_4 if orf_frame_4 else "No valid ORF")
    print("Frame 5 ORF:",orf_frame_5 if orf_frame_5 else "No valid ORF")
    print("Frame 6 ORF:", orf_frame_6 if orf_frame_6 else "No valid ORF")

    all_orfs=[orf_frame_1,orf_frame_2,orf_frame_3,orf_frame_4,orf_frame_5,orf_frame_6]
    valid_orfs=[orf for orf in all_orfs if orf!=""]

    if valid_orfs:
        longest_orf=max(valid_orfs,key=len)
        print("Final ORF (longest):",longest_orf)

    else:
        print("No valid ORF found in any reading frame.")

    for_protein=longest_orf.replace("T","U")
    protein_sequence=""

    for i in range(0, len(for_protein), 3):
        codon=for_protein[i:i+3]
        amino_acid=protein.get(codon, "N/A")
        protein_sequence+=amino_acid
        
    print("Protein Sequence:", protein_sequence)