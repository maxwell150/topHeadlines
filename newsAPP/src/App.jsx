import React from 'react';
import { BrowserRouter as Router, Route, Routes, Navigate } from 'react-router-dom';
import Article from './Article';
import Api from './Api';

const App = () => {
  return (
    <>
    <Router>
      <Routes>
        <Route exact path="/" element={<Article />} />
        <Route path="/developers" element={<Api />} />
        <Route path="*" element={<Navigate to="/" />} />
      </Routes>
    </Router>
    </>
  );
}

export default App;