import pandas as pd
from pandas import DataFrame
# 데이터 생성
data = {
    "Title": [
        "Inception", "Interstellar", "The Dark Knight", "Parasite", "Avengers: Endgame",
        "The Matrix", "Gladiator", "Titanic", "Joker", "Mad Max: Fury Road",
        "The Godfather", "Pulp Fiction", "Schindler's List", "The Shawshank Redemption", "Fight Club"
    ],
    "Genre": [
        "Sci-Fi", "Sci-Fi", "Action", "Drama", "Action",
        "Sci-Fi", "Historical", "Romance", "Drama", "Action",
        "Crime", "Crime", "Drama", "Drama", "Drama"
    ],
    "Year": [
        2010, 2014, 2008, 2019, 2019,
        1999, 2000, 1997, 2019, 2015,
        1972, 1994, 1993, 1994, 1999
    ],
    "Director": [
        "Christopher Nolan", "Christopher Nolan", "Christopher Nolan", "Bong Joon-ho", "Anthony Russo",
        "Lana Wachowski", "Ridley Scott", "James Cameron", "Todd Phillips", "George Miller",
        "Francis Ford Coppola", "Quentin Tarantino", "Steven Spielberg", "Frank Darabont", "David Fincher"
    ],
    "Rating": [
        8.8, 8.6, 9.0, 8.6, 8.4,
        8.7, 8.5, 7.8, 8.5, 8.1,
        9.2, 8.9, 8.9, 9.3, 8.8
    ],
    "Audience_Million": [
        100, 120, 150, 80, 200,
        90, 50, 220, 85, 75,
        110, 95, 85, 130, 70
    ],
    "Budget_Million": [
        160, 165, 185, 11, 356,
        63, 103, 200, 55, 150,
        6, 8, 22, 25, 63
    ]
}

df = DataFrame(data)

# 1. 특정 장르("Action")의 영화 목록 출력
action_movies = df[df["Genre"] == "Action"]
print("1. Action 장르의 영화 목록:")
print(action_movies, "\n")

# 2. 특정 연도(2010년) 이후 개봉한 영화 목록 출력 (2010년 포함)
movies_after_2010 = df[df["Year"] >= 2010]
print("2. 2010년 이후 개봉한 영화 목록:")
print(movies_after_2010, "\n")

# 3. 평점이 9.0 이상인 영화 찾기
high_rated_movies = df[df["Rating"] >= 9.0]
print("3. 평점이 9.0 이상인 영화:")
print(high_rated_movies, "\n")

# 4. 특정 감독("Christopher Nolan")의 영화 목록 출력
nolan_movies = df[df["Director"] == "Christopher Nolan"]
print("4. Christopher Nolan 감독의 영화:")
print(nolan_movies, "\n")

# 5. 특정 예산 범위 내의 영화 찾기 (제작비 50백만 ~ 200백만)
budget_range_movies = df[(df["Budget_Million"] >= 50) & (df["Budget_Million"] <= 200)]
print("5. 제작비가 50백만 ~ 200백만인 영화:")
print(budget_range_movies, "\n")

# 6. 제작비 100백만 이상인 영화만 필터링
high_budget_movies = df[df["Budget_Million"] >= 100]
print("6. 제작비가 100백만 이상인 영화:")
print(high_budget_movies, "\n")

# 7. 관객 수가 100백만 이상인 영화만 찾기
high_audience_movies = df[df["Audience_Million"] >= 100]
print("7. 관객 수가 100백만 이상인 영화:")
print(high_audience_movies, "\n")

# 8. 가장 최근에 개봉한 영화 찾기 (max() 미사용)
# Year 기준으로 오름차순 정렬 후 마지막 행 선택
sorted_by_year = df.sort_values(by="Year")
most_recent_movie = sorted_by_year.iloc[-1]
print("8. 가장 최근에 개봉한 영화:")
print(most_recent_movie, "\n")

# 9. 가장 오래된 영화 찾기 (min() 미사용)
# Year 기준으로 오름차순 정렬 후 첫 행 선택
oldest_movie = sorted_by_year.iloc[0]
print("9. 가장 오래된 영화:")
print(oldest_movie, "\n")

# 10. 첫 5개의 영화만 출력 (df[:5] 또는 df.head(5) 미사용)
# iloc를 이용하여 첫 5행 선택
first_five_movies = df.iloc[0:5]
print("10. 첫 5개의 영화:")
print(first_five_movies, "\n")