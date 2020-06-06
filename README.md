# my-auto-flask-service
a simple flask based service

This project is a skelaton for bootstraping a simple flask server application.

## server
The main interface into the server is using http requests.
The interface is declared in the openAPI schema.
More on openAPI spec ***here***

According to the openAPI spec, a flask server will be initiated, and is configured with all the routes that was specified in the spec.

The flask app is injected with a controler module (http adapter) that will handle the http requests.
The operationID field is the interface between the openAPI spec and the application controller.
More on operationID ***here***


# SDK
## Why we need SDK?
Potentialy, many application and servicesb (consumers) would like to use the server API in order to configure it, add/edit/delete/get data. 
Examples for theses consumers:
1) Frontend GUI application.
2) Costumers scripts.
3) API gateway.
4) Other backend microservice.

We would like to give our consumers an easy-to-use tool, for communicating with our server.
Easy means that the consumers need to handle only the relevant data, (i.e - the data sent and received to/from the server, auth credentials), and do not need to handle the way to send it (u.e data in body/param, data schema, auth in which format, pathes, http verbs etc etc)

In order to hide the specifics of request toward our server, we will supply a SDK package, that will expose a simple interface toward our server.



## SDK generation


The SDK is generated in 2 steps:
1. (Auto Generation) HTTP client, that is generated according to the openAPI spec.
    We are using the official openAPI generator project for this action.
    More on openAPI code generator. 

2. (Currently - manual generation) Service SDK. Wrap the HTTP methods in buissnes logic methods.
    The HTTP client will be injected into the SDK class, which will expose the HTTP client methods in a buisness logical way.
    * SDK  of service will usually contain a syncronious request/response (HTTP) methods, and asyncronious event subscription (verios protocols). This project concentrate on the syncronious part.  

3. (Currently - manual generation) Test integration between the server and the SDK


### Steps

1. produce a python HTTP client code:
```
./generate_sdk.sh
```

2. Create SDK class in /sdk/sdk.py, wrap and expose the generated HTTP client code

3. create integration test in the tests/api-tests directory.

run docker compose that will initiate the server, and run the tests.
```
./run-tests-docker.sh
```


## TODO
* openAPI viewer
* examples (should be simmilar to integration tests)
* documentation
* SDK class
* auto-generate SDK wrapper
* auto generate SDK basic tests




