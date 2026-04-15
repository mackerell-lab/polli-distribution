import pandas as pd
import numpy as np
import math, argparse

parser = argparse.ArgumentParser(description='Compute statistics about particle distribution')
parser.add_argument('input', help='Input file, csv format')
parser.add_argument('--n_bin', type=int, default=16, help='Number of bins; default=%(default)s')
args = parser.parse_args()

# Read in ImageJ data
df = pd.read_csv(args.input)
# Calculate approximate center and shift
df['X']-=df['X'].max()/2
df['Y']-=df['Y'].max()/2

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
stats=df.groupby(f'bin{n_bin}').agg({'Area': ['count', 'sum', 'mean', 'std', 'sem']})

# Summary stats over the bins are here:
summary = stats.agg(['mean', 'std', 'sem'])
summary.index = ['Mean', 'Std', 'SEM']

stats = pd.concat([stats, summary])
print(stats)
stats.to_csv(args.input[:-4]+'_stats.csv')
print(f'\nResults saved to {args.input[:-4]}_stats.csv')
