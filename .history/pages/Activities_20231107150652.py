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

with tab1:
    st.write(pdfList[1])
with tab2:
    st.write(pdfList[2])
with tab3:
    st.write(pdfList[3])
with tab4:
    st.write(pdfList[4])
with tab5:
    st.write(pdfList[5])
with tab6:
    st.write(pdfList[6])
with tab7:
    st.write(pdfList[7])
with tab8:
    st.write(pdfList[8])
with tab9:
    st.write(pdfList[9])
with tab10:
    st.write(pdfList[10])


for i in pdfList:
    with open(i, "rb") as f:
        base64_pdf = base64.b64encode(f.read()).decode('utf-8')

    pdf_display = f'<iframe src="data:application/pdf;base64,{base64_pdf}" width="800" height="800" type="application/pdf"></iframe>'

    st.markdown(pdf_display, unsafe_allow_html=True)