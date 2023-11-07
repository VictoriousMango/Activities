import streamlit as st
import base64

pdfList = [
    'a taped tale.pdf', 
    'Cache of Rymes.pdf', 
    'COLLOQUY OF THE MIND SEMINAR.pdf', 
    'expresso Burst your fears.pdf', 
    'GENZ ARGOTS TREZIRE.pdf', 
    'Persona Verse Trezire .pdf',
    'psychemon.pdf',
    'TREZIRE BROCHURE PRESENTS PSYCHESTRA.pdf',
    'TREZIRE Just Dance .pdf',
    'TREZIRE MAIN POSTER.pdf']

tab1, tab2, tab3, tab4, tab5, tab6, tab7, tab8, tab9, tab10 = st.tabs([i[:-4] for i in pdfList])

def displayPDF(filePath):
    with open(filePath, "rb") as f:
        base64_pdf = base64.b64encode(f.read()).decode('utf-8')

    pdf_display = f'<iframe src="data:application/pdf;base64,{base64_pdf}" width="800" height="800" type="application/pdf"></iframe>'

    st.markdown(pdf_display, unsafe_allow_html=True)

with tab1:
    displayPDF(pdfList[0])
with tab2:
    displayPDF("Cache of Rymes.pdf")
with tab3:
    displayPDF(pdfList[2])
with tab4:
    displayPDF(pdfList[3])
with tab5:
    displayPDF(pdfList[4])
with tab6:
    displayPDF(pdfList[5])
with tab7:
    displayPDF(pdfList[6])
with tab8:
    displayPDF(pdfList[7])
with tab9:
    displayPDF(pdfList[8])
with tab10:
    displayPDF(pdfList[9])

