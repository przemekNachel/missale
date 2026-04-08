from pypdf import PdfReader, PdfWriter, PageObject, Transformation


def merge_fixed_rotation(file1, file2, output_file):
    reader1 = PdfReader(file1) if file1 != "None.pdf" else None
    reader2 = PdfReader(file2) if file2 != "None.pdf" else None
    writer = PdfWriter()

    A4_W = 595.28
    A4_H = 841.89

    new_page = PageObject.create_blank_page(width=A4_W, height=A4_H)

    pages = []
    pages.append(reader2.pages[0]) if reader2 else None
    pages.append(reader1.pages[0]) if reader1 else None

    for i, p in enumerate(pages):
        p.mediabox.right = 1000
        p.mediabox.top = 1000

        ty_offset = (A4_H / 2) if i == 0 else 0

        trans = Transformation().rotate(90).translate(tx=A4_W, ty=ty_offset)
        p.add_transformation(trans)

        new_page.merge_page(p)

    writer.add_page(new_page)

    with open(output_file, "wb") as f:
        writer.write(f)


def merge_two_pages(file1, file2, output_file):
    merger = PdfWriter()
    merger.append(file1)
    merger.append(file2)
    merger.write(output_file)
# merge_fixed_rotation("1.pdf", "2.pdf", "combined_a4.pdf")
