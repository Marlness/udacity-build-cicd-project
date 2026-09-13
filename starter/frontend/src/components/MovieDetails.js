import React, { useState, useEffect } from 'react';
import PropTypes from 'prop-types';
import axios from 'axios';

function MovieDetail({ movie }) {
  const [details, setDetails] = useState(null);
  const [error, setError] = useState('');

  useEffect(() => {
    const fetchMovieDetails = async () => {
      try {
        const response = await axios.get(`${process.env.REACT_APP_MOVIE_API_URL}/movies/${movie.id}`);
        setDetails(response.data);
      } catch (err) {
        setError('Unable to load movie details.');
        setDetails(null);
      }
    };

    fetchMovieDetails();
  }, [movie]);

  return (
    <div>
      {error && <p role="alert">{error}</p>}
      <h2>{details?.movie.title}</h2>
      <p>{details?.movie.description}</p>
    </div>
  );
}

MovieDetail.propTypes = {
  movie: PropTypes.shape({
    id: PropTypes.oneOfType([PropTypes.string, PropTypes.number]),
    title: PropTypes.string,
    description: PropTypes.string,
  }).isRequired,
};

export default MovieDetail;
