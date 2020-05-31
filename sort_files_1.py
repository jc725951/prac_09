
import os




def main():

    """put files in folders sama as their extensions."""

    os.chdir("FilesToSort")

    for filename in os.listdir('.'):

        # take files without any directories

        if os.path.isdir(filename):

            continue



        extension = filename.split('.')[-1]


        try:

            os.mkdir(extension)

        except FileExistsError:

            pass

        print("{}/{}".format(extension, filename))

        os.rename(filename, "{}/{}".format(extension, filename))





main()