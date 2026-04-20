import pandas as pd
import numpy as np
import math, argparse

parser = argparse.ArgumentParser(description='Compute statistics about particle distribution')
parser.add_argument('input', help='Input file, csv format')
parser.add_argument('-o', help='Optional name of output file, csv format')
parser.add_argument('--n_bin', type=int, default=16, help='Number of Sector-shaped bins; default=%(default)s')
parser.add_argument('--max_area', type=float, help='Optional max Area for the size distribution (auto-calculated if not supplied)')
parser.add_argument('--min_area', type=float, help='Optional min Area for the size distribution (auto-calculated if not supplied)')
parser.add_argument('--n_bin_area', type=int, default=10, help='Number of particle size (Area) distribution bins; default=%(default)s')
args = parser.parse_args()

if args.input[-3:] != 'csv':
  print('ERROR: Input must be CSV format file with .csv extension!')
  quit(1)

# Read in ImageJ data
df = pd.read_csv(args.input, skipfooter=4, engine='python') 
# assumes first line has overall circle Area and Centroid X,Y (this is saved into metadata)
# skips the last 4 rows which contain stats we don't need (Mean, Min, Max, SD)
metadata = df.iloc[0]
df = df.iloc[1:].copy()
x0 = float(metadata['X'])
y0 = float(metadata['Y'])
# Calculate approximate center and shift
df['X']-=x0
df['Y']-=y0

# r = sqrt(x^2, y^2)
df['r'] = np.sqrt(df['X']**2+df['Y']**2)

# theta = atan2(y/x)
# NOTE: atan2 robustly defined piecewise from -pi to pi
# https://en.wikipedia.org/wiki/Atan2#Definition_and_computation
df['theta'] = np.arctan2(df['Y'],df['X'])

n_bin=args.n_bin
# Compute n_bin sectors:
df[f'bin{n_bin}'] = np.floor((df['theta'] + np.pi) / (2*np.pi) * n_bin)%n_bin
# Stats per-bin (per-sector) are calculated here:

stats = df.groupby(f'bin{n_bin}').agg(
  count=('Area', 'count'),
  sum=('Area', 'sum'),
  mean=('Area', 'mean'),
  std=('Area', 'std'),
  sem=('Area', 'sem')
)

# Size distribution calculation:
min_area = df["Area"].min()
if args.min_area: min_area = args.min_area
max_area = df["Area"].max()
if args.max_area: max_area = args.max_area

bins = np.linspace(min_area, max_area, args.n_bin_area+1)
size_distr = (df.assign(area_bin=pd.cut(df["Area"], bins=bins, include_lowest=True))
    .groupby([f"bin{n_bin}", "area_bin"], observed=False)
    .size()
    .unstack(fill_value=0)
)
stats = stats.join(size_distr, how='left')

# Summary stats over the bins:
summary = stats.agg(['mean', 'std', 'sem'])
summary.index = ['Mean', 'Std', 'SEM']

stats = pd.concat([stats, summary])
print(stats)

# Save output
output_filename=f'{args.input[:-4]}_stats{n_bin}.csv'
stats.to_csv(output_filename)
print(f'\nResults saved to {output_filename}')
