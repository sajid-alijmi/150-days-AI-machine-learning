import json

data = load_data("store_data.json")
print(data, type(data)) 

# clean & structure the data
def clean_data(data):
    text_to_num = {"one": 1, "two": 2, "three": 3, "four": 4, "five": 5}
    cleaned_data = []
    unique_users = set()

    for user in data:
        #Clean ratings - data consistency
        raw_rating = str(user["rating"]).strip().lower()
        if(raw_rating in text_to_num):
            raw_rating = text_to_num[raw_rating]
        user["rating"] = raw_rating

        #Handle missing vals
        raw_age = user.get("age")
        if(raw_age == None):
            user["age"] = None

        #duplication data
        if(user["name"].strip() in unique_user):
            continue

        cleaned_data.append(user)

    return cleaned_data

clean_data(data)

data = clean_data(data)

#Get meaningful insight from 
def get_insights(data):

    #avg rating
    tot_rating = 0
    for user in data:
        tot_rating += float(user["rating"])

    print(f"avg rating = {tot_rating/len(data)}")

    #percentage of users with poor rating
    poor_ratings = 0
    for user in data:
        if(float(user["rating"]) < 4):
            poor_ratings += 1

    print(f"of user with poor rating = {poor_ratings/len(data) * 100}%")

get_insights(data)

def get_recommendations(data):
    recommendation =[]

    for user in data:
        curr_recomm = {}
        curr_recomm["name"] = user["name"]

        if(float(user["rating"]) >= 4):
            curr_recomm["brand"] = "Apple"
        else:
            curr_recomm["brand"] = "Samsung"
        recommendation.append(curr_recomm)
    return recommendation
get_recommendations(data)
