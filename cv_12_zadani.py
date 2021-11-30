from PIL import Image

# Na bile pozadi o zadane velikosti nakreslete cerny ctverec o zadane strane,
# jehoz stred bude umisten do stredu obrazku.

BLACK = (0, 0, 0)
WHITE = (255, 255, 255)


# def square(size: int = 150, a: int = 75) -> None:
#     im = Image.new("RGB", (size, size), WHITE)
#     for x in range(size//2 - a//2, size - a//2):
#         for y in range(size//2 - a//2, size - a//2):
#             im.putpixel((x, y), BLACK)
#     im.show()
#
# square()


# Nakreslete sachovnicovy vzor o zadane velikosti obrazku a sirce pruhu.


def chessboard(image: int = 240, stripe: int = 30) -> None:
    im = im = Image.new("RGB", (image, image), WHITE)
    for x in range(image):
        for y in range(image):
            if ((x + stripe) // stripe + (y + stripe) // stripe) % 2 != 1:
                im.putpixel((x, y), BLACK)
            else:
                im.putpixel((x, y), WHITE)
    im.show()

chessboard()


# Napiste funkci, ktera odstrani z daneho obrazku zelenou barvu (alternativne
# cervenou nebo modrou)


def without_green(filename: str) -> None:
    im = Image.open(filename)
    im = im.convert("RGB")
    width, height = im.size
    for x in range(width):
        for y in range(height):
            (r, g, b) = im.getpixel((x, y))
            im.putpixel((x, y), (r, 0, b))
    im.show()

without_green("xmas_tree.jpg")


# Napiste funkci, ktera dany obrazek prevrati vzhledem k jeho vertikalni ose.


def invert(filename: str) -> None:
    im = Image.open(filename)
    im_inverted = Image.new("RGB", im.size, WHITE)
    width, height = im.size
    for x in range(width):
        for y in range(height):
            (r, g, b) = im.getpixel((x, y))
            im_inverted.putpixel((-x, y), (r, g, b))

    im_inverted.show()

invert("xmas_tree.jpg")
