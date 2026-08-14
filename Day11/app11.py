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