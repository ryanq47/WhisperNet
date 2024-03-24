Rough working docs

## ListenerHTTP Plugin


Endpoints:
     - listener_http_get_endpoint
        - 


     - listener_http_post_endpoint
        - the inital checkin endpoint. New clients check in here, and they will get sent back data + a new url 

Funcs:
    client_checkin_validation:
        Does some validation to see if a client already exists.
            - calls main node to see if in DB
                - if not: 
                    create instance in DB
                    Create class instance, add to dict

                - if is:
                    Lookup class instance, pop next command, send it in response. 



## New server setup

1 "master/main" server, holds the DB (and a few other items). Nodes/other servers are the same, but use diff plugins & query the master server for data. Listeners & other plugins (except auth + user, and simplec2, these are per instance) can be run on any server, as they will use API calls to get the data they need, instead of accessing it directly. 

All servers/nodes have the same bones, ex utils will exist on everything. They differ in what plugins they have. Diff plugins have diff depenencies/submodules, which are included in the plugin folders. 



## HTTPJsonRequest

Generates requests to be sent to beacons. ONE class instance per request. 

Usage:

```

# Import/Init class:

myrequest = HTTPJsonRequestBuilder()


## Set items

myrequest.callback.server = 192.168.0.50
ex... expand

#get json to be sent:

myrequest_json = myrequest.generate_json(id=request_id)

## congrats, your json is now generated. 

```