import React, { useState, useEffect } from 'react';
import PropTypes from 'prop-types';
import axios from 'axios';

function MovieList({ onMovieClick }) {
  const [movies, setMovies] = useState([]);
  const [error, setError] = useState('');

  useEffect(() => {
    const fetchMovies = async () => {
      try {
        const response = await axios.get(`${process.env.REACT_APP_MOVIE_API_URL}/movies`);
        setMovies(response.data.movies || []);
      } catch (err) {
        setError('Unable to load movies right now.');
        setMovies([]);
      }
    };

    fetchMovies();
  }, []);

  return (
    <>
      {error && <p role="alert">{error}</p>}
      <ul>
        {movies.map((movie) => (
          <li className="movieItem" key={movie.id} onClick={() => onMovieClick(movie)}>
            {movie.title}
          </li>
        ))}
      </ul>
    </>
  );
}

MovieList.propTypes = {
  onMovieClick: PropTypes.func.isRequired,
};

export default MovieList;
