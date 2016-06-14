# Program to delete a file in complete directory tree.

# Import os library to access some buit-in functions for access directory name, status etc.
import os;

# Print details about program to user.
print '\n' + '*' * 10 + ' Remove file with Pyhton ' + '*' * 10;
print '  Note:- Enter value inside Quotes (Example >> Hello: \'World\')\n'

# Get users input for file name and directory path.

file_to_delete = input('Enter file name to delete: ');
directory = input('Enter directory from which file should be deleted: ');

if directory[0] == '~':
    directory = directory.replace('~', os.path.expanduser('~'), 1);

def path_exists(directory):
    'Check if the path entered by user exists'
    try:
        os.stat(os.path.dirname(directory));
        print 'Directory found: Initiating file remove......';
        delete_file_in_tree(file_to_delete, directory);
    except:
        print 'Directory not found: Aborting.......';

def delete_file_in_tree(file, directory):
    'Delete all the file occurance in the directory tree'

    # Track number of files deleted
    file_removed = 0;

    for (pathname, dirname, filename) in os.walk(directory):
        for file_name in filename:
            if file_name.find(file) != -1:
                os.remove(pathname + '/' + file_name);
                file_removed += 1;

    print 'Successfully deleted %s file occurances.' %file_removed;

# Execute directory exists functionality.
path_exists(directory);
