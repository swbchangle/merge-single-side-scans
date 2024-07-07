import sys
from pypdf import PdfReader, PdfWriter

if __name__ == "__main__":
    args = sys.argv[1:]
    print("Merging")
    print(f"\t{args[0]}")
    odd_pages_pdf = PdfReader(args[0])
    print(f"\t{args[1]}")
    even_pages_pdf = PdfReader(args[1])
    out_pdf = PdfWriter()

    assert odd_pages_pdf.get_num_pages() == even_pages_pdf.get_num_pages(), "The single-scan inputs must have the same number of pages" 

    nr_pages = odd_pages_pdf.get_num_pages()
    for i in range(nr_pages):
        out_pdf.add_page(odd_pages_pdf.get_page(i))
        out_pdf.add_page(even_pages_pdf.get_page(nr_pages - i -1))
    
    print("into ")
    print(f"\t{args[2]}")
    with open(args[2], "wb") as out:
        out_pdf.write(out)