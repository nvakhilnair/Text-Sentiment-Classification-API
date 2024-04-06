from fastapi import FastAPI, Query
from fastapi.responses import JSONResponse, FileResponse
from process_string import ProcessText
from classification import Classifier

app = FastAPI()
process_obj = ProcessText()
classify_obj = Classifier()

@app.get("/")
async def read_root():
    """
    Return the homepage HTML file.
    """
    return FileResponse(r".\templates\homepage.html")


@app.get("/classify/")
async def process_text(
    input_text: str = Query(title="Input Text", description="Text to process"),
    preprocess: bool = Query(
        False, title="preprocess", description="Enable preprocessing"
    ),
):
    """
    Process and clean uncleaned text data.

    Args:
        input_text (str): The uncleaned text data.
        preprocess (bool): Whether to apply preprocessing to text.

    Returns:
        JSONResponse: Polarity of the input text.
    """
    if preprocess:
        response = await process_obj.clean_text(
            uncleaned_text=input_text
        )
        return JSONResponse(content={"Polarity": await classify_obj.classify(response)}, status_code=200)
    return JSONResponse(content={"Polarity": await classify_obj.classify(input_text)}, status_code=200)
