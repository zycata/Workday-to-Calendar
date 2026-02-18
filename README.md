# UBC Workday Excel to Calendar (.ics) converter
Let's be real guys, UBC workday kinda sucks and they don't have any options to directly expert to google calendar.  
So I decided to create one myself (mainly to teach myself apis n stuff) 



### How it works:
- Frontend written in react JSX (overengineered I'm aware)
- Sends a POST request to the backend with a flask api
- backend server receives the file and converts it into a .ics with some processing (logic will be explained soon)
- returns the .ics file to the browser (or an error) 
- Will most likely be hosted on google cloud or vercel with a docker image

### How to run 
```bash
cd frontend
npm install 

npm run dev

# backend running will be added later
```