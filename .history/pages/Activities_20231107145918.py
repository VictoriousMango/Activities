import streamlit as st

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

for i in pdfList:
    with open(i, "rb") as f:
        base64_pdf = base64.b64encode(f.read()).decode('utf-8')

    pdf_display = f'<iframe src="data:application/pdf;base64,{base64_pdf}" width="800" height="800" type="application/pdf"></iframe>'

    st.markdown(pdf_display, unsafe_allow_html=True)