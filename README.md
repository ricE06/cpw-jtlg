# cpw-jtlg
A website to host the 2025 CPW Jet Lag The Game event.

## Installation

First, clone this repository locally. This app requires Flask and python-dotenv,
both of which can be pip-installed:

```
pip install flask python-dotenv
```

Also, run 

```
cd frontend
npm install
```

to install all node dependencies.

## Running the server

In the `backend` directory, run

```
flask run --debug
```

to start the flask app with debug on. This server will be listening at `localhost:5000`.
To hook up the frontend, navigate to `frontend` and run

```
npm run start
```

Now, navigate to `localhost:3000` and the app should be working!
