from flask import Flask, render_template, request
import requests

app = Flask(__name__)

# TMDB API配置
TMDB_API_KEY = "1c2dd94e0687f2265f362d6249ee446d"  # 使用用户提供的API密钥
BASE_URL = "https://api.themoviedb.org/3"

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/recommend', methods=['POST'])
def recommend():
    movie_title = request.form.get('movie_title')
    
    # 获取相似电影
    similar_movies = get_similar_movies(movie_title)
    
    return render_template('recommendations.html', 
                          movies=similar_movies,
                          query=movie_title)

# 心情关键词到电影名称的映射
MOOD_MOVIE_MAPPING = {
    "Sad": "Manchester by the Sea",
    '开心': 'The Intouchables',
    '难过': 'The Pursuit of Happyness',
    '兴奋': 'Inception',
    '平静': 'Before Sunrise',
    '愤怒': 'Fight Club'
}

def get_similar_movies(title):
    # 检查是否是预设心情关键词
    if title in MOOD_MOVIE_MAPPING:
        title = MOOD_MOVIE_MAPPING[title]
    
    try:
        # 1. 先搜索电影ID
        search_url = f"{BASE_URL}/search/movie?api_key={TMDB_API_KEY}&query={title}"
        response = requests.get(search_url, timeout=10)  # 添加10秒超时
        response.raise_for_status()  # 检查HTTP错误
        data = response.json()
        
        if not data.get('results'):
            return []
        
        movie_id = data['results'][0]['id']
        
        # 2. 获取相似电影
        similar_url = f"{BASE_URL}/movie/{movie_id}/similar?api_key={TMDB_API_KEY}"
        response = requests.get(similar_url, timeout=10)
        response.raise_for_status()
        data = response.json()
        
        return data.get('results', [])[:5]  # 返回前5个相似电影
    except requests.exceptions.RequestException as e:
        print(f"Error fetching movie data: {e}")
        return []

if __name__ == '__main__':
    app.run(debug=True)