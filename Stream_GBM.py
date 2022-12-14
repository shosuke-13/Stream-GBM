import streamlit as st
import base64
import streamlit.components.v1 as stc


#base UI config, reload -> apply other pages
def ui_analysis():        
    #Header
    st.image('./img_sample/plants_icon.png',width=500)
    st.title('LightGBM Classification For Prediction Of Soil-Types')
    st.info('Last Update : 2022/12/07')
    

#display GIF on home
def display_GIF():
    file_ = open("./img_sample/test.gif", "rb")
    contents = file_.read()
    data_url = base64.b64encode(contents).decode("utf-8")
    file_.close()

    st.markdown(
        f'<img src="data:image/gif;base64,{data_url}" alt="cat gif">',
        unsafe_allow_html=True,
        )

def md_explain():
    st.markdown('---')
    st.markdown('This application can analysis soil table-data.')
        
    
def main():
    ui_analysis()
    display_GIF()
    md_explain()
    
    
if __name__ == '__main__':
    main()
