
# Author     : Tomas O'Malley
# Student ID : G00361128 (@gmit.ie)
# Course     : Software Development GA_KSOAG_H08 Y3
# Module     : Graph Theory  -(48901)
# Program    : NFA Builder - Commandd line arguments 
# Due Date 	 : 03/04/2020


import argparse
if __name__ == '__main__':
    parser = argparse.ArgumentParser(
        description="NFA Program Help Guide"
    )

    parser.add_argument('REGEX', help=" REGEX")
    parser.add_argument('STRING', help="STRING")

    args = parser.parse_args()

    print(args)