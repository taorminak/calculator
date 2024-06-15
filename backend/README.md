## Instructions

- Create a virtual environment:
    ```bash
    python -m venv venv
    .\venv\Scripts\activate
    ```

- Install dependencies
    ```bash
    pip install -r requirements.txt
    ```

- Run the backend
    ```bash
    uvicorn main:app --reload
    ```


## Using this repository to bootstrap your work

```bash
git clone https://github.com/Branquo/challenge
cd challenge
rm -rf .git
git init
git add .
git commit -m "init"
```
- create new private repo on Github without initializing README or other files.
```bash
git remote add origin <your-new-repo>
git push -u origin master
```
