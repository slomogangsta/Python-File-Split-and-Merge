from fsplit.filesplit import Filesplit
import os, argparse, sys, glob, shutil

ap = argparse.ArgumentParser()
ap.add_argument("-i", "--file", required=True, help="Path to input file")
ap.add_argument("-o", "--output_dir", required=True, help="Path to the empty output directory")
ap.add_argument("-s", "--split_size", required=True, help="Size of each split in bytes")
ap.add_argument("-l", "--log", required=False, help="When set to True, execution log is written to log_split.txt")
ap.add_argument("-f", "--force", required=False, help="When set to True, removes any existing files in the Output Directory")
ap.add_argument("-n", "--newline", required=False, help="When set to True, split files will not carry any incomplete lines. Useful for structured files")
ap.add_argument("-ih", "--header", required=False, help="When set to True,  the first line in the source file is considered as a header and each split will include the header. Useful for structure files")
args = vars(ap.parse_args())

def delete_files():
    folder = args['output_dir']
    for filename in os.listdir(folder):
        file_path = os.path.join(folder, filename)
        try:
            if os.path.isfile(file_path) or os.path.islink(file_path):
                os.unlink(file_path)
            elif os.path.isdir(file_path):
                shutil.rmtree(file_path)
        except PermissionError as pe:
            print(pe)
            print("Please re-run the code with appropriate privilages")
        except Exception as e:
            print('Failed to delete %s. Reason: %s' % (file_path, e))

def split_cb(f, s):
    print("file: {0}, size: {1}".format(f, s))
    if(bool(args['log'])):
        fo = open(args['output_dir']+"\log_split.txt","a")
        fo.write("file: {0}, size: {1}\n".format(f, s))
        fo.close()

args['output_dir'] = args['output_dir'].replace("\\","/")
args['file'] = args['file'].replace("\\","/")

try:

    if(os.path.isdir(args['output_dir'])):
        if(bool(args['force'])):
            delete_files()
        if(len(os.listdir(args['output_dir']))!=0):
            raise ValueError("Output directory should be empty! Exiting...")
    else:
        os.mkdir(args['output_dir'])

    if not os.path.isfile(args['file']):
        raise ValueError("Input file path is invalid")
    
    fs = Filesplit()
    fs.split(file=args['file'], split_size=int(args['split_size']), output_dir=args['output_dir'], callback=split_cb, new_line = bool(args['newline']), include_header = bool(args['header']))
    print("Splitting sucessfully completed!")

except ValueError as ve:
   print(ve)

except Exception as e:
    print("Oops!", e.__class__, "occurred.")