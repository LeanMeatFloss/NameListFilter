# NameListFilter
A python project for filtering the files in the folder that contains in the .txt list.

## Usage

This program is for this scenario:

- [x] you have a list of files
- [x] your files can be identified by the file's filename
- [x] you have a list of file names stored in .txt file that has been archived
- [x] you want to move those files into different folders "archived" and "not archived"
- [x] you want to get the list of files that are not archived

## How to Use it

Using the filter.py, and it has those following input parameters:

- -i: Input directory. The program will search all files in the directory and it's sub-directory.
- -o: Output directory path. The program will make two subdirectories that are "existed" and "donotexisted".
- -c: Configure file path. The file that stored the filename that has been stored.
- -p: Pattern ( optional ). The pattern that needs to match the input filenames. Once the matched text not existed in the configure file, the related file will move to the target directory "donotexisted". And the matched text that existed in the configure file, the related file will move to the target directory "existed".
  - By default, the pattern will set to *

