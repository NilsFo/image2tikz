import os
import numpy as np
import cv2
import argparse


class TikzImage:

    def __init__(self, rgb_image: np.ndarray, file_name: str) -> None:
        super().__init__()

        # extracting image pixel and meta data
        self.rgb_image = rgb_image
        self.file_name = file_name
        del rgb_image, file_name

        self.width = self.rgb_image.shape[0]
        self.height = self.rgb_image.shape[1]

        # Color infrastructure
        self.color_map: [TikzRGB] = []
        self.pixel_map: [TikzPixel] = []

        # Converting image
        k = 0
        for i in range(self.height):
            for j in range(self.width):
                k = k + 1
                p = int(float(k) / float(self.width * self.height) * 100)
                print(f'Extracting pixel {k}/{self.width * self.height}: {p}%')

                # Access individual RGB channels
                red = self.rgb_image[i, j, 2]
                green = self.rgb_image[i, j, 1]
                blue = self.rgb_image[i, j, 0]

                rgb = TikzRGB(red=red, green=green, blue=blue, image_name=self.file_name)
                if rgb not in self.color_map:
                    self.color_map.append(rgb)

                index = self.color_map.index(rgb)
                pixel = TikzPixel(color_index=index,
                                  y=self.width - i - 1,
                                  x=j
                                  )
                self.pixel_map.append(pixel)


class TikzPixel:

    def __init__(self, x, y, color_index) -> None:
        super().__init__()

        self.x = x
        self.y = y
        self.color_index = color_index

    def to_instruction(self, image_src: TikzImage) -> str:
        color_name = image_src.color_map[self.color_index].color_name()
        return '\\node[draw=none, fill=' + color_name + ', minimum width=1cm, minimum height=1cm] at (' + str(
            self.x) + ',' + str(self.y) + ') {};'


class TikzRGB:

    def __init__(self, red: int, green: int, blue: int, image_name: str) -> None:
        super().__init__()

        self.red = red
        self.green = green
        self.blue = blue
        self.image_name = image_name

    def color_name(self) -> str:
        # unique identifier for the color to be used in tikz
        return 'custom-color-' + self.image_name + '-' + str(self.red) + '-' + str(self.green) + '-' + str(self.blue)

    def to_instruction(self) -> str:
        # the command to be used by the tex compiler
        # defines the color for the pixel to address
        return '\\definecolor{' + self.color_name() + '}{RGB}{' + str(self.red) + ',' + str(self.green) + ',' + str(
            self.blue) + '}'

    def __str__(self) -> str:
        return f'tikzRGB: ({self.red},{self.green},{self.blue})'

    def __eq__(self, other) -> bool:
        if isinstance(other, TikzRGB):
            return (
                    self.red == other.red and
                    self.green == other.green and
                    self.blue == other.blue
            )
        return False


def image2tikz(input_file_path: str) -> None:
    if not os.path.exists(input_file_path):
        print(f'Could not find image {input_file_path}.')
        raise FileNotFoundError()

    # converting file name
    file_name = os.path.splitext(os.path.basename(input_file_path))[0]
    file_name = str(file_name).lower().strip()
    while '  ' in file_name:
        file_name = file_name.replace('  ', '')
    file_name = file_name.replace(' ', '-').strip('-').strip()
    out_file_name = file_name + '.pgf'

    # Loading the image
    image = cv2.imread(input_file_path)

    # Converting pixels
    tikz_image = TikzImage(rgb_image=image, file_name=file_name)

    # Writing out file
    f = open(out_file_name, 'w')
    f.write('\\begin{tikzpicture}\n')

    # Writing Color Map
    print('Writing Color Map...')
    f.write('\n\t%COLOR MAP\n')
    for color in tikz_image.color_map:
        f.write('\t' + color.to_instruction() + '\n')

    # Writing Pixel
    print('Writing image...')
    f.write('\n\n\t%IMAGE PIXEL\n')
    for pixel in tikz_image.pixel_map:
        f.write('\t' + pixel.to_instruction(image_src=tikz_image) + '\n')

    f.write('\\end{tikzpicture}\n')
    f.close()

    # all done!
    print(f'Finished Converting: {out_file_name}')


def is_dev_mode() -> bool:
    in_pycharm = False
    try:
        in_pycharm = "PYCHARM_HOSTED" in os.environ
    except Exception as e:
        return False

    return in_pycharm


if __name__ == '__main__':
    # First: Check if this instance runs in pycharm
    if is_dev_mode():
        print('Dev mode engaged.')
        image2tikz(input_file_path='example/mandrill.png')
        exit(0)

    # If not, let's read arguments
    parser = argparse.ArgumentParser(description='Runs the project_lotte scheduling.')
    parser.add_argument('-i', '--image_input_path', type=str, required=True,
                        help='Path of the input image to be parsed.')

    # Parsing the arguments
    args = parser.parse_args()

    # running main script
    image2tikz(input_file_path=args.image_input_path)
