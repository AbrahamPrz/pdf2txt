# import module
from pdf2image import convert_from_path
from os import path, makedirs
from pytesseract import pytesseract
from tqdm.auto import tqdm

# pdf_to_image_to_txt converts a pdf to txt file by converting pdf to image and then using pytesseract to convert image to txt
def pdf_to_image_to_txt(pdf_path, output_path=None):
    output_path = path.basename(pdf_path)[:-4] if output_path is None else output_path
    if not path.exists(output_path):
        makedirs(output_path)
    # Convert pdf to image
    images = convert_from_path(pdf_path)

    for i in tqdm(range(len(images)), desc="Converting pdf to txt"):
        # Defining paths to tesseract.exe and the image we would be using
        path_to_tesseract = r"/usr/bin/tesseract"
        # Providing the tesseract executable location to pytesseract library
        pytesseract.tesseract_cmd = path_to_tesseract
        # Passing the image object to image_to_string() function to extract the text from the image
        text = pytesseract.image_to_string(images[i]).strip()
        with open(output_path + f"/page{i}" + ".txt", "w") as f:
            f.write(text)


if __name__ == "__main__":
    current_dir = path.abspath(path.dirname(__file__))
    pdf = path.join(current_dir, "example.pdf")
    pdf_to_image_to_txt(pdf)
