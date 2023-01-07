from pathlib import Path
import argparse
from computingGCcontent.computing_gc_content import compute_gc

# initialize argparse object, add input parameters
arg_parser = argparse.ArgumentParser()
arg_parser.add_argument("in_file", type=str, help="Input File Pathname")
args = arg_parser.parse_args()

in_path = Path(args.in_file)

# call main method 'compute_gc' and print answer to terminal
with in_path.open('r') as input_file:
    gc = compute_gc(input_file)
    print(f'{gc[0]}\n{gc[1]}')
