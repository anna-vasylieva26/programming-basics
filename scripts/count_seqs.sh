#!/bin/bash
# count_seqs.sh — how many sequences are in a FASTA file?

file=$1                          # $1 = the first thing after the script name
n=$(grep -c ">" "$file")         # $( ) = save the output of a command
echo "$file contains $n sequences"