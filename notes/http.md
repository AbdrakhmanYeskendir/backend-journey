Request is when the client asks for something from the site.
    Request contains:
        Method: GET, POST, PUT, PATCH, DELETE
        URL: what are we addressing, for example /posts/1
        Headers: official infromaation(in what fromat you are accepting the answer, who are you and so on)
        Body: data you are sending(only in POST, PUT, PATCH)
Response is when the site answer the request sending them some data.
    Response contains:
        Status code: number that tells how did it go
        Headers: official infro from server
        Body: data itslef, usually in JSON
HTTP Methods:
    GET - to get some data
    POST - to create some data
    PUT - to change everything
    PATCH - to change a part
    DELETE - to remove the data
Meaning of the codes:
    200 - OK, success
    201 - Created
    400 - Bad Request, client sent wrong data
    401 - Unauthorized, server does not know who are you
    404 - Not Found
    500 - Internal Server Error
Rule:
    2xx - success
    4xx - mistake form the client side
    5xx - mistake from the server side
