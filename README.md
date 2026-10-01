# FASTA Analyzer & 6-Frame ORF Translation Pipeline

A robust Python bioinformatics suite designed to parse multi-FASTA files, calculate nucleotide statistics, scan sequences across all 6 open reading frames (ORFs), and translate DNA into protein sequences.

This repository combines sequence profiling, transcription, complementation, and full 6-frame ORF scanning into a single, light-weight, pure-Python toolset.

---

## Key Features

- **Multi-FASTA Parsing:** Reads multi-line FASTA files cleanly, handling headers (`>`) and sequence fragmentation using dictionary data structures.
- **Nucleotide Profiling & Statistics:**
  - Precise base counts (A, T, C, G)
  - Sequence integrity validation (flags non-canonical characters)
  - GC content percentage computation
- **Transcription & Complements:**
  - Direct complementary RNA sequence generation
  - Reverse complementary RNA sequence mapping
- **6-Frame ORF Search:**
  - Scans forward and reverse complement strands across frames 0, 1, and 2
  - Identifies start (`ATG`) and stop (`TAA`, `TAG`, `TGA`) codons to locate valid ORFs
  - Isolates and extracts the longest ORF per sequence automatically
- **Protein Translation:** Translates DNA/RNA codons into amino acid sequences using standard genetic code mapping.

---

## Repository Structure

```text
.
├── fasta_analyzer_pipeline.py   # Base statistics, GC%, RNA complements, and direct translation
├── fasta_orf_detector.py        # Multi-FASTA 6-frame ORF scanning & protein translation
├── dna_sequence_orf_detector.py # Core logic scanner for direct single-sequence input
└── test.fasta                   # Sample multi-FASTA file for quick testing
