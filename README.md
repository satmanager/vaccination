# vaccination
Basic API REST Example


#Installation on GCP
Be sure to enable deployment manager API

Execute this commands in google cloud shell to deploy:

git clone https://github.com/satmanager/vaccination
gcloud deployment-manager deployments create dep1 --config vaccination/vm_startup_script/python/vm.yaml

Please wait some minutes until you can reach the service in a browser pointing to your VM external ip address

#Active endpoints

POST /token            Obtain a jwt token to can authenticate to the other endpoints (body of the request must be json in the following way:
                       {"username": "superuser", "password": "superuser"}
                       )

GET /drugs             Obtain a list of drugs
GET /drugs/{id}        Obtain detail of one drug
POST /drugs            Create a drug. JSON Body (
                        {
                        "name": "Drug Three",
                        "code": "DG003",
                        "description": "Drug number three"
                        }
                        )
PUT /drugs/{id}        Edit drug detail. JSON Body (
                        {
                        "name": "Drug Three",
                        "code": "DG003",
                        "description": "Drug number three"
                        }                        
                       )     

GET /vaccination       Obtain a list of vaccinations
GET /vaccination/{id}  Obtain detail of one vaccination