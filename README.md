# mood-effect-movie



## Projects
This is a movie recommendation system based on TMDB API, built with Flask framework. Users can get similar movie recommendations by entering a movie title or mood keywords.

## Tech Stack
- Backend Framework: Flask
- API: TMDB API
- Frontend: HTML/CSS

## Installation Steps
1. Clone repository
```bash
git clone <repository_url>
cd movie
```
2. Install dependencies
```bash
pip install -r requirements.txt
```
3. Get TMDB API Key
   - Visit [TMDB website](https://www.themoviedb.org/) to register an account
   - Get API key in account settings
4. Set environment variable
```bash
export TMDB_API_KEY=your_api_key
```
5. Run application
```bash
python app.py
```

## Usage
1. Visit `http://localhost:5000`
2. Enter a movie title or mood keywords (e.g. "happy", "sad")
3. Click "Get Recommendations" button
4. View the list of recommended similar movies

## License
MIT License
