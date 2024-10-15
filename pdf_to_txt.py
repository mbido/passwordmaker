import PyPDF2

def pdf_to_text(pdf_file, txt_file):
  """
  Convertit un fichier PDF en fichier texte.

  Args:
    pdf_file: Le chemin d'accès au fichier PDF.
    txt_file: Le chemin d'accès au fichier texte de sortie.
  """
  with open(pdf_file, 'rb') as pdf:
    pdf_reader = PyPDF2.PdfReader(pdf)
    
    with open(txt_file, 'w') as text:
      for page_num in range(len(pdf_reader.pages)):
        page = pdf_reader.pages[page_num]
        text.write(page.extract_text())

# Exemple d'utilisation
pdf_to_text('mon_livre.pdf', 'mon_livre.txt')