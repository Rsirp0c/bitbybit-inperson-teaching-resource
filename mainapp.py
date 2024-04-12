import streamlit as st
import streamlit.components.v1 as components
import base64
import textwrap
import requests

st.set_page_config(page_title="Bitbybit course material", page_icon="🌎") 

#
def render_svg(svg):
    """Renders the given svg string."""
    b64 = base64.b64encode(svg.encode('utf-8')).decode("utf-8")
    html = r'<img  width=200 src="data:image/svg+xml;base64,%s"/>' % b64
    st.write(html, unsafe_allow_html=True)


url = "https://bitbybitcoding.org/imgs/Logos%20and%20Icons/Logo.svg"
r = requests.get(url) 
svg = r.content.decode() 

def link(text,url):
    col1, col2,  = st.columns([3,1])
    with col1:
        text
    with col2:
        st.link_button('click here', url)
#main page --------------------------------------------------------------------------------------------------------------------------------------------------------------------------------

render_svg(svg) 
st.header(":blue[Bit by Bit] in-person program",divider='orange')
'#### We share the lecture docs here!'
st.link_button('link to programiz', 'https://www.programiz.com/python-programming/online-compiler/')

# st.write('')

link('#### :blue[week 1]: Introduction to Python', 'https://bitbybitcoding.notion.site/L1-Introduction-to-Python-099b550cf99a4e229ceb13eb6f90a19a?pvs=4')
link('#### :blue[week 2]: Basic Syntax and Concepts', 'https://bitbybitcoding.notion.site/L2-Basic-Syntax-and-Concepts-89cfb10d5f0d4f43849f1ed96ab4dd02?pvs=74')
link('#### :blue[week 3]: Control Structures', 'https://bitbybitcoding.notion.site/L3-Control-Structures-f50254152c9b4c0198c8e37edab59217?pvs=74')
link('#### :blue[week 4]: Basic data structure', 'https://bitbybitcoding.notion.site/L4-basic-data-structure-47041119a2a046bcaa3305cc352743a7')
link('#### :blue[week 5]: Functions', 'https://bitbybitcoding.notion.site/L5-functions-70d606ebeb8a40c991ffd818445882b3?pvs=4')
link('#### :blue[week 6]: Streamlit', 'https://bitbybitcoding.notion.site/Crash-Course-on-Streamlit-0c232745f77b414ea8848efcde083dd0?pvs=25')

st.write('')

"#### Don't forget coming to the :rainbow[FRIDAY lecture]! it's on :rainbow[4pm] every week!"
