import fitz  # mila manao pip install PyMuPDF


def analyser_pdf(chemin_pdf):
    doc = fitz.open(chemin_pdf)
    texte_total = ""

    for page_num, page in enumerate(doc):
        texte = page.get_text()
        texte_total += f"\n--- Page {page_num + 1} ---\n{texte}\n"

    doc.close()
    return texte_total


"""if __name__ == "__main__":
    chemin = "teste.pdf" 
    texte = analyser_pdf(chemin)
    print(texte)"""
