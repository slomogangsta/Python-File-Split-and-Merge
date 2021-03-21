# Python-File-Split-and-Merge
These scripts are an extension of the [filesplit library](https://github.com/ram-jayapalan/filesplit, "Github Repository of filesplit"). These scripts provide the felixibilty of using command line arguments with 
the filesplit library thus making it more effective and easy to use. 
Note: These scripts do not extend all the features of the filsplit library, but does include most commonly used features.

## split.py
The split.py script splits the given file into multiple chunks. The script accepts the following arguments:
1. ``-i`` or ``--file`` (str) (Required): Path to the source file
2. ``-o`` or ``--output_dir`` (str) (Required): Path to the empty output directory. The split files will be written into this directory. If the directory does not exist the script will create it for you.
3. ``-s`` or ``--split_size`` (int) (Required): Split size in bytes. Each split will correspond to the size provided
4. ``-l`` or ``--log`` (bool) (Optional): When set to ``True``, the output of the script will be written to a log file stored in the output directory
5. ``-f`` or ``--force`` (bool) (Optional): When set to ``True``, any existing contents of the output directory will be deleted
6. ``-n`` or ``--newline`` (bool) (Optional): When set to ``True``, split files will not carry any incomplete lines. This flag can be helpful when splitting structured file.
7. ``-ih`` or ``--header`` (bool) (Optional); When set to ``True``, the first line in the source file is considered as a header and each split will include the header. This flag can be helpful when splitting structured file.
The split process creates a manifest file ``fs_manifest.csv`` in the output directory. This manifest file is required for the merge operation.

## merge.py
The merge.py script merges the split files into a sigle file. The script accepts the following arguments:
1. ``-i`` or ``--input_dir`` (str) (Required): Path to the directory containing the split files and the manifest
2. ``-o`` or ``--file`` (str) (Required): Name of the merged file. This merged file will be stored in the input directory
3. ``-l`` or ``--log`` (bool) (Optional): When set to ``True``, the output of the script will be written to a log file stored in the input directory
4. ``-c`` or ``--Clear`` (bool) (Optional): When set to ``True``, the split files will be deleted once the merged file is generated

## Usage
`example: split.py`

.. code-block:: python

    python split.py -i "/path/to/source/file" -o "/path/to/output/dir" -s 10000000 -l True -n True -ih True
 
`example: merge.py`

.. code-block:: python

    python merge.py -i "/path/to/input/dir" -o "output_file_name" -s 10000000 -l True -n True -ih True
