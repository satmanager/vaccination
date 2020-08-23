# vaccination
Basic API REST Example


#Installation on GCP
Be sure to enable deployment manager API

Execute this commands in google cloud shell to deploy:

git clone https://github.com/satmanager/vaccination
gcloud deployment-manager deployments create dep1 --config vaccination/vm_startup_script/python/vm.yaml

Please wait some minutes until you can reach the service in a browser pointing to your VM external ip address