<img src="./img_sample/plants_icon.png" width="400px"><br>
# Stream GBM
![Streamlit version](https://img.shields.io/badge/Streamlit-v1.14.1-orange)
![Update](https://img.shields.io/badge/Update-2022/12/21-gblue)
![License](https://img.shields.io/badge/License-naro-green)

- ##  About Stream GBM
Stream GBM is a soil type classification tool. 
This tool uses Light GBM model, and output classification accuracy and confusion matrix.<br>

- ##  Analysis Flow<br>

### Analysis
Please input soil data csv file and select some dataset select config.
Click button, automatically start model training(Light GBM).

1. Input soil dataset (__only csv__), drop and drug to file uploader.<br>
2. Select explanatory and objective variables.<br>
3. Click `Start Analysis` button.<br>
4. Show Results.<br>

    - Classification accuracy<br>
    - Confusion matrix<br>
    - Feature importances<br>

<img src="https://github.com/shosuke-13/Stream-GBM/blob/a34b57e5ad72a0f02343762b3b4713cb82af1016/demo/demo_analysis.gif" width="750">

### Visualization
Also, you can check your dataset on this page.
please upload your dataset file again, and check descriptive statistics.<br>

1. Upload Soil dataset file.<br>
2. Check Results and Click `Press to Download`, output descriptive statistics.<br>

<img src="https://github.com/shosuke-13/Stream-GBM/blob/a34b57e5ad72a0f02343762b3b4713cb82af1016/demo/demo_visualization.gif" width="750">
