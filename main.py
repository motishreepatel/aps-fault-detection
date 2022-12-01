import pymongo

# Provide the mongodb localhost url to connect python to mongodb.
client = pymongo.MongoClient("mongodb://localhost:27017/neurolabDB")

# Database Name
dataBase = client["neurolabDB"]

# Collection  Name
collection = dataBase['Products']

# Sample data
d = {'companyName': 'iNeuron',
     'product': 'Affordable AI',
     'courseOffered': 'Machine Learning with Deployment'}

# Insert above records in the collection
rec = collection.insert_one(d)

# Lets Verify all the record at once present in the record with all the fields
all_record = collection.find()

# Printing all records present in the collection
for idx, record in enumerate(all_record):
     print(f"{idx}: {record}")

#we are creating a new variable for new github repo as 'origin'. we can use any name for variable. now we can see some mis-
#match in here and in github repo. here by doing git log we can see 3 commits, but in github repo there is one commit and
#in both places ids are different. so if we try to update this content to the github repo, it will create problem for us.
#now lets try to push this content to github using git code 'git push origin main'(git push variable name branch name)
# after doing git push, now we are getting some error. for that we have to pull all the files that this git repo already has,
#check with my own code if its working or not and then push with all files together again.
# after doing 'git pull origin main' we r now getting fatal error. This error because ids of all commits are not matching.
# now we can either delete the commits in my code or can delete the commit in git repo. since the commits in our code are
#not created by us, and is not much use to us. so better to delete these commits.
# code 'ls -a' is to check if there is any hidden files. cd .git/ means we are going inside .git file. then ls means what
# is there inside .git file. so we can see there are logs inside. ls means list. so when we check ls, it gives us list of
# files or folders in that directory
# git official document with all codes - https://git-scm.com/docs/git-reset
# if we will use redirect the other commits to a single commit is called soft reset. if we delete other commits and put 
# them in a single commit is called hard reset. So lets do soft reset. git add . means we have added all files to staging area

