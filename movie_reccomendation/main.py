import pandas as pd

# Load the MovieLens dataset (assuming you have 'ratings.csv' file)
# You can download the dataset from: https://grouplens.org/datasets/movielens/latest/
ratings = pd.read_csv('ratings.csv')  # Replace with the actual path to your ratings.csv file

# Load the movies dataset (assuming you have 'movies.csv' file)
movies = pd.read_csv('movies.csv')  # Replace with the actual path to your movies.csv file

# Calculate average ratings for each movie
movie_ratings = ratings.groupby('movieId')['rating'].mean().reset_index()

# Function to get movie recommendations for a given user
def get_movie_recommendations(user_id, num_recommendations=5):
    # Get movies not rated by the user
    unrated_movies = movie_ratings[~movie_ratings['movieId'].isin(ratings[ratings['userId'] == user_id]['movieId'])]

    # Sort movies by average rating in descending order
    unrated_movies = unrated_movies.sort_values(by='rating', ascending=False)

    # Get top N recommended movies
    top_recommendations = unrated_movies.head(num_recommendations)

    # Get movie titles for the recommendations
    movie_titles = [movies[movies['movieId'] == movie_id]['title'].iloc[0] for movie_id in top_recommendations['movieId']]

    return movie_titles

# Example usage
user_id_to_recommend = 1
recommendations = get_movie_recommendations(user_id_to_recommend)
print(f"Top 5 Movie Recommendations for User {user_id_to_recommend}:")
for i, movie_title in enumerate(recommendations, start=1):
    print(f"{i}. {movie_title}")
