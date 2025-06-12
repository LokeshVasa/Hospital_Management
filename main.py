
# reading data fro json files

from doc_pat_info_reader import get_hosp_data


doctors, patients= get_hosp_data()


# for doctor in doctors:
#     print(doctor)

# for patient in patients:
#     print(patient)
# for doctor in doctors:   
#     print(f"{doctor['d_name']} is {doctor['speciality']}")    
    
for i in range(len(doctors)):
     print(f"{doctors[i]['d_name']} is {doctors[i]['speciality']}")

for patient in patients:
    print(f"{patient['p_name']} is suffering with {patient['issue']} ")
    
   

# for i in range(len(patients)):
#     print(f"{patients[i]['p_name']} is suffering with {patients[i]['issue']} ")    
