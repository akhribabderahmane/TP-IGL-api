import requests

BASE_URL = 'http://localhost:8000/api/patients'

def test_list_patients():
    # Get all patients
    print("\nFetching all patients...")
    response = requests.get(f'{BASE_URL}/')
    print(f"Status: {response.status_code}")
    
    if response.status_code == 200:
        patients = response.json()
        print(f"\nTotal patients found: {len(patients)}")
        
        # Display each patient's information in a formatted way
        for patient in patients:
            print("\n" + "="*50)
            print(f"Patient ID: {patient['id']}")
            print(f"Name: {patient['user']['nom']} {patient['user']['prenom']}")
            print(f"NSS: {patient['nss']}")
            print(f"Birth Date: {patient['date_naissance']}")
            print(f"Address: {patient['addresse']}")
            print(f"Insurance: {patient['mutuelle']}")
            print(f"Contact Person: {patient['personne_contact']}")
            print(f"Doctor ID: {patient['medcin_traitant']}")
            print("DPI Info:")
            print(f"  - Created: {patient['dpi']['created_at']}")
            if patient['dpi']['antecedants']:
                print(f"  - Medical History: {patient['dpi']['antecedants']}")
            if patient['dpi']['bilan_biologique']:
                print(f"  - Biological Assessment: {patient['dpi']['bilan_biologique']}")
    else:
        print(f"Error: {response.json()}")

if __name__ == "__main__":
    test_list_patients()