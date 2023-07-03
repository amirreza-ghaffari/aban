
Welcome 

To run the Project Using Docker run bellow commands:

    sudo docker compose up

  Open another terminal and run(aban-web-1 name may differ in another machine):
  
    sudo docker exec -it aban-web-1 -sh
  Then run bellow command to createsuperuser:

    python manage.py createsuperuser

    
then go to admin panel (CryptoCurrency model, '/admin/crypto/cryptocurrency/') and create Coins like 'bitcoin' and 'tether' with their price
note = 'the coins prices are saved in sql database for simplicity which is not recommended :)'

 --------------------------------------------------------------------
<h1>The Transaction API is written both Class Based and Functional:</h1>


Also There is a swagger document in '/swagger/'


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


  
