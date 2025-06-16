import json
import os


def add_new_patient(new_patient_info:dict, file_path= r"D:\python-practice\doctor_appointment\patients.json"):
    """
    Updates a JSON file with a new dictionary.

    :param new_data: Dictionary with new data to update
    :param file_path: Path to the JSON file
    """
    # If the file exists, load the existing data
    if os.path.exists(file_path):
        print("File exists")
        with open(file_path, 'r') as file:
            try:
                data = json.load(file)
                print("Date read")
            except json.JSONDecodeError:
                data = []
                print("Data read failed")
    else:
        data = []

    # Update the data with the new dictionary
    data.append(new_patient_info)
    print("Data Added Successfully")

    # Write the updated data back to the file
    try:
        with open(file_path, 'w') as file:
            json.dump(data, file, indent=4)
        print("Success")
    except Exception as e:
        print(e)
        
    if os.path.exists(file_path):
        print("File exists")
        with open(file_path, 'r') as file:
            try:
                data = json.load(file)
                print("Date read")
            except json.JSONDecodeError:
                data = []
                print("Data read failed")
    else:
        data = []
        
    last_patient= data[-1]['p_name']
        
        
    return f"Succesfully Added {last_patient}"


# if __name__=="__main__":
#     new_dict =  {
#         "p_name": "groot",
#         "issue": "caridology",
#         "time_required": 5
#     }
#     add_new_patient(new_dict)
