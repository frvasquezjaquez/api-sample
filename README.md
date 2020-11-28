uvicorn main:app --reload


docker build -t grupobabeldemoregistry.azurecr.io/apis/get-transaction:latest .


docker run  --name mycontainer  -p 9020:80 grupobabeldemoregistry.azurecr.io/apis/get-transaction:latest 


kubectl port-forward service/get-transactions 9080:8092