import contextvars

class LoggerContext():
    
    def __init__(self):
        self._request_id = contextvars.Context("request_id", default=None)
        self._user_id = contextvars.Context("user_id", default=None)
        self._project_id = contextvars.Context("project_id", default=None)
        self._org_id = contextvars.Context("org_id", default=None)

        @property
        def request_id(self):
            # return self._request_id  - would this work?
            return self._request_id.get()
        
        @request_id.setter
        def request_id(self, value):
            # self._request_id = value
            # return self._request_id
            # are the get() and set() methods not the getter and setter for a class?
            self._request_id.set(value)
        
        @property
        def org_id(self):
            return self._org_id.get()
        
        @org_id.setter
        def org_id(self, value):
            self._org_id.set(value)

        @property
        def project_id(self):
            return self._project_id.get()
        
        @project_id.setter
        def project_id(self, value):
            self._project_id.set(value)

        @property
        def user_id(self):
            return self._user_id.get()
        
        @user_id.setter
        def user_id(self, value):
            self._user_id.set(value)
        

       
ctx = LoggerContext()