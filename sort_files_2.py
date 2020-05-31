
import os

def main():

    """Move file according to user choice"""

    # dictionary to give the right path to files to their given names

    extension_to_category = {}

    os.chdir("FilesToSort")

    for filename in os.listdir('.'):

        # Ignore directories, just process files

        if os.path.isdir(filename):

            continue



        extension = filename.split('.')[-1]

        if extension not in extension_to_category:

            category = input("What category would you like to sort {} files into? ".format(extension))

            # Now we can map this new extension to a folder name

            extension_to_category[extension] = category

            try:

                #give exception if user choose ann exicting folder
                os.mkdir(category)

            except FileExistsError:

                pass


        os.rename(filename, "{}/{}".format(extension_to_category[extension], filename))





main()