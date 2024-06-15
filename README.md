# Challenge

The `Calculator` web service.

- For the backend work on the provided Python FastAPI starter code (Install instructions are in the `backend` folder). Feel free to change the code however you like, or even start from scratch if you prefer to do so. You can also choose a different language if you want to.
- For the frontend use any programming language / library / technology that you are most comfortable with.
- The Bonus features are optional nice-to-haves.

## Description

- Implement a JSON REST interface
- A `User` has the following attributes:
    - `username`
    - `password`
    - `role`: Either `scientist` or `student`.
- A `student`
    - only has access to the `+` and `-` operators.
    - can update their password.
- A `scientist` in addition to what a `student` can do
    - can use `*` and `/`.
    - can add another `scientist` or `student`.
    - can view a history section, where all calculations of **all** users are listed.
- The calculations need to happen in the Backend.
- All endpoints need to be protected by a `JWT` token.
- The only unprotected endpoint is the login, where the token can be obtained. A valid `username` and `password` returns a token. This endpoint is already provided in the starter code. You will need to update the JWT token and endpoints to include roles for role-based access control.
- The entire development process has to be regularly commited to a newly created git repository following **Best Practises**
- For **Best Practises** reference to the Resource section below. This includes practises like:
    - RESTful API design
    - Git
    - Python/Javascript/Typescript Style Guides

## Minimum Viable Product

- The Calculator is implemented as mentioned above.
- There is a `README.md` that documents how to build, run and use the service.

## Bonus features

- The backend service persists the user and history data and is not lost after reboot of the application. The choice of persistence is up to you. It can be anything from a heavy database to a textfile containting all the data.
- The backend service has an [Open API](https://www.openapis.org/) description
- Automated integration tests are implemented.
- CI/CD pipeline for automatically building and testing the backend is implemented.
- The backend can be started using `docker-compose`.

## Resources

Please make sure to follow **Best Practises**. These resources will help you out achieving this. Note, that it is not required to study the resources by heart, they are meant as guidelines to help while coding.
- RESTful API
    - [Microsoft's RESTful web API design](https://learn.microsoft.com/en-us/azure/architecture/best-practices/api-design)
    - [Microsoft Azure REST API Guidelines](https://github.com/microsoft/api-guidelines/blob/vNext/azure/Guidelines.md)
- Git
    - [Git Commit Best Practises](https://gist.github.com/luismts/495d982e8c5b1a0ced4a57cf3d93cf60#file-gitcommitbestpractices-md)
    - [Git Tips](https://gist.github.com/luismts/495d982e8c5b1a0ced4a57cf3d93cf60#file-gittips-md)
- [Google Style Guide](https://google.github.io/styleguide/)