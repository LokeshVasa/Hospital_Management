from doc_pat_info_reader import get_hosp_data


doctors, patients= get_hosp_data()

# speciality=input("ask:")

# speciality_availibity=0

# for doctor in doctors:
#     if doctor['speciality'] == speciality:
#         speciality_availibity+=doctor['availability']
# print(speciality_availibity)         

# doctors_speciality_count={}

# for doctor in doctors:
#     speciality=doctor['speciality']
#     if speciality not in doctors_speciality_count.keys():
#         doctors_speciality_count[speciality]=doctor['availability']        
    
#     elif speciality in doctors_speciality_count.keys():
#         doctors_speciality_count[speciality]+=doctor['availability']    
    
# print(doctors_speciality_count)        






patients_count={}

for patient in patients:
    issue=patient['issue']
    if issue not in patients_count.keys():
        patients_count[issue]=patient['time_required']
    elif issue in patients_count.keys():
        patients_count[issue]+=patient['time_required']

print(patients_count)            