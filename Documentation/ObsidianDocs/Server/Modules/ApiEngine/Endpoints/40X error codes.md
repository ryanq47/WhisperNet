
#### 404 Errors
JWT Req: N/A
Method: Any

All 404 errors are returned as a 200. This is to prevent (or slow) URL discovery by a potential adversary. 
See Security Testing > Url Fuzzing & discovery for more details.

There are 2 404 pages currently:
- 404-default.html - The default "oops not found"
- 404-default-alt.html - The default "oops not found", but with some extra useless code to change the page length. 

These are located at `Server\ApiEngine\html\errorcodes`

