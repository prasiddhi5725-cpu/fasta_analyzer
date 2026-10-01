DNA=input("Enter the DNA sequence: ")


final_DNA=DNA.upper().strip().replace(" ","")

print(final_DNA)
complement={"A":"T", "T":"A", "C":"G", "G":"C"}

complement_sequence=""

for base in final_DNA:
    complement_base=complement.get(base.upper(), base)
    complement_sequence+=complement_base

reverse_complement=complement_sequence[::-1]
reverse=reverse_complement.replace(" ","")

stop_codon=("TAA","TAG","TGA")


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

orf_frame_1=to_find_orf(final_DNA,"ATG",0)
orf_frame_2=to_find_orf(final_DNA,"ATG",1)
orf_frame_3=to_find_orf(final_DNA,"ATG",2)

orf_frame_4=to_find_orf(reverse_complement,"ATG",0)
orf_frame_5=to_find_orf(reverse_complement,"ATG",1)
orf_frame_6=to_find_orf(reverse_complement,"ATG",2)

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

