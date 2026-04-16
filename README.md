# polli-distribution
Post-process image data to get stats about particle distribution in angular bins (sectors) provided by ImageJ. You can obtain centroids of the particles from ImageJ and export that as a csv by selecting Centroid under the menu Analyze > Set Measurements... .
The CSV is expected to have at least these three columns: Area, X, Y. It may have others, e.g. Mean, Min, Max. The order doesn't matter. It is expected to be created with ImageJ to have the circular ROI defined, wiht the center of that circular ROI contained in the first row. The last 4 rows contain stats which are ignored.

A new CSV file is created with "\_statsN" appended to the name. If your input file is test.csv with n\_bin=5, then test\_stats5.csv is created. It generates n\_bin sectors, and the following per-bin statistics: total count of particles, sum of Area, mean of Area, stdev of Area, and standard error of the mean of Area. Then over all bins, additional stats are reported, namely the Mean, Std and SEM.

An area distribution with n\_bin\_area many bins is also generated per-sector. The min and max area to set the edges of the histogram can also be supplied. They will be automatically determined based on the total area distribution if not supplied.


```
$ python distribution.py -h
usage: distribution.py [-h] [-o O] [--n_bin N_BIN] [--max_area MAX_AREA] [--min_area MIN_AREA] [--n_bin_area N_BIN_AREA] input

Compute statistics about particle distribution

positional arguments:
  input                 Input file, csv format

options:
  -h, --help            show this help message and exit
  -o O                  Optional name of output file, csv format
  --n_bin N_BIN         Number of Sector-shaped bins; default=16
  --max_area MAX_AREA   Optional max Area for the size distribution (auto-calculated if not supplied)
  --min_area MIN_AREA   Optional min Area for the size distribution (auto-calculated if not supplied)
  --n_bin_area N_BIN_AREA
                        Number of particle size (Area) distribution bins; default=10
```

Example:

```
$ python distribution.py test.csv --n_bin 5 --n_bin_area 3 --max_area 0.03 
            count       sum      mean       std       sem  (2.03e-05, 0.01]  (0.01, 0.02]  (0.02, 0.03]
0.0   1147.000000  0.086340  0.000075  0.000725  0.000021        642.000000      0.000000      1.000000
1.0    998.000000  0.067786  0.000068  0.000378  0.000012        691.000000      1.000000      0.000000
2.0    673.000000  0.068114  0.000101  0.001074  0.000041        296.000000      1.000000      1.000000
3.0   1027.000000  0.092731  0.000090  0.000940  0.000029        731.000000      0.000000      1.000000
4.0   1215.000000  0.080981  0.000067  0.000636  0.000018        617.000000      0.000000      1.000000
Mean  1012.000000  0.079190  0.000080  0.000750  0.000024        595.400000      0.400000      0.800000
Std    209.031098  0.011073  0.000015  0.000271  0.000011        173.064439      0.547723      0.447214
SEM     93.481549  0.004952  0.000007  0.000121  0.000005         77.396770      0.244949      0.200000

Results saved to test_stats5.csv

```

