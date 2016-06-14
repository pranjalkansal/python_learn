# Program to delete a file in complete directory tree.

# Import os library to access some buit-in functions for access directory name, status etc.
import os;

# Print details about program to user.
print '\n' + '*' * 10 + ' Remove directory with Pyhton ' + '*' * 10;
print '  Note:- Enter value inside Quotes (Example >> Hello: \'World\')\n'

# Get users input for directory path.
directory = input('Enter directory which should be deleted: ');

if directory[0] == '~':
    directory = directory.replace('~', os.path.expanduser('~'), 1);

if directory[-1] == '/':
    directory = directory[0:-1];

def path_exists(directory):
    'Check if the path entered by user exists'
    try:
        os.stat(os.path.dirname(directory));
        print 'Directory found: Initiating file remove......';
        delete_directory(directory);
    except:
        print 'Directory not found: Aborting.......';

def delete_directory(directory):
    'Delete complete directory tree'

    # Track number of files and directories deleted.
    file_removed = 0;
    directories_removed = 0;

    # Directory track.
    directory_list = [directory];
    inner_directive = '';

    dir_file = open('dir_structure.txt', 'w');
    for (pathname, dirname, filename) in os.walk(directory):
        for file_name in filename:
            os.remove(pathname + '/' + file_name);
            file_removed += 1;
        for dir_name in dirname:
            directory_list.append(pathname + '/' + dir_name);
            dir_file.write(pathname + '/' + dir_name + '\n\n');

    while len(directory_list):
        os.rmdir(directory_list.pop());
        directories_removed += 1;
    dir_file.close();
    print 'Successfully deleted %s file and %s directories.' %(file_removed, directories_removed);

# Execute directory exists functionality.
path_exists(directory);
