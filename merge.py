from fsplit.filesplit import Filesplit
import os, argparse, sys, glob

ap = argparse.ArgumentParser()
ap.add_argument("-i", "--input_dir", required=True, help="Path to directory containing the split files")
ap.add_argument("-o", "--file", required=True, help="Output file name")
ap.add_argument("-l", "--log", required=False, help="When set to True, execution log is written to log_split.txt")
ap.add_argument("-c", "--clean", required=False, help="Removes split files after merging them")
args = vars(ap.parse_args())

def merge_cb(f, s):
    print("file: {0}, size: {1}".format(f, s))
    if(bool(args['log'])):
        fo = open(args['input_dir']+"\log_merge.txt","a")
        fo.write("file: {0}, size: {1}\n".format(f, s))
        fo.close()

try:
    args['input_dir'] = args['input_dir'].replace("\\","/")
    args['file'] = args['input_dir'] + "/" + args['file'] 

    if(os.path.isdir(args['input_dir'])):
        if(len(os.listdir(args['input_dir']))==0):
            raise ValueError("Input directory should not be empty! Exiting...")
    else:
        raise ValueError("Input directory path is invalid")
    
    fs = Filesplit()
    fs.merge(input_dir=args['input_dir'], output_file=args['file'], callback=merge_cb, cleanup=bool(args['clean']))
    print("Merging sucessfully completed!")

except ValueError as ve:
   print(ve)

except Exception as e:
    print("Oops!", e.__class__, "occurred.")