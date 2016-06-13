# Program to copy a complete directory from one location to another.

# Import os library to access some buit-in functions for access directory name, status etc.
import os;

# Create base path.
base_path = os.path.expanduser('~') + '/Desktop/';

# Print details about program to user.
print '\n' + '*' * 10 + ' Copy directory with Pyhton ' + '*' * 10;
print '\n Enter path relative to desktop i.e only folders that exists on desktop can be copied.\n';
print '  Note:- Enter value inside Quotes (Example >> Hello: \'World\')\n'

# Path where directory will be copied.
directory_to_path = base_path + input('Enter path where data will be copied: ');

# Path from which directory should be copied.
directory_from_path = base_path + input('\nEnter path from where data would be copied: ');

# Check if directory exists in to_path, if not create new directory.
def create_directory(path):
    'Creates a new directory if not found in the provided path.'

    # Create logs file.
    file_log = open('file_log.txt', 'a');

    try:
        file_log.write('******** Checking for directory ********\n');
        dir_check = os.path.dirname(path);
        file_log.write('Directory path: ' + dir_check);
        os.stat(dir_check);
    except:
        file_log.write('!!!!! Directory not found !!!!!\n');
        file_log.write('Creating new directory....\n');
        os.makedirs(dir_check);
        file_log.write('!!!!! Directory created successfully !!!!!\n');
        file_log.write('-' * 20);

    file_log.close();

# Copy files in directives recursively to another postion.
def copy_files():
    'Copy complete directory tree from one location to another.'

    # Directory to loop from.
    directory_list = [];
    inner_directory = '';

    # Write the file_structure in a file.
    file_structure = open('file_structure.txt', 'w');

    # Loop directory tree of directory_from_path to copy it's content in directory_to_path.
    for (pathname, dirname, filename) in os.walk(directory_from_path):
        file_structure.write('Directory: ' + str(dirname) + ' File: ' + str(filename) + '\n');
        for directory in dirname:
            create_directory(directory_to_path + inner_directory + directory + '/');
        for file_name in filename:
            if file_name != '.DS_Store': # Don't copy mac temp files.
                read_from = open(pathname + '/' + file_name, 'r');
                write_to = open(directory_to_path + inner_directory + file_name, 'w');
                write_to.write(read_from.read());
                read_from.close();
                write_to.close();
            else:
                print '-------- Got mac temp file: ' + file_name + ' ------------';
        for index in range(len(dirname), 0, -1):
            directory_list.append(inner_directory + dirname[index - 1]);
        if len(directory_list):
            inner_directory =  directory_list.pop() + '/';

    file_structure.close();

# Create initial directories if not exists.
create_directory(directory_to_path);

# Start copy.
copy_files();
