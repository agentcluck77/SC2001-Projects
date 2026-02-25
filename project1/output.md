aloy@Aloysiuss-MBP ~/p/SC2001-projects (main) [SIGTERM]> uv run python project1/experiment.py
=== (c-i) Fixed S, vary n ===
  n=     1,000  comparisons=13,443
  n=     2,000  comparisons=28,641
  n=     5,000  comparisons=66,639
  n=    10,000  comparisons=143,251
  n=    20,000  comparisons=307,487
  n=    50,000  comparisons=879,469
  n=   100,000  comparisons=1,861,055
  n=   200,000  comparisons=3,925,456
  n=   500,000  comparisons=11,100,774
  n= 1,000,000  comparisons=23,186,830
  n= 2,000,000  comparisons=48,377,083
  n= 5,000,000  comparisons=116,159,682
  n=10,000,000  comparisons=242,316,893

=== (c-ii) Fixed n, vary S ===
  S=     1  comparisons=1,536,452
  S=     2  comparisons=1,536,452
  S=     3  comparisons=1,536,327
  S=     4  comparisons=1,536,715
  S=     5  comparisons=1,536,715
  S=     6  comparisons=1,554,603
  S=     7  comparisons=1,557,771
  S=     8  comparisons=1,557,771
  S=     9  comparisons=1,557,771
  S=    10  comparisons=1,557,771
  S=    11  comparisons=1,557,771
  S=    12  comparisons=1,619,210
  S=    13  comparisons=1,638,658
  S=    14  comparisons=1,638,658
  S=    15  comparisons=1,638,658
  S=    16  comparisons=1,638,658
  S=    17  comparisons=1,638,658
  S=    18  comparisons=1,638,658
  S=    19  comparisons=1,638,658
  S=    20  comparisons=1,638,658
  S=    21  comparisons=1,638,658
  S=    22  comparisons=1,638,658
  S=    23  comparisons=1,638,658
  S=    24  comparisons=1,763,202
  S=    25  comparisons=1,860,433
  S=    26  comparisons=1,860,433
  S=    27  comparisons=1,860,433
  S=    28  comparisons=1,860,433
  S=    29  comparisons=1,860,433
  S=    30  comparisons=1,860,433
  S=    31  comparisons=1,860,433
  S=    32  comparisons=1,860,433
  S=    33  comparisons=1,860,433
  S=    34  comparisons=1,860,433
  S=    35  comparisons=1,860,433
  S=    36  comparisons=1,860,433
  S=    37  comparisons=1,860,433
  S=    38  comparisons=1,860,433
  S=    39  comparisons=1,860,433
  S=    40  comparisons=1,860,433
  S=    41  comparisons=1,860,433
  S=    42  comparisons=1,860,433
  S=    43  comparisons=1,860,433
  S=    44  comparisons=1,860,433
  S=    45  comparisons=1,860,433
  S=    46  comparisons=1,860,433
  S=    47  comparisons=1,860,433
  S=    48  comparisons=1,946,232
  S=    49  comparisons=2,381,785
  S=    50  comparisons=2,381,785
  S=    51  comparisons=2,381,785
  S=    52  comparisons=2,381,785
  S=    53  comparisons=2,381,785
  S=    54  comparisons=2,381,785
  S=    55  comparisons=2,381,785
  S=    56  comparisons=2,381,785
  S=    57  comparisons=2,381,785
  S=    58  comparisons=2,381,785
  S=    59  comparisons=2,381,785
  S=    60  comparisons=2,381,785
  S=    61  comparisons=2,381,785
  S=    62  comparisons=2,381,785
  S=    63  comparisons=2,381,785
  S=    64  comparisons=2,381,785
  S=    65  comparisons=2,381,785
  S=    66  comparisons=2,381,785
  S=    67  comparisons=2,381,785
  S=    68  comparisons=2,381,785
  S=    69  comparisons=2,381,785
  S=    70  comparisons=2,381,785
  S=    71  comparisons=2,381,785
  S=    72  comparisons=2,381,785
  S=    73  comparisons=2,381,785
  S=    74  comparisons=2,381,785
  S=    75  comparisons=2,381,785
  S=    76  comparisons=2,381,785
  S=    77  comparisons=2,381,785
  S=    78  comparisons=2,381,785
  S=    79  comparisons=2,381,785
  S=    80  comparisons=2,381,785
  S=    81  comparisons=2,381,785
  S=    82  comparisons=2,381,785
  S=    83  comparisons=2,381,785
  S=    84  comparisons=2,381,785
  S=    85  comparisons=2,381,785
  S=    86  comparisons=2,381,785
  S=    87  comparisons=2,381,785
  S=    88  comparisons=2,381,785
  S=    89  comparisons=2,381,785
  S=    90  comparisons=2,381,785
  S=    91  comparisons=2,381,785
  S=    92  comparisons=2,381,785
  S=    93  comparisons=2,381,785
  S=    94  comparisons=2,381,785
  S=    95  comparisons=2,381,785
  S=    96  comparisons=2,381,785
  S=    97  comparisons=2,765,465
  S=    98  comparisons=3,506,203
  S=    99  comparisons=3,506,203
  S=   100  comparisons=3,506,203

=== (c-iii) Optimal S per size ===
  n=     1,000  optimal S=1  comparisons=8,687
  n=     5,000  optimal S=1  comparisons=55,247
  n=    10,000  optimal S=1  comparisons=120,456
  n=    50,000  optimal S=1  comparisons=718,230
  n=   100,000  optimal S=1  comparisons=1,536,276

=== (d) Hybrid vs Mergesort on 10M ===


==================================================
  n = 10,000,000,  S = 32
  hybrid_sort : 242,315,882 comparisons  |  40.442s
  merge_sort  : 220,098,758 comparisons  |  41.675s
==================================================

