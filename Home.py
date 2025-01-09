import streamlit as st


def sidebar ():
    uploaded_pdfs = st.file_uploader
    ('Adicione seus arquivos pdf',
     type=['.pdf',],
     accept_multiple_files=True)
    pass

def main ():
    with st.sidebar:

        sidebar ()


    pass

if __name__ == '__main__':
    main()