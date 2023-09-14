Flask recommends a WSGI frontend, and at the moment I've chosen 'waitress'. It's a super easy drop in server:
```
    from waitress import serve

    serve(FlaskAPIListener.app, host=ip, port=port)

```

I don't know too much about it yet, but all flask servers will be front ended by this. 

