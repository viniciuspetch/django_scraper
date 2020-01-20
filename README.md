# News Hub
News Hub with scraper. Webpage/front-end, server/back-end, and web scraping script. Implemented in Django. Uses SQLite 3 as database. For now, the web scraping is manual, and works only on Tecmundo.

---

### Before anything:
Install all the dependecies, saved in the `requirements.txt` file

### How to use the website/server
Run `python manage.py runserver`. The website will then online at `localhost:8000`.

### How to use the scraper
Run `python manage.py capturar_noticias`. The script will then update the database with the new articles from www.tecmundo.com.br. 

---

### Project organization
Everything was made following the Django organization style.
- `scraper` folder holds the app responsible for the web scraping and the website
- The scraping script will be in `scraper/management/commands`
- The view and model will be in `scraper`
- The Django Template will be in `scraper/template/scraper`
- The static files used by the webpage will be in `scraper/static/scraper`

### The web scraper and database
The web scraper will get and store at the SQLite database the ID (extracted from the URL), URL, title, source (in this case, 'Tecmundo'), and the article itself.

The dependencies of the web scraper are `requests` (to make HTTP requests) and `BeautifulSoup4` (to parse the collected HTML).

### The website
The page will the built using Django Template and the list of articles from the database. The implemented JS will be responsible for filtering the articles based on the search bar (and clear search button), and for changing the `open/close` icon in each article title.

The dependencies of the website are `Bootstrap.css`, `Bootstrap.js`, `Jquery.js` and `Popper.js` (all via CDN). The necessary files from the project itself are `index.css`, `index.js`, `chevron-down.svg` and `chevron-right.svg`, all in the `static` folder
