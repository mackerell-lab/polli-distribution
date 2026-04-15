# polli-distribution
Post-process image data to get stats about particle distribution in angular bins (sectors) provided by ImageJ. You can obtain centroids of the particles from ImageJ and export that as a csv by selecting Centroid under the menu Analyze > Set Measurements... .
The CSV is expected to have at least these three columns: Area, X, Y. It may have others, e.g. Mean, Min, Max. The order doesn't matter.

A new CSV file is created with "\_statsN" appended to the name. If your input file is example.csv with n\_bin=3, then example\_stats3.csv is created. It generates n\_bin sectors, and the following per-bin statistics: total count of particles, sum of Area, mean of Area, stdev of Area, and standard error of the mean of Area. Then over all bins, additional stats are reported, namely the Mean, Std and SEM.

The CSV is expected to be created with ImageJ to have the circular ROI defined, and the center is contained in the first row. THe last 4 rows contain stats which are ignored.

```
usage: distribution.py [-h] [--n_bin N_BIN] input

Compute statistics about particle distribution

positional arguments:
  input          Input file, csv format

options:
  -h, --help     show this help message and exit
  --n_bin N_BIN  Number of bins; default=16
```

Example:

```
$ python distribution.py Results_749-193-2_SB_only_centroids.csv --n_bin 4
             Area                                        
            count       sum      mean       std       sem
0.0   1150.000000  0.067687  0.000059  0.000687  0.000020
1.0   1012.000000  0.072954  0.000072  0.000820  0.000026
2.0    912.000000  0.051360  0.000056  0.000508  0.000017
3.0   1314.000000  0.097711  0.000074  0.000931  0.000026
Mean  1097.000000  0.072428  0.000065  0.000737  0.000022
Std    174.497373  0.019199  0.000009  0.000182  0.000004
SEM     87.248687  0.009600  0.000005  0.000091  0.000002

Results saved to Results_749-193-2_SB_only_centroids_stats.csv
```

