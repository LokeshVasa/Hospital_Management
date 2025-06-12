def get_hosp_data():
    import json
    
    with open("doctors.json",'r') as file:
        doctors=json.load(file)
        
    with open("patients.json",'r') as file:
        patients=json.load(file)
        
    return doctors, patients