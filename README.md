<img src="./img_sample/plants_icon.png" width="400px"><br>
# Stream GBM
![Streamlit version](https://img.shields.io/badge/Streamlit-v1.14.1-orange)

- ###  About Stream GBM
Stream GBM is a soil type classification tool. 
This tool uses Light GBM model, and output classification accuracy and confusion matrix.<br>

- ###  Analysis Flow<br>

#### Page : Analysis
1. Input soil dataset (__only csv__), drop and drug to file uploader.<br>
2. Select explanatory and objective variables<br>
3. Click `Start Analysis` button<br>

![demo analysis](https://github.com/shosuke-13/Stream-GBM/blob/a34b57e5ad72a0f02343762b3b4713cb82af1016/demo/demo_analysis.gif)

#### Page : Results
You can check these results.<br>

1. Classification accuracy<br>
2. Confusion matrix<br>
3. Feature importances<br>

Click `Press to Download`, output predicted Soil types csv file.

![demo visualization](https://github.com/shosuke-13/Stream-GBM/blob/a34b57e5ad72a0f02343762b3b4713cb82af1016/demo/demo_visualization.gif)
