import streamlit as st

st.set_page_config(
    page_title="ORF Finder & Sequence Explorer",
    page_icon="🧬",
    layout="wide"
)

st.markdown("""
<style>
    .stApp { max-width: 1200px; margin: 0 auto; }
    .main-title { font-size: 2.2rem; font-weight: 700; color: #1E3A8A; margin-bottom: 0.2rem; }
    .sub-title { font-size: 1.05rem; color: #4B5563; margin-bottom: 1.5rem; }
    div[data-testid="stMetricValue"] { font-size: 1.4rem; font-weight: 600; }
</style>
""", unsafe_allow_html=True)

st.markdown('<div class="main-title">🧬 ORF Finder & Sequence Explorer</div>', unsafe_allow_html=True)
st.markdown('<div class="sub-title">An interactive bioinformatics tool to identify and analyze Open Reading Frames across all 6 reading frames.</div>', unsafe_allow_html=True)

with st.sidebar:
    st.header("⚙️ App Controls")
    
    if st.button("🔄 Reset / Clear All", use_container_width=True):
        st.rerun()

    st.divider()
    with st.expander("ℹ️ Instructions & Help"):
        st.write("**1. Input DNA:** Upload a `.fasta`/`.txt` file or paste sequence text.")
        st.write("**2. Adjust Threshold:** Set the minimum nucleotide length for valid ORFs.")
        st.write("**3. Run Analysis:** Click 'Find ORF' to evaluate all 6 reading frames.")
        st.write("**4. Export:** Download full sequence results in standardized FASTA format.")

uploaded_file = st.file_uploader("Upload a DNA sequence file (FASTA format)", type=["fasta", "fa","txt"])
pasted_sequence = st.text_area("Or paste your DNA sequence here (FASTA format)",height=200)
min_length = st.slider("Minimum ORF length (bases)", 30, 1000, 300, step=3)

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

stop_codon=("TAA","TAG","TGA")

def to_find_orf(sequence,start_codon,frame_start,min_length):
    orf=""
    found_start=False
    orf_list=[]
            

    for i in range (frame_start,len(sequence),3):
                
        codon=sequence[i:i+3]

        if codon==start_codon:
            found_start=True

        if found_start:
            orf+=codon
            if codon in stop_codon:
                if len(orf) >= min_length:
                    orf_list.append(orf)
                orf=""
                found_start=False
            
    if orf_list:
        return max(orf_list,key=len)
    else:
        return ""

if st.button("🚀 Find ORF", type="primary"):

    open_file=[]

    if uploaded_file is not None:
        open_file=uploaded_file.read().decode("utf-8").splitlines()

    elif pasted_sequence:
        open_file=pasted_sequence.strip().upper()

    if open_file:

        use_sequence=""
        collection={}
        current_header=""

        for line in open_file:
        
            sequence=line.strip().upper()

            if not sequence:
                continue

            if sequence.startswith(">"):
                current_header=sequence
                use_sequence=""
            else:
                if not current_header:
                    current_header=">pasted_sequence"
                use_sequence+=sequence
                collection[current_header]=use_sequence

        all_results=""

        for header, sequence in collection.items():

            st.divider()
            st.subheader(f"🏷️ {header}")

            gc_count=sequence.count("G")+sequence.count("C")
            gc_percent=round((gc_count/len(sequence))*100,2) if len(sequence)>0 else 0

            m_col1, m_col2, m_col3 = st.columns(3)
            m_col1.metric("Sequence Length", f"{len(sequence)} bp")
            m_col2.metric("GC Content", f"{gc_percent}%")
            m_col3.metric("Minimum ORF Cutoff", f"{min_length} bp")

            complement_table = str.maketrans("ATCG", "TAGC")

            reverse_complement_sequence = sequence.translate(complement_table)[::-1]

            with st.spinner("Analyzing reading frames..."):   

                orf_frame_1=to_find_orf(sequence,"ATG",0,min_length)
                orf_frame_2=to_find_orf(sequence,"ATG",1,min_length)
                orf_frame_3=to_find_orf(sequence,"ATG",2,min_length)

                orf_frame_4=to_find_orf(reverse_complement_sequence,"ATG",0,min_length)
                orf_frame_5=to_find_orf(reverse_complement_sequence,"ATG",1,min_length)
                orf_frame_6=to_find_orf(reverse_complement_sequence,"ATG",2,min_length)

            tab1, tab2 = st.tabs(["🔍 All Reading Frames (1–6)", "🧬 Longest ORF & Protein Translation"])

            with tab1:
                with st.container(height=180):
                
                    st.text("Frame 1 ORF: " + (orf_frame_1 if orf_frame_1 else "No valid ORF"))
                    st.text("Frame 2 ORF: " + (orf_frame_2 if orf_frame_2 else "No valid ORF"))
                    st.text("Frame 3 ORF: " + (orf_frame_3 if orf_frame_3 else "No valid ORF"))

                    st.text("Frame 4 ORF:" + (orf_frame_4 if orf_frame_4 else "No valid ORF"))
                    st.text("Frame 5 ORF: " + (orf_frame_5 if orf_frame_5 else "No valid ORF"))
                    st.text("Frame 6 ORF: " + (orf_frame_6 if orf_frame_6 else "No valid ORF"))

            all_orfs=[orf_frame_1,orf_frame_2,orf_frame_3,orf_frame_4,orf_frame_5,orf_frame_6]
            valid_orfs=[orf for orf in all_orfs if orf!=""]

            with tab2:
                if valid_orfs:
                    longest_orf=max(valid_orfs,key=len)

                    st.markdown("**Longest Detected ORF (DNA):**")
                    with st.container(height=100):
                        st.code (longest_orf, language="text")

                    for_protein=longest_orf.replace("T","U")
                    protein_sequence=""

                    for i in range(0,len(for_protein),3):
                        codon=for_protein[i:i+3]
                        amino_acid=protein.get(codon,"")
                        protein_sequence+=amino_acid

                    st.markdown("**Translated Protein Sequence:**")
                    with st.container(height=100):
                        st.code(protein_sequence, language="text")

                    all_results += f"{header}_longest_ORF\n{longest_orf}\n{header}_protein\n{protein_sequence}\n\n"

                else:
                    st.info("No valid ORF found matching the length criteria across any reading frame.")
                    all_results += f"{header}\nNo valid ORF found in any reading frame.\n\n"

        if all_results:
            st.divider()
            st.download_button(
                label="📥 Download All Results (.txt)",
                data=all_results,
                file_name="orf_results_summary.txt",
                mime="text/plain",
                use_container_width=True
            )

    else:
        st.warning("Please upload a FASTA file or paste a DNA sequence to proceed.")