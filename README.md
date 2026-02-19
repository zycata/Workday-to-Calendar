# UBC Workday Excel to Calendar (.ics) converter
Let's be real guys, UBC workday kinda sucks and they don't have any options to directly expert to google calendar.  
So I decided to create one myself (mainly to teach myself apis n stuff) 



### How it works:
- Frontend written in react JSX (overengineered I'm aware)
- Sends a POST request to the backend with a flask api
- backend server receives the file and converts it into a .ics with some processing (logic will be explained soon)
- returns the .ics file to the browser (or an error) 
- Will most likely be hosted on google cloud or vercel with a docker image

### How to run Frontend in development
```bash
cd frontend
npm install 

npm run dev

```

### Backend setup in development
```bash
# assuming in project root
pip install backend/requirements.txt 
# if your on linux 
pip install gunicorn
# you may substitute 4 for n amount of processes
gunicorn -w 4 -b "0.0.0.0:5100" backend.api:app

# if you're own windows
python -m backend.api
```

Alternatively, you may also run `./wsl_env.sh` on linux to do a semi-automated install (follow instructions)

### Docker
You can use docker to build a docker image and run it through a docker container (recommended)

```bash
docker build -t workday-app .
docker run -p 5100:5100 workday-app
```