from fastapi import FastAPI
from fastapi.responses import HTMLResponse
from fastapi.staticfiles import StaticFiles

app = FastAPI()

@app.get("/", response_class=HTMLResponse)
async def read_root():
    return """
    <!DOCTYPE html>

    </head>
    <body>
        <h1>About Me</h1>
        <p>
            Hello! I am Peter Liu. I am passionate about coding.
            Here is a brief overview of my background, goals, and experiences.
        </p>

        <h2>Experiences/Projects</h2>

        <h3>Project 1</h3>
        <p>
            <strong>Title:</strong> ELP at Revelle <br>
            <strong>Time Period:</strong>  2022 - 9  to 2023 - 6 <br>
            <strong>Description:</strong> Set up the earth day event at revelle plaza

        <h3>Project 2</h3>
        <p>
            <strong>Title:</strong> Coding<br>
            <strong>Time Period:</strong> 2022 - 9 <br>
            <strong>Duties/Description:</strong> built a lot of things
        </p>

        <h3>Project 3</h3>
        <p>
            <strong>Title:</strong> Playing chess<br>
            <strong>Time Period:</strong> 2023-9 <br>
            <strong>Duties/Description:</strong> Avid chess player
        </p>
    </body>
    </html>
    """

if __name__ == "__main__":
    import uvicorn

    uvicorn.run(app, host="localhost", port=6543)
