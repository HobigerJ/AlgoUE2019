#!/usr/bin/env python3

import argparse
import sys
import numpy as np
from Bio import SeqIO

# parser with program explanation
parser = argparse.ArgumentParser(prog="Needleman-Wunsch pairwise global sequence alignment", 
                                description="Calculates global alignment for 2 Sequences. \n" "As input please use a fasta-file (via STDIN).\n",
                                formatter_class=argparse.RawTextHelpFormatter,
                                add_help=True)
parser.add_argument("--match", 
                    type=int, 
                    default=1, 
                    help="Score for match, positive integer. Default +1")
parser.add_argument("--mismatch", 
                    type=int, 
                    default=-1,
                    help="Score for mismatch, positive or negative integer. Default -1")
parser.add_argument("--gap", 
                    type=int, 
                    default=-2, 
                    help="Score for gap, positive or negative integer. Default -2")

# parsing at the end of the file

# creating matrix in correct size, finding matches and creating score matrix

def create_matrix(row_number, column_number):
    matrix = np.zeros(shape=(row_number, column_number), dtype=np.int)
    return matrix


def find_match(nuc1, nuc2, match_score, mismatch_score):
    if nuc1 == nuc2:
        return match_score
    else:
        return mismatch_score


def needleman_wunsch(seq1, seq2, match_score, mismatch_score, gap_score):

    n = len(seq1)
    m = len(seq2)
    
    score_matrix = create_matrix(m+1, n+1)  # matrix is n*m

    for i in range(1, m+1):
        next_score = score_matrix[i - 1, 0] + gap_score 
        score_matrix[i, 0] = next_score

    for j in range(1, n+1):
        next_score = score_matrix[0, j-1] + gap_score
        score_matrix[0, j] = next_score

    for i in range(1, m+1):
        for j in range(1, n+1):

            match_find = find_match(seq1[j-1], seq2[i-1], match_score, mismatch_score)

            diagnonal_score = score_matrix[i-1, j-1] + match_find
            right_score = score_matrix[i-1, j] + gap_score
            down_score = score_matrix[i, j-1] + gap_score

            max_score = max([diagnonal_score, right_score, down_score])
            score_matrix[i, j] = max_score  # choose max score for each value

    # Traceback
    output_seq1 = ""  
    output_seq2 = ""

    i = m  # iterators have length of the sequences
    j = n

    while i > 0 and j > 0:  
        current_score = score_matrix[i][j]
        dia_score = score_matrix[i-1][j-1]
        up_score = score_matrix[i][j-1]
        left_score = score_matrix[i-1][j]

        if current_score == dia_score + find_match(seq1[j-1], seq2[i-1], match, mismatch):
            output_seq1 += seq1[j-1]
            output_seq2 += seq2[i-1]
            i -= 1
            j -= 1
        elif current_score == up_score + gap:
            output_seq1 += seq1[j-1]
            output_seq2 += "-"
            j -= 1
        elif current_score == left_score + gap:
            output_seq1 += "-"
            output_seq2 += seq2[i-1]
            i -= 1

    while j > 0:
        output_seq1 += seq1[j-1]
        output_seq2 += "-"
        j -= 1
    while i > 0:
        output_seq1 += "-"
        output_seq2 += seq2[i-1]
        i -= 1

    output_seq1 = output_seq1[::-1] 
    output_seq2 = output_seq2[::-1]

    results = [score_matrix, output_seq1, output_seq2]

    return results


def decoration(alignment_1, alignment_2):
    match_deco = ""
    length = max(len(alignment_2)-1, len(alignment_1)-1)
    i = 0
    while i <= length:
        if alignment_1[i] == alignment_2[i]:
            match_deco += "*"
            i += 1
        else:
            match_deco += " "
            i += 1
    return match_deco


def output_as_clustal(header_list, sequence_list, higlight_string):
    print("CLUSTAL\n\n")
    if len(header_list[0]) == len(header_list[1]):
        spacer = " " * len(header_list[0])

    if len(max(sequence_list[0], sequence_list[1])) <= 60:  # if length is < 60 just print
        print(f"{header_list[0]}\t{sequence_list[0]}\n"
              f"{header_list[1]}\t{sequence_list[1]}\n"
              f"{spacer}\t{higlight_string}")
    else:
        seqLength = len(sequence_list[0])   # if length is > 60 create "subs" for the next line
        i = 0
        sub_seq1 = []
        sub_seq2 = []
        sub_deco = []

        while i <= seqLength - 1:
            sub_seq1.append(sequence_list[0][i:i + 60])  # print the nucleotide in the list + index 60
            sub_seq2.append(sequence_list[1][i:i + 60])
            sub_deco.append(higlight_string[i:i + 60])
            i += 60

        i = 0
        while i <= len(sub_seq1) - 1:
            print(f"{header_list[0]}\t{sub_seq1[i]}\n"
                  f"{header_list[1]}\t{sub_seq2[i]}\n"
                  f"{spacer}\t{sub_deco[i]}\n\n")
            i += 1


# now we parse
DEBUG = False

if DEBUG:
    args = parser.parse_args(["--match", "1", "--mismatch", "-1", "--gap", "-2"])
else:
    args = parser.parse_args()

    # and then run the algorithm
    match = args.match
    mismatch = args.mismatch
    gap = args.gap

    if sys.stdin.isatty():  # checks if the program receives the input via stdin
        parser.print_help()
    else:
        header = []
        sequence = []
        for record in SeqIO.parse(sys.stdin, "fasta"):
            header.append(record.id)
            sequence.append(record.seq)

        sequence1 = sequence[0]
        sequence2 = sequence[1]

        allResults = needleman_wunsch(sequence1, sequence2, match, mismatch, gap)
        scoreMatrix = allResults[0]
        seqAlign = allResults[1:3]

        matchHighlights = decoration(seqAlign[0], seqAlign[1])

        output_as_clustal(header, seqAlign, matchHighlights)
        print(scoreMatrix[-1, -1], file=sys.stderr)