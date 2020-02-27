## Breast Cancer Cell Detection


#### Please limit yourself to 4 hours time!

You work for the data team at a local research hospital. You've been tasked with developing a means to help doctors diagnose breast cancer. You've been given data about biopsied breast cells; where it is benign (not harmful) or malignant (cancerous).

* What features of a cell are the largest drivers of malignancy? Build a model that predicts whether a given biopsied breast cell is benign or malignant.
* What features drive your false positive rate for your model you derived above, what features drive your false negative rate?
* How would a physician use your product?
* There is a non-zero cost in time and money to collect each feature about a given cell. How would you go about determining the most cost-effective method of detecting malignancy?

We are looking for a coherent data-story - think of this challenge as building the MVP of a data product. That means you should be able to explain the “why” behind the technical choices you made and show that you made those choices with your user needs in mind. This is a deliberately open-ended question that provides a chance to showcase your EDA, analysis, and presentation skills.

Follow data challenge best practices. Pay particular attention to how you present your findings - communicate your critical thinking, **tell a data story.** Please code and annotate your analysis in a Jupyter notebook. Please place your submission in the submission folder.

### Deliverables:

* Your final software deliverable should be a REST API (locally-hosted - in future weeks you will containerize and deploy to AWS) that you will be expected to demo
  * [REST API + React Front End tutorial](https://towardsdatascience.com/create-a-complete-machine-learning-web-application-using-react-and-flask-859340bddb33)
  * [Build an API using Flask](https://github.com/TannerGilbert/Tutorials/tree/master/Deploying%20your%20ML%20Model)
  * [Tutorial: Building a RESTful API with Flask](https://kite.com/blog/python/flask-restful-api-tutorial/)
  * [How to Build RESTful APIs with Python and Flask](https://www.codementor.io/dongido/how-to-build-restful-apis-with-python-and-flask-fh5x7zjrx)
  * [Deploying an ML Model as REST API](https://towardsdatascience.com/deploying-a-machine-learning-model-as-a-rest-api-4a03b865c166)
  * Try and limit yourself to 4 hours for the analysis
    * After the 4 hour analysis is done leave yourself enough time to put together a presentation + API

### Please push your submissions to the Submissions sub-folder with the naming convention: lname_fname_DC3.

The dataset consists of 699 cells for which you have the following features:

Sample code number: id number
Clump Thickness: 1 - 10
Uniformity of Cell Size: 1 - 10
Uniformity of Cell Shape: 1 - 10
Marginal Adhesion: 1 - 10
Single Epithelial Cell Size: 1 - 10
Bare Nuclei: 1 - 10
Bland Chromatin: 1 - 10
Normal Nucleoli: 1 - 10
Mitoses: 1 - 10
Class: (2 for benign, 4 for malignant)

The dataset is also available here: https://archive.ics.uci.edu/ml/machine-learning-databases/breast-cancer-wisconsin/breast-cancer-wisconsin.data
