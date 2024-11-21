from fastapi import FastAPI, Form, Request
from fastapi.responses import RedirectResponse, HTMLResponse
from fastapi.templating import Jinja2Templates
from fastapi.staticfiles import StaticFiles
from urllib.parse import urlparse
from functions import urlButton1,urlButton2,fetch_article,fetch_original_article,makePrediction,extract_keywords,urlButton3,search_news_by_keywords,clean_title,refine_keywords # Import the function from your functions.py

class Config:
    TEMPLATES_DIR = "templates"
    STATIC_DIR = "static"

app = FastAPI()
app.mount("/static", StaticFiles(directory="static"), name="static")
templates = Jinja2Templates(directory=Config.TEMPLATES_DIR)

@app.get("/", response_class=HTMLResponse)
async def read_root(request: Request):
    """Render the index page"""
    return templates.TemplateResponse("index.html", {"request": request})

@app.get("/aboutus", response_class=HTMLResponse)
async def about_us(request: Request):
    """Render the About Us page."""
    return templates.TemplateResponse("aboutUs.html", {"request": request})

@app.get("/relatedlinks", response_class=HTMLResponse)
async def read_root(request: Request):
    """Render the Related Links page"""
    return templates.TemplateResponse("relatedLinks.html", {"request": request})


@app.post("/analyze", response_class=HTMLResponse)
async def analyze_and_search(request: Request, url: str = Form(...)):
    """Process URL for bias analysis and fetch related articles."""
    try:
        # Analyze the URL
        print("URL Received:", url)  # Debugging log
        biasValue = urlButton1(url)  # Perform bias analysis
        print("Bias Value:", biasValue)

        # Map prediction to position value for the arrow
        position_map = {
            0: 15,    # Position for left
            1: 45,    # Position for center
            2: 80     # Position for right
        }
        
        prediction = ["Left", "Neutral", "Right"][biasValue]
        arrow_position = position_map.get(biasValue, 10)  # Default to center if unknown

        # Debugging log
        print(f"Prediction: {prediction}, Arrow Position: {arrow_position}")

        # Extract domain name
        parsed_url = urlparse(url)
        domain_name = parsed_url.netloc

        # Use the analyzed URL as a keyword for article search
        ogTitle,ogContent = fetch_article(url)
        print(f"Original Title: {ogTitle}")
        # ogTitle1 = urlButton3(url)
        # print(f"Cleaned Title: {ogTitle1}")  

        ogTitle1 = extract_keywords(ogTitle)  
        print(f"Refined Keywords From Title: {ogTitle1}")  
        articles = urlButton2(ogTitle1)

        # Render the results.html with both prediction and articles
        return templates.TemplateResponse(
            "results.html",
            {
                "request": request,
                "prediction": prediction,
                "arrow_position": arrow_position,
                "url": url,
                "domain_name": domain_name,
                "articles": articles,  # Include related articles
                "title": ogTitle
            }
        )
    except Exception as e:
        # Debugging log
        print(f"Error: {str(e)}")
        return templates.TemplateResponse(
            "index.html",
            {
                "request": request,
                "error": f"Error processing request: {str(e)}"
            }
        )



@app.post("/search_articles", response_class=HTMLResponse)
async def search_articles(request: Request, keywords: str = Form(...)):
    """Fetch articles and render them in relatedLinks.html."""
    try:
        # Use the search function to fetch articles
        articles = urlButton2(keywords)  # Fetches up to 5 articles

        # Render the Related Links page with fetched articles
        return templates.TemplateResponse(
            "relatedLinks.html",
            {
                "request": request,
                "articles": articles,  # Pass articles to the template
                "keywords": keywords  # Optional: Pass keywords for display
            }
        )
    except Exception as e:
        return templates.TemplateResponse(
            "index.html",
            {
                "request": request,
                "error": f"Error searching articles: {str(e)}"
            }
        )

@app.post("/analyzeContent", response_class=HTMLResponse)
async def analyze_content(request: Request, content: str = Form(...), headline: str = Form(...)):
    """Process URL for bias analysis and fetch related articles."""
    try:
        print("Headline Received:", headline)  # Debugging log
        print("Content Received:", content)  # Debugging log
       
        biasValue = makePrediction(content)  # Perform bias analysis
        print("Bias Value:", biasValue)

        # Map prediction to position value for the arrow
        position_map = {
            0: 15,    # Position for left
            1: 45,    # Position for center
            2: 80     # Position for right
        }
        
        prediction = ["Left", "Neutral", "Right"][biasValue]
        arrow_position = position_map.get(biasValue, 45)  # Default to center if unknown


        articles = fetch_original_article(headline)  # Fetch up to 5 related articles

        if(articles == None):
            headline = extract_keywords(headline)
            articles = fetch_original_article(headline)
            ogTitle = articles['title']
            domain_name = articles['domain']
            url = articles['url']
        else:
            ogTitle = articles['title']
            domain_name = articles['domain']
            url = articles['url']
       

        print(url)
        print(ogTitle)
        print(domain_name)

        ogTitle1 = urlButton3(url)
        print(f"Cleaned Title: {ogTitle1}")  

        ogTitle1 = refine_keywords(ogTitle1)
        print(f"Refined Keywords From Title: {ogTitle1}")

        articles = urlButton2(ogTitle1)
        print(articles)

        # Render the results.html with both prediction and articles
        return templates.TemplateResponse(
            "results.html",
            {
                "request": request,
                "prediction": prediction,
                "arrow_position": arrow_position,
                "url": url,
                "domain_name": domain_name,
                "articles": articles,  # Include related articles
                "title": ogTitle
            }
        )
    except Exception as e:
        return templates.TemplateResponse(
            "index.html",
            {
                "request": request,
                "error": f"Error processing request: {str(e)}"
            }
        )