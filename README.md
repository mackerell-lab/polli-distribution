# polli-distribution
Post-process image data to get stats about particle distribution

usage: distribution.py [-h] [--n_bin N_BIN] input

Compute statistics about particle distribution

positional arguments:
  input          Input file, csv format

options:
  -h, --help     show this help message and exit
  --n_bin N_BIN  Number of bins; default=16

Example:

$ python distribution.py Results_749-193-2_SB_only_centroids.csv 
        Area                              
       count       sum      mean       std
0.0   277.00  0.011220  0.000041  0.000083
1.0   321.00  0.010044  0.000031  0.000034
2.0   367.00  0.040215  0.000110  0.001213
3.0   185.00  0.006209  0.000034  0.000043
4.0   289.00  0.020815  0.000072  0.000588
5.0   239.00  0.010273  0.000043  0.000091
6.0   248.00  0.008441  0.000034  0.000032
7.0   236.00  0.033426  0.000142  0.001565
8.0   217.00  0.023467  0.000108  0.000958
9.0   190.00  0.006046  0.000032  0.000026
10.0  249.00  0.013792  0.000055  0.000379
11.0  256.00  0.008055  0.000031  0.000022
12.0  307.00  0.041012  0.000134  0.001492
13.0  270.00  0.031111  0.000115  0.001278
14.0  389.00  0.015160  0.000039  0.000202
15.0  348.00  0.010429  0.000030  0.000027
Mean  274.25  0.018107  0.000066  0.000502

Results saved to Results_749-193-2_SB_only_centroids_stats.csv


