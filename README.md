# Brain-Anomaly-Detection-using-a-Convolutional-AutoEncoder

Early and accurate detection of brain tumors is a critical aspect of modern healthcare. Brain tumors pose a serious threat to the health and quality of life of patients, and early detection can be crucial for effective treatment and better clinical outcomes. According to recent statistical data, brain tumors are the tenth leading cause of death worldwide, in both men and women, underlining the importance of addressing this problem in an effective and timely manner.

Magnetic resonance imaging (MRI) is a medical imaging technique that uses magnetic fields and radio waves to generate detailed images of the inside of the human body. This type of imaging provides valuable information about soft tissues, organs, and internal structures of the body. However, manually identifying brain tumors in medical images, such as magnetic resonance imaging (MRI), is a laborious and error-prone process.

One of the key challenges in applying deep learning to MRI images is the limited availability of large, labeled data sets to train models. This is where Autoencoders gain importance (compared to other architectures such as Convolutional Neural Networks), since these models are a type of unsupervised learning, meaning they do not need a labeled data set to be able to make a classification. That is why, as a solution to this problem, I suggest the use of a Convolutional Autoencoder (CAE). A CAE like the one used in this project only needs images of healthy patients to be trained and subsequently make a classification of healthy patients and those with abnormalities.

This project presents a method for detecting brain gliomas using a three-dimensional Convolutional Autoencoder (CAE) trained exclusively with volumes of various magnetic resonance imaging (MRI) modalities from healthy patients. Three experiments were conducted to contribute to this field. In the first experiment, the negative impact of resizing the dataset to specific dimensions in the presence of significant dimensional variability was demonstrated, and the clustered reshape method was proposed as a more precise alternative. In the second experiment, task transfer was employed to classify patients, and high performance was observed when combining the T1 and FLAIR modalities, while the T2 modality was concluded to be ineffective for glioma detection. Finally, the third experiment demonstrated the impact of acquisition parameters in the datasets on classification and how they can lead to incorrect conclusions.

HOW TO RUN THE CODE?
Once the RSNA-MICCAI dataset ([RSNA-MICCAI Brain Tumor Radiogenomic Classification | Kaggle](https://www.kaggle.com/c/rsna-miccai-brain-tumor-radiogenomic-classification/data)) has been downloaded, there must be 4 files, of which only two are used: the train directory and the train_labels.csv file. In the train set there is a subdirectory for each patient and within each of these subdirectories there are 4 folders containing the DICOM (2D) files for each type of MRI (only 3 are used in this project). The train_labels.csv file contains the labels for each patient to know if they are healthy or contain a glioma. With the preprocessing.py file we separate the healthy patients and those with glioma and also convert the 2D images into 3D volumes.
On the other hand, the rest of the code (the experiments) is in the Jupyter file Anomaly_Brain_Detection.ipynb, where the behavior and the reasoning behind the functions are already described. For a correct execution of the code, the following libraries are needed:
- Torch and torchvision for everything related to the models and tensors.
- Json and os for the treatment of files and directories.
- Matplotlib for making the graphics.
- Numpy for vector and matrix calculations.
- Nibabel for the treatment of medical volumes.
- Scipy for using resizing.
- Sci-Kit Learn for the classifiers, partitions, metrics, …
- Collections for using the Counter function to calculate the modal dimensions.
- Optuna for the optimization of classifier parameters.
- Imblearn for balancing the subsets.

ATTENTION: The comments of the code of this project are currently only available in Spanish. For any further questions, feel free to contact me on my email address: apumarb@gmail.com
