# UBC Workday Excel to Calendar (.ics) converter
Let's be real guys, UBC workday kinda sucks and they don't have any options to directly expert to google calendar.  
So I decided to create one myself. I'm aware that there are extensions and another site already that do this, but I'm mainly creating this to learn and create a somewhat "practical" applicaton.

### How it works:
- Frontend written in react JSX (overengineered I'm aware)
- Sends a POST request to the backend with a flask api
- backend server receives the file and converts it into a .ics with some processing
- returns the .ics file to the browser (or an error) 
- Hosted through google cloud run, with 0 cpus on idle (it's cheaper for me that way...)

### Requirements:
- Python version that supports all the libraries in [requirements.txt](backend/requirements.txt) 
- If you're on linux a python version that supports the previous entry and gunicorn
- Nodejs 20 or higher with an npm version that supports "lockfileVersion" 3

### Frontend setup
```bash
cd frontend
npm install 
npm run build 
# if no errors occur, you are good to go!
```

### Backend setup in development
```bash
# assuming in project root
pip install backend/requirements.txt 
# run the entire application
python -m backend.api
# will run on http://127.0.0.1:5100

# if your on linux, you can run using gunicorn instead
pip install gunicorn
# you may substitute 1 for n amount of processes
gunicorn -w 1 -b "0.0.0.0:5100" backend.api:app

```

Alternatively, you may also run `./L_env.sh` on linux to do a semi-automated install of the python resource (read the file for trouble shooting)

### Docker
You can use docker to build a docker image and run it through a docker container (recommended)

```bash
docker build -t workday-app .
docker run -p 5100:5100 workday-app
```


### Command line interface

Alternatively, you can also use the [converter.py](backend/converter.py) to use as a command line tool to converter a workday excel to a .ics file. Remember your relative folder is the folder you're running python in and not the directory the file is in. 
```bash
# Usage
python -m backend.converter [input_file] [output_file]
# Example
python -m backend.converter Schedule.xlsx  backend/why_here.ics
```
