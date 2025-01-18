from ConnectAPI import *

# This AzureOpenAIController function is use to Validate the payload data["prompt"] is not empty and string format.
def AzureOpenAIController(Question):
    try:
        if Question != "":
            return openai(Question)
        else:
            return {
                "message":"Invaild data !",
                "status":400
            }
    except Exception as e:
        return {
                "Error":str(e),
                "statusCode":500
            }
        
# This googleSerpController function is use to Validate the payload data["prompt"] is not empty and string format.
def googleSerpController(Question):
    try:
        if Question != "":
            return get_google_serp_results(Question)
        else:
            return {
                "message":"Invaild data !",
                "status":400
            }
    except Exception as e:
        return {
                "Error":str(e),
                "statusCode":500
            }
