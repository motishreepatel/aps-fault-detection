import pymongo
#we have installed pandas in requirements.txt. Now we will import it here
import pandas as pd
import json

#This file is to dump csv data into mongodb
# Provide the mongodb localhost url to connect python to mongodb.
client = pymongo.MongoClient("mongodb://localhost:27017/neurolabDB")

DATA_FILE_PATH = "/config/workspace/aps_failure_training_set1.csv"
# We right click and copy path of aps csv file and stored it in this variable
# since we have to dump data into mongodb we should know a database name and a collection name
DATABASE_NAME = "aps"
COLLECTION_NAME = "sensor"

#to read csv file we need pandas library and that pandas library is not yet installed. So we have to install that. 
# so we can install that and mention in requirements.txt file
if __name__ == "__main__" :
    df = pd.read_csv(DATA_FILE_PATH)
    print(f"rows and columns:{df.shape}")
    #now we have to insert this dataframe into mongodb. for that we have to convert this dataframe to json format.
    df.reset_index(drop=True, inplace = True)

    json_record = list(json.loads(df.T.to_json()).values())
    # we will keep all the values in a list so that one record will be in one row
    #also this is one line code to convert any dataframe to json format
    print(json_record[0]) # to see whether data is properly converted or not
    # now we have to insert this data to mongodb
    client[DATABASE_NAME][COLLECTION_NAME].insert_many(json_record)
    # now we got the data in mongodb where class is the target column. values are positive and negative. if 
    # positive menas failure is because air pressure system, negative means failure is not because air pressure system.

    #Now our data is in database in form of mongodb so from here actual data science project or work starts.

    #Let's configure github repository with this project so that whatever code we write here, it be updated in 
    # github and can be accessed anywhere and in any system
    # we have created a github repository with name aps-fault-detection. Every github repository has a unique url. Also 
    # we can see the branch is main. In VSCode if check in bottom left corner, we can see here also branch is main.
    # by checking git remote -v we can see that some other git repository is already connected to this origin  https://github.com/iNeuron-Pvt-Ltd/neurolab-mongodb-python 
    # but it's possible to remove existing repo and connect to a new github repo
    # here we can see the existing repo is stored in a variable name origin. So if we delete the variable origin, we can delete the existing repo
    # so to remove this, the git code will be 'git remote remove origin' - remote because this git repo is not in our local system,
    # and somewhere in server. and origin is the variable name. To check if it is deleted or not we will check 'git remote -v'
    # again and see if any git repo is there. Now we can see there is no remote repo. To see all the commits and all
    # messages we will type 'git log'
    # now we will create a new variable to submit this code to a new github repo. Usually variable name taken is 'origin'.
    # for this we will go to main.py and create this new variable in terminal

# so when more than one person are working in the same project, it will show who has done what commit and at what time.
# git push origin main -f -> here -f because we are pushing it forcefully

