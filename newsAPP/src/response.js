const newsListEndpoint = 'http://localhost:8000/articles/latest';

const fetchData = async () => {
  try {
    const response = await fetch(newsListEndpoint);

    if (!response.ok) {
      throw new Error(`HTTP error! Status: ${response.status}`);
    }

    const newsList = await response.json();
    return newsList;

  } catch (error) {
    console.error('Error fetching data:', error.message);
  }
};

export default fetchData;

