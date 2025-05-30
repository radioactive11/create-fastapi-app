class ContextHijackerMiddleware():
    def __init__(self, app):
        #this app can be the actual FastAPI app or another Middleware
        #this will be called when the FastAPI app is wrapped inside the middleware

        self.app = app 
        
    def __call__(self, scope, receive, send):
        #this function is called by the ASGI app(uvicorn)
        #this function enables the middleware to be the app from ASGI's POV
        #scope: a dictionary with request data
        #receive: a callable to receive client data
        #send: Async callable to send response pieces back to client


        #set required params for the middleware object
        #this middleware can be used for logging purposes
        pass