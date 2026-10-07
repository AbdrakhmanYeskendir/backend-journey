Request is when the client asks for something from the site.
    Request contains:
        Method: GET, POST, PUT, PATCH, DELETE
        URL: what are we addressing, for example /posts/1
        Headers: official information which goes with the request and response(in what format you are accepting the answer, who are you and so on). They are built like pairs "key: value"
        Body: data you are sending(only in POST, PUT, PATCH)
Response is when the site answers the request sending them some data.
    Response contains:
        Status code: number that tells how did it go
        Headers: official info from server
        Body: data itself, usually in JSON
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
    403 - server knows who you are, but you are not allowed
    404 - Not Found
    500 - Internal Server Error
Rule:
    2xx - success
    4xx - mistake from the client side
    5xx - mistake from the server side
Headers:
    Content-Type: format of the body: application/json for JSON
    Accept: in which format a client wants to get a response
    Authorization: who are you: token or password
    User-Agent: who is making a request: browser, curl, requests
    * Content-Type describes what is in the body of this message, while Accept asks server in what format to return a response
