# FASTA Analyzer Pipeline

A Python tool that reads a multi-FASTA file and runs a full analysis on
each sequence it contains — from raw DNA all the way to a translated
protein.

For every sequence in the file, it reports:
- Base counts (A, T, C, G)
- Whether the sequence is valid (contains only A/T/C/G)
- GC content percentage
- The complementary RNA sequence
- The reverse complementary RNA sequence
- The translated protein sequence (using the standard codon table)

Handles files with multiple sequences (multi-FASTA), correctly keeping
each sequence's results separate.

## Files
- `fasta_analyzer_pipeline.py` — main script
- `test.fasta` — sample multi-FASTA file with several real sequences, included for testing

## Run it
```
python dna_toolkit.py
```
Then enter the path to a `.fasta` file when prompted (e.g. `test.fasta`
if using the included sample file). The file should be in the same
folder as the script, or you can give a full path.
