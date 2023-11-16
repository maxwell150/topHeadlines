import React, { useState } from "react";
import './Api.css'
import './App.css'
import fetchData from "./response";


const Api = () => {
  const [apiKey, setApiKey] = useState(null);

  const generateApiKey = async () => {
    try {
      const response = await fetch('http://127.0.0.1:8000/generate_api_key');
      const data = await response.json();
      setApiKey(data.api_key);
    } catch (error) {
      console.error('Error generating API key:', error);
    }
  };

  return (
    <div className="response-body">
      <h1>Get Your Daily News</h1>
      <hr />
      <button onClick={generateApiKey}>Generate API Key</button>

      {apiKey && (
        <div>
          Your API Key: <b>{apiKey}</b>
          <br />
          <b>Usage:</b>
          <hr />
          <br />
          <code className="curl">
            <b>CURL</b>
            <br />
            <span>curl -X</span>'GET'\
            'http://localhost:8000/articles/apiKey={apiKey}' \-H 'accept: application/json'
          </code>
          <br />
          <code className="response">
            <b>Request URL</b>
            <br />
            http://localhost:8000/articles/apiKey={apiKey}
          </code>
          <br />
          Response body:
          <br />
          <table>
            <thead>
              <tr>
                <td>Code:</td>
                <td>Detail</td>
              </tr>
            </thead>
            <tbody>
              <tr>
                <td>200</td>
                <td>
                  <h5>Response body</h5>
                </td>
              </tr>
            </tbody>
          </table>
        </div>
      )}
    </div>
  );
};

export default Api;
