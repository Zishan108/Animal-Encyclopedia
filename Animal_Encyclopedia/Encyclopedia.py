import requests

animal_name = input("Enter the name of animal whose information you want to gather : ")

response = requests.get(f"https://api.api-ninjas.com/v1/animals?name={animal_name}",
                        headers={"X-Api-Key": "r5G9K9MJb5jC+gWV3awFMA==1MOqUWqBRN99b8DQ"})

if response.status_code == requests.codes.ok:
    print(response.text)


else :
    print("Error!!")
