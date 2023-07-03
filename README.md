
<h2>Welcome</h2> 

To run the Project Using Docker run bellow commands:

    sudo docker compose up

  Open another terminal and run:
  
    sudo docker exec -it aban-web-1 -sh
'aban-web-1' name may differ in another machine
Then run bellow command to createsuperuser:

    python manage.py createsuperuser

    
then go to admin panel (CryptoCurrency model, '/admin/crypto/cryptocurrency/') and create Coins like 'bitcoin' and 'tether' with their prices
note = 'the coins prices are saved in sql database for simplicity which is not recommended :)'

 --------------------------------------------------------------------
<h1>The Transaction API is written both Class Based and Functional:</h1>
The PostMan Document file is available in: 
<h3>'aban_tether.postman_collection.json'</h3>


Also There is a swagger document in :
```
http://127.0.0.1:8000/swagger/
```

-------- Functional -------

```
url = '/crypto/api/v1/do_transaction/'
data = {
  "coin_name": "bitcoin",
  "amount": 1.2
  }
```
-------- Class based -------
```

url = '/crypto/api/v1/transactions/'
data = {
  "coin_name": "bitcoin",
  "amount": 1.2
  }
```


  
