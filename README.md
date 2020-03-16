## Daupler Developer Code Test | Notes

### Setup
Follow standard procedure for setting up a Django project. Note that,
as allowed, this project uses a SQLite3 database.

Best practice dictates that the Django SECRET_KEY not be stored in
Github. Note that settings.py expects this to be an environment
variable. Feel free to define in settings.py once the code is local,
if desired.

### Design Comments
I wasn't sure what to call the sample app but I didn't want to call it
API--so, I went with water! :)

Similarly with the models, particularly Employee, I was
tempted to create the relationship with Team as a through model with
the assumption that a person could be on more than one team and, in
association with the teams they are on, have a role and on call order
that might be different accordingly.

Also, in the API call to list teams and team members, members are listed
but not as a hyperlinked foreign key relationship that could then be
followed to get the details for the team member.

I debated on how to implement the requirement that on call order can
be changed. You can change it easily by doing a simple put for the
given person. However, if you try to change it to an on call value that
already exists within the team, the API returns an error. I could see
this being changed / improved depending on how the front end is
designed.

For each design decision, I decided to keep it simple--meet your
requirements and not add complexity.

### Calling the API
I used Postman to call the API and ensured BasicAuth was defined for
each call as the API is defined to required authentication. The user
added when running .manage.py createsuperuser suits that purpose
perfectly (though a superuser permission level is not required).

#### Teams
/teams/ - get (lists teams, and members), post

/team/1/ - put, delete

Data required for team:

{'name': 'awesome response team'}

#### Roles
/roles - get, post

/role/1/ - put, delete

Data required for role:

{'name': 'First Responder'}

#### Employee
/employees/ - get, post

/employee/1/ - put, delete

Data required for employee:

{'first_name': 'Barney', 'last_name': 'Diehl', 'team': 1, 'role': 1, 'on_call_order': 3}

