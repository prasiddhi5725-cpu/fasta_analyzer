# 🧬 FASTA Analyzer & 6-Frame ORF Translation Suite

A comprehensive bioinformatics software suite built in Python to parse multi-FASTA files, perform 6-frame Open Reading Frame (ORF) identification, calculate sequence statistics, and translate DNA into protein sequences. 

This repository provides both an **interactive Web Application (GUI)** built with Streamlit and **Command-Line Tools (CLI)** for automated server execution.

---

## ✨ Features

### 🖥️ Streamlit Web GUI (`fasta_orf_detector_gui.py`)
* **Dual Input Modes:** Upload `.fasta`/`.fa`/`.txt` files or paste raw DNA sequences directly.
* **Interactive Controls:** Dynamic slider to adjust minimum ORF length cutoffs in real-time.
* **Structured Visuals:** Tabbed interface organizing all 6 reading frames ($5'\rightarrow3'$ and $3'\rightarrow5'$) alongside translated amino acid sequences.
* **Scrollable Sequence Views:** Compact code containers with horizontal and vertical scrollbars to handle long sequences cleanly.
* **Unified Export:** Download all generated ORFs and translated proteins as a standard FASTA-formatted text file.

### 💻 Command-Line Pipeline (`fasta_analyzer_pipeline.py` & `fasta_orf_detector.py`)
* **Multi-FASTA Parsing:** Reads multi-line FASTA files cleanly using dictionary data structures, preserving sequence headers (`>`).
* **Nucleotide Profiling & Statistics:**
  * Exact base counts (A, T, C, G)
  * Sequence integrity validation (flags non-canonical bases)
  * GC content percentage computation
* **Transcription & Complements:** Direct complementary and reverse complementary sequence generation.
* **6-Frame ORF Scanner:**
  * Scans forward (+1, +2, +3) and reverse complement (-1, -2, -3) strands.
  * Detects start (`ATG`) and stop (`TAA`, `TAG`, `TGA`) codons.
  * Automatically isolates and extracts the longest ORF per sequence.
* **Protein Translation:** Translates nucleotide codons into amino acid sequences using standard genetic code tables.

---

## 📁 Repository Structure

```text
.
├── fasta_orf_detector_gui.py    # Interactive Streamlit Web Application
├── fasta_orf_detector.py        # Multi-FASTA 6-frame ORF scanning & protein translation (CLI)
├── fasta_analyzer_pipeline.py   # Base statistics, GC%, RNA complements, and direct translation
├── dna_sequence_orf_detector.py # Core logic scanner for direct single-sequence input
├── requirements.txt             # Project dependencies
├── test.fasta                   # Sample multi-FASTA file for testing
└── README.md                    # Project documentation
🚀 Installation & Setup
Clone the repository:

Bash
git clone [https://github.com/YOUR_USERNAME/fasta-orf-translation-suite.git](https://github.com/YOUR_USERNAME/fasta-orf-translation-suite.git)
cd fasta-orf-translation-suite
Install dependencies:

Bash
pip install -r requirements.txt
💡 How to Use
Launching the Web App (GUI)
Run the following command to start the interactive Streamlit interface:

Bash
streamlit run fasta_orf_detector_gui.py
Running Command Line Scripts (CLI)
Run full 6-frame ORF scanner on multi-FASTA files:

Bash
python fasta_orf_detector.py
Run sequence profiling & RNA complement pipeline:

Bash
python fasta_analyzer_pipeline.py
Run single-sequence core logic script:

Bash
python dna_sequence_orf_detector.py
📋 Requirements
Python 3.8+

streamlit

pandas

biopython

📄 License
This project is open-source and available under the MIT License.
