# Stream GBM
![Streamlit version](https://img.shields.io/badge/Streamlit-v1.14.1-orange)
![Update](https://img.shields.io/badge/Update-2023/5/24-blue)
![License](https://img.shields.io/badge/License-naro-green)

<img src="https://github.com/shosuke-13/Stream-GBM/blob/main/icon/plants_icon.png" width="400px"><br>

##  About Stream GBM & Target Dataset
Stream GBM is a soil type classification tool. 
This tool uses Light GBM model, and output classification accuracy and confusion matrix.<br>
The purpose of this analysis tools is classification of soil types.Please input 2 soil csv dataset (model training dataset and classification dataset). Model training dataset needs explanatory variables and a objective variable. Classification dataset needs only explanatory variable. You can input category variables in these dataset, but please select category variables.<br>

##  Analysis Flow<br>
### __Model Training & Predict__
Please input soil data csv file and select some dataset configuration.
Click button, automatically start model training(Light GBM).
First, input your dataset, drop and drug to file uploader. 2 tabs exist, model training dataset and classification dataset.
Please upload both dataset files. Next, Select category,explanatory and objective variables.

<img src="https://github.com/shosuke-13/Stream-GBM/blob/05e1031d82630108b7c1adbff791cfa46cc11449/demo/demo_input.gif" width="650">

Click `Start Analysis`, and then, check results.

<img src="https://github.com/shosuke-13/Stream-GBM/blob/05e1031d82630108b7c1adbff791cfa46cc11449/demo/demo_model.gif" width="650">

### __Visualization__
Also, you can check your dataset on this page.
please upload your dataset file again, and check descriptive statistics.
Upload Soil dataset file and check results. if you click `Press to Download`, you can output descriptive statistics.<br>

<img src="https://github.com/shosuke-13/Stream-GBM/blob/a34b57e5ad72a0f02343762b3b4713cb82af1016/demo/demo_visualization.gif" width="600">
