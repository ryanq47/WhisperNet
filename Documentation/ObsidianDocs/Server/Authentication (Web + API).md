
Authentication exists in 2 forms:
- Plugin/API Authentication
- Webserver/User authentication


here's a high level overview of how it works.

[ Old ]
Each plugin *should* have its own table in the users.db table. During authentication, only that table is checked for user/pass. This way, if an external plugin gets pwned, only that plugin has been breached, and the attacker cannot use said credentials to access other API endpoints, or the webserver itself.

[ New ]
All the API users are stored in one table. Access is now controlled through roles, which is an additional field in the DB. Users & api_users are still separated. This is an intentional design choice, these 2 should never mix - i.e. A user should not be able to access the API, and an api_user should not be able to access the web endpoints

![[Pasted image 20231007142634.png]]


Additional Considerations (aka cover my ass):

*If an attacker can SQL inject, they could grab hashed passwords of the other API & user accounts, however I aim to not have any injectable fields. Still, even if they can inject, they'll have to crack the bcrypt hashes. *
## Roles:

Right now these are API only.

- "filehost_admin": Admin for filehost plugin
- "filehost_user": User for filehost plugin

or more general, 
- "NAME_admin"
- "NAME_user" 