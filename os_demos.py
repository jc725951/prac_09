

import os

def main():


    print("Starting directory is: {}".format(os.getcwd()))



    # To change in whatever directory you want

    os.chdir('Lyrics/Christmas')



    # display all files of directory

    print("Files in {}:\n{}\n".format(os.getcwd(), os.listdir('.')))



    #To avoid crash if the file already exists

    try:

        os.mkdir('temp')

    except FileExistsError:

        pass



    # Loop through each file in the (current) directory

    for filename in os.listdir('.'):

        # Ignore directories, just process files

        if os.path.isdir(filename):

            continue



        new_name = get_fixed_filename(filename)

        print("Renaming {} to {}".format(filename, new_name))

        os.rename(filename, new_name)


def get_fixed_filename(filename):

    """Return a 'fixed' version of filename."""

    new_name = filename.replace(" ", "_").replace(".TXT", ".txt")

    return new_name


def demo_walk():

    """Process all subdirectories using os.walk()."""

    os.chdir('Lyrics')

    for directory_name, subdirectories, filenames in os.walk('.'):

        print("Directory:", directory_name)

        print("\tcontains subdirectories:", subdirectories)

        print("\tand files:", filenames)

        print("(Current working directory is: {})".format(os.getcwd()))



        # loop to rename the files

        for filename in filenames:

            full_name = os.path.join(directory_name, filename)

            new_name = os.path.join(directory_name, get_fixed_filename(filename))

            os.rename(full_name, new_name)

main()
