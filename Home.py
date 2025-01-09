from pathlib import Path

import streamlit as st

PASTA_ARQUIVOS = Path (__file__).parent/ 'arquivos'


def sidebar ():
    uploaded_pdfs = st.file_uploader
    ('Adicione seus arquivos pdf',
     type=['.pdf'],
     accept_multiple_files=True
     )
    if not uploaded_pdfs is None:
        for arquivo in PASTA_ARQUIVOS. glob ('*.pdf'):
            arquivo.unlink()
        for pdf in uploaded_pdfs:
            with open(PASTA_ARQUIVOS / pdf.name, 'wb') as
                f.write(pdf.read())



    pass

def main ():
    with st.sidebar:
        sidebar ()


    pass

if __name__ == '__main__':
    main()