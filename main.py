from fastapi import FastAPI, HTTPException
from pydantic import BaseModel
import uvicorn
from controller import *
app = FastAPI()


class Item(BaseModel):
    Question: str

# This route is used to connect to the Azure Open AI API  "ChatGPT - 4" and implement the third tier.
@app.post("/openai/")
async def create_item(item: Item):
    try :
        response = AzureOpenAIController(item.Question)
        return response
    except Exception as e:
        return {
            "error": str(e),
            "stratusCode": 500
        }

# This route is used to connect to the Google Search API and implement the third tier.
@app.post("/google/")
async def create_item(item: Item):
    try :
        response = AzureOpenAIController(item.Question)
        return response
    except Exception as e:
        return {
            "error": str(e),
            "stratusCode": 500
        }



if __name__ == "__main__":
    uvicorn.run("main:app", host="0.0.0.0", port=8000)