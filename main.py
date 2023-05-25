import streamlit as st
import base64
import streamlit.components.v1 as stc


#base UI config, reload -> apply other pages
def ui_analysis():        
    #Header
    #st.image('./icon/plants_icon.png',width=500)
    st.title('LightGBM Classification for CSV Dataset')
    

#display GIF on home
def display_GIF():
    file_ = open("./icon/Force.gif", "rb")
    contents = file_.read()
    data_url = base64.b64encode(contents).decode("utf-8")
    file_.close()

    st.markdown(
        f'<img src="data:image/gif;base64,{data_url}" alt="cat gif"  width="700">',
        unsafe_allow_html=True,
        )
        
    
def main():
    ui_analysis()
    display_GIF()
    
    st.markdown('---')
    st.markdown('[Stream GBM : README](https://github.com/shosuke-13/Stream-GBM)')
    
    
if __name__ == '__main__':
    main()
