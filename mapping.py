from doc_pat_info_reader import get_hosp_data
doctors, patients= get_hosp_data()


mappingss=[]

for patient in patients:
    issue=patient['issue']
    
    total_doctors= len(doctors)
    
    for i in range(total_doctors):
        if doctors[i]['speciality']==issue and patient['time_required'] <= doctors[i]['availability']:
            mappingss.append((doctors[i]['d_name'],patient['p_name']))
            doctors[i]['availability']-=patient['time_required']
            
print(mappingss)
print()
print(doctors)
        
        
# for doctor in doctors:
#         if doctor['speciality']==issue and patient['time_required'] <= doctor['availability']:
#             mappingss.append((doctor['d_name'],patient['p_name']))
#             doctor['availability']-=patient['time_required']