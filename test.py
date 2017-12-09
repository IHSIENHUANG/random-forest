import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.ensemble import RandomForestClassifier
from sklearn.metrics import accuracy_score
from sklearn.metrics import confusion_matrix

from sklearn.feature_extraction.text import CountVectorizer
import pdb

# File Paths
INPUT_PATH = "data.csv"
#OUTPUT_PATH = "output.csv"

# Headers
HEADERS = ['class', 'cap-shape', 'cap-surface', 'cap-color', 'bruises', 'odor', 'gill-attachment', 'gill-spacing', 'gill-size', 'gill-color', 'stalk-shape', 'stalk-root', 'stalk-surface-above-ring', 'stalk-surface-below-ring', 'stalk-color-above-ring', 'stalk-color-below-ring', 'veil-type', 'veil-color', 'ring-number', 'ring-type', 'spore-print-color', 'population', 'habitat']



def read_data(path):
    """
    Read the data into pandas dataframe
    :param path:
    :return:
    """
    data = pd.read_csv(path)
    return data


def get_headers(dataset):
    """
    dataset headers
    :param dataset:
    :return:
    """
   # print ("get header" dataset.columns.values)
    return dataset.columns.values


def add_headers(dataset, headers):
    """
    Add the headers to the dataset
    :param dataset:
    :param headers:
    :return:
    """
    dataset.columns = headers
    return dataset


def data_file_to_csv():
    """

    :return:
    """

    # Headers
    HEADERS = ['class', 'cap-shape', 'cap-surface', 'cap-color', 'bruises', 'odor', 'gill-attachment', 'gill-spacing', 'gill-size', 'gill-color', 'stalk-shape', 'stalk-root', 'stalk-surface-above-ring', 'stalk-surface-below-ring', 'stalk-color-above-ring', 'stalk-color-below-ring', 'veil-type', 'veil-color', 'ring-number', 'ring-type', 'spore-print-color', 'population', 'habitat']


    # Load the dataset into Pandas data frame
    dataset = read_data(INPUT_PATH)
    # Add the headers to the loaded dataset
    dataset = add_headers(dataset, headers)
    # Save the loaded dataset into csv format
    dataset.to_csv(OUTPUT_PATH, index=False)
    print "File saved ...!"


def split_dataset(dataset, train_percentage, feature_headers, target_header):
    """
    Split the dataset with train_percentage
    :param dataset:
    :param train_percentage:
    :param feature_headers:
    :param target_header:
    :return: train_x, test_x, train_y, test_y
    """

    # Split dataset into train and test dataset
  
    train_x, test_x, train_y, test_y = train_test_split(dataset[feature_headers], dataset[target_header], 
                                                       train_size=train_percentage)
    '''
    for row in train_x:
	print("%s" %row)
    for row2 in test_x:
	print("%s" %row2)
    '''
    return train_x, test_x, train_y, test_y


def handel_missing_values(dataset, missing_values_header, missing_label):
    """
    Filter missing values from the dataset
    :param dataset:
    :param missing_values_header:
    :param missing_label:
    :return:
    """

    return dataset[dataset[missing_values_header] != missing_label]


def random_forest_classifier(features, target):
    """
    To train the random forest classifier with features and target data
    :param features:
    :param target:
    :return: trained random forest classifier
    """
    clf = RandomForestClassifier(random_state =10 ,max_features=10)
    clf.fit(features, target)
    return clf


def dataset_statistics(dataset):
    """
    Basic statistics of the dataset
    :param dataset: Pandas dataframe
    :return: None, print the basic statistics of the dataset
    """
    print dataset.describe()



    """
    Main function
    :return:
    """
def main():
    # Load the csv file into pandas dataframe
    dataset = pd.read_csv("data.csv")
    # Get basic statistics of the loaded dataset
    #dataset_statistics(dataset)

    # Filter missing values
    #print ("where is my data")
    #print("target %s" %HEADERS[0])
    #print("other %s"  %HEADERS[1:])
    left = 10 
    train_x, test_x, train_y, test_y = split_dataset(dataset, 0.5, HEADERS[left:], HEADERS[0])#HEADER[1:] other feature|  HEADERS[0] : target feature
    # Train and Test dataset size details
    print "Train_x Shape :: ", train_x.shape
    print "Train_y Shape :: ", train_y.shape
    print "Test_x Shape :: ", test_x.shape
    print "Test_y Shape :: ", test_y.shape
	
    print "DEBUG"
    # Create random forest classifier instance
    #vec2 = CountVectorizer()
    #Y = vec2.fit.transform(train_y)  
    trained_model = random_forest_classifier(train_x, train_y)
    #trained_model = random_forest_classifier(train_x, train_y)
    print "Trained model :: ", trained_model

    predictions = trained_model.predict(test_x)


    for i in xrange(0, 5):
        print "Actual outcome :: {} and Predicted outcome :: {}".format(list(test_y)[i], predictions[i])
    
    print "Train Accuracy :: ", accuracy_score(train_y, trained_model.predict(train_x))
    print "Test Accuracy  :: ", accuracy_score(test_y, predictions)
    print " Confusion matrix ", confusion_matrix(test_y, predictions)

if __name__ == "__main__":
    main()
