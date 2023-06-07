import uvicorn
from fastapi import FastAPI
from scrapper import Scraper

app = FastAPI()
quotes = Scraper()

@app.get("/qoutes/{tag}", tags=["quotes"])
async def get_quotes(tag: str):
    return quotes.scrape_data(tag)

if __name__ == "__main__":
    uvicorn.run(app, host="0.0.0.0", port=8000)