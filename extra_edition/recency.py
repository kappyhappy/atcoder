import datetime

def recency(date_str):
    today = datetime.date.today()
    target_date = datetime.datetime.strptime(date_str, "%Y%m%d").date()
    diff_date = (today - target_date).days
    return str(diff_date)

def pick_userid_date(user_data_dict):
    recency_val = recency(user_data_dict["date"])
    id_date_dict = {
        "user_id": user_data_dict["user_id"],
        "recency": recency_val,
    }
    return id_date_dict
    
def main():
    recency_list = []
    user_data_1 = {"user_id": "user_id_1", "date": "20181001", "amount": "100"}
    user_data_2 = {"user_id": "user_id_2", "date": "20181101", "amount": "10"}
    user_data_3 = {"user_id": "user_id_3", "date": "20180901", "amount": "500"}
    user_data_4 = {"user_id": "user_id_4", "date": "20180301", "amount": "50"}
    user_data_5 = {"user_id": "user_id_5", "date": "20180601", "amount": "30"}

    user_data_list = [
        user_data_1,
        user_data_2,
        user_data_3,
        user_data_4,
        user_data_5
    ]

    for each_item in user_data_list:
        recency_list.append(pick_userid_date(each_item))

    print(recency_list)
    recency_list.sort(key=lambda x: x["recency"])

    print("sorted by recency ascending")
    print(recency_list)

    recency_list.sort(key=lambda x: x["recency"], reverse=True)
    print("sorted by recency descending")
    print(recency_list)

if __name__ == "__main__":
    main()



