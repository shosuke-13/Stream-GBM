<img src="./img_sample/plants_icon.png" width="400px"><br>
# Stream GBM
![Streamlit version](https://img.shields.io/badge/Streamlit-v1.14.1-orange)
![Update](https://img.shields.io/badge/Update-2022/12/22-blue)
![License](https://img.shields.io/badge/License-naro-green)

- ##  About Stream GBM
Stream GBM is a soil type classification tool. 
This tool uses Light GBM model, and output classification accuracy and confusion matrix.<br>

- ## Target Dataset
The purpose of this analysis tools is classification of soil types.Please input 2 soil csv dataset (model training dataset and classification dataset). Model training dataset needs explanatory variables and a objective variable. Classification dataset needs only explanatory variable. You can input category variables in these dataset, but please select category variables.<br>

*!Note* : Before classification soil types, drop None cells in classification dataset.

- ##  Analysis Flow<br>
### Analysis
Please input soil data csv file and select some dataset configuration.
Click button, automatically start model training(Light GBM).

1. Input soil dataset (__only csv__), drop and drug to file uploader. 2 tabs exist, model training dataset and classification dataset.
   Please upload both dataset files.
2. Select category,explanatory and objective variables.

<img src=https://github.com/shosuke-13/Stream-GBM/blob/05e1031d82630108b7c1adbff791cfa46cc11449/demo/demo_input.gif" width="650">

3. Click `Start Analysis` button.
4. Show Results.
      Three tabs. <br>
    - Classification accuracy
    - Confusion matrix
    - Feature importances　　

<img src="https://github.com/shosuke-13/Stream-GBM/blob/05e1031d82630108b7c1adbff791cfa46cc11449/demo/demo_model.gif" width="650">

### Visualization
Also, you can check your dataset on this page.
please upload your dataset file again, and check descriptive statistics.<br>

1. Upload Soil dataset file.<br>
2. Check Results and Click `Press to Download`, output descriptive statistics.<br>

<img src="https://github.com/shosuke-13/Stream-GBM/blob/a34b57e5ad72a0f02343762b3b4713cb82af1016/demo/demo_visualization.gif" width="600">
