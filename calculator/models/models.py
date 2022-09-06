from pydantic import BaseModel


class RequestOperation(BaseModel):
    a:int
    b:int
    
class ResponseOperation(BaseModel):
    result:float
