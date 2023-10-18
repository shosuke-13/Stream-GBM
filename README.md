![Streamlit version](https://img.shields.io/badge/Streamlit-v1.14.1-orange)
![Update](https://img.shields.io/badge/Update-2023/10/18-blue)
![License](https://img.shields.io/badge/License-MIT-green)
# Stream-GBM
<img src=https://github.com/shosuke-13/Stream-GBM/blob/main/images/title_image.png width="1000">
&nbsp;

- [Stream-GBM](#stream-gbm)
- [About Stream GBM \& Target Dataset](#about-stream-gbm--target-dataset)
- [Cutom Theme](#cutom-theme)
  - [__1. ML model__](#1-ml-model)
  - [__2. Visualization__](#2-visualization)
  - [__3. Create Sample Dataset__](#3-create-sample-dataset)
  - [__4. Dashboard__](#4-dashboard)
- [References](#references)

&nbsp;
####  About Stream GBM & Target Dataset
Stream-GBM is a ML classification tool. 
This tool uses Light GBM model, and output classification accuracy and confusion matrix.
The purpose of this analysis tools is that user can simple ML analysis more easier.Please input two csv dataset (model training dataset and classification dataset). Model training dataset needs explanatory variables and a objective variable. Classification dataset needs only explanatory variable. You can input category variables in these dataset, but please select category variables.<br>

&nbsp;
#### Cutom Theme
```toml
[theme]
base="dark"
primaryColor="#60b5a5"
backgroundColor="#43454a"
secondaryBackgroundColor="#60b5a5"
```
<img src=https://github.com/shosuke-13/Stream-GBM/blob/main/images/custom_theme.png width="1000">


&nbsp;
## __1. ML model__
- #### Model training and predict page
On this page, you can perform a classification task using a machine learning model.
You can freely select the features to use for prediction using a select box.

<img src=https://github.com/shosuke-13/Stream-GBM/blob/main/demo/analysis_page.gif width="450">

&nbsp;
## __2. Visualization__
- #### Dataset visualization page
On this page, you can check the descriptive statistics of the data and examine the correlation.

<img src=https://github.com/shosuke-13/Stream-GBM/blob/main/demo/visualization_page.gif width="450">


## __3. Create Sample Dataset__
- #### Create N rows x M columns sample dataset to test this application
You can create a sample dataset and test the functionality.
By moving the slider, you can freely create and output a dataset with 1 to 1000 rows and 1 to 10 columns.

<img src=https://github.com/shosuke-13/Stream-GBM/blob/main/demo/create_sample_page.gif width="450">


## __4. Dashboard__
- #### Check and EDA your dataset using PyGwalker
You can create scatter plots, bar charts, and line graphs using PyGWalker.
You can efficiently perform exploratory data analysis (EDA) on this page.

<img src=https://github.com/shosuke-13/Stream-GBM/blob/main/demo/dashboard_page.gif width="650">

***
#### References
- [Streamlit Documentation](https://docs.streamlit.io/)
- [PyGWalker](https://github.com/Kanaries/pygwalker)
