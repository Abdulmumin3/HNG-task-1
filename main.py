from fastapi import FastAPI, Query
from datetime import datetime
import pytz

app = FastAPI()

@app.get('/api/')
async def personal_info(slack_name: str=Query(..., description = "Enter your slack name"), track: str=Query(..., description = "Enter your track")):
    utc_time = datetime.now(pytz.utc)
    response = {"slack name": slack_name, "current_day": utc_time.strftime("%A"), "utc_time": utc_time.strftime("%Y-%m-%dT%H:%M:%SZ"), "github_file_url": "https://github.com/username/repo/blob/main/file_name.ext", "github_repo_url": "https://github.com/username/repo", "track": track, "status_code": 200}
    return response