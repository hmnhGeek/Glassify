# GLASSIFY

Glassify is a command line tool that gives a glassy effect to your images. It requires a positive integer **power index**, 8 being the optimal, which decides how much glassy effect is to be applied on the image.

## Power Index
Power index decides how glassy the image will become. A power index of 1,2,3 and 4 is **not so glassy** instead it is just jumpled pieces of the original image. A power index of 5, 6, 7, 8, 9, 10, with 8 being optimal, gives you an appreciable glassy effect. Power index 11, 12, and after that becomes so glassy that your eyes will perceive the image as original image.

## Usage
      usage: glassify.py [-h] [-f F] [-p P] [-s]

      optional arguments:
      -h, --help       show this help message and exit
      -f F, --file F   Pass image file.
      -p P, --power P  Pass glass effective value.
      -s, --save       To save or not.

## Sample
![Show Piece](https://github.com/hmnhGeek/Glassify/blob/master/samples/showpiece.jpg)

Although, a magnified view of the glassed image can convince you for the effectiveness of the tool. You can view some more images **(magnified)** in the samples folder.
