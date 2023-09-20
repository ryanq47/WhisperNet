

| Cookie | Value | Desc | 
|----------|----------|----------| 
| err | error message | Used to return error messages to the requester | 
| Row 2, Col 1 | Row 2, Col 2 | Row 2, Col 3 |



## Cookie breakdowns

#### err cookie:
This cookie is used to return error messages to the requester. Because all pages return a '200', this is used as a workaround to get error messages across when needed. It's not the most secure, as it can reveal python & flask error messages, but its handy for development