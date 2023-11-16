import { useState, useEffect } from 'react'
import './App.css'
import axios from 'axios'
import React from 'react'
import TruncatedText from './truncate'
import { Link } from 'react-router-dom';


const Article = () => {
  const [data, setData] = useState([]);
  const [loading, setLoading] = useState(true);

  const max_length = 200;

  useEffect(() => {
    const fetchData = async () => {
      try {
        const response = await axios.get('http://127.0.0.1:8000/articles');
        setData(response.data);
        setLoading(false);
      } catch (error) {
        console.error('Error fetching data:', error);
        setLoading(false);
      }
    };

    fetchData();
  }, []);

  return (
    <div>
      <nav>
        <Link to='/developers'>
          <button>For Developers</button>
        </Link>
        <h1>Get Your Daily News</h1>
        <hr />
      </nav>

      <div className='container'>
        <section className='headlines'>
          <h3>Top Headlines</h3>
          <hr />
          <ul>
            {data.map(item => (
              <li key={item.id}>
                <a href={item.source_url} target='_blank' rel='noopener noreferrer'>
                  {item.title}
                </a>
              </li>
            ))}
          </ul>
        </section>
        <div className='articles'>
          {loading ? (
            <p>Loading...</p>
          ) : (
            <article>
              {data.map(item => (
                <div key={item.id} className='newsArticle truncate-text'>
                  <h2>
                    <a href={item.source_url} target='_blank' rel='noopener noreferrer'>
                      {item.title}
                    </a>
                  </h2>
                  <span>
                    <small>by {item.author}</small>
                  </span>
                  <br />
                  <img src={item.url_to_image} alt='news' />
                  <h3>{item.description}</h3>
                  <p>
                    <TruncatedText text={item.content} maxLength={max_length} />
                  </p>
                </div>
              ))}
            </article>
          )}
        </div>
      </div>
    </div>
  );
};

export default Article;



