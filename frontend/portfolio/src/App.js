import React, { useEffect, useState } from 'react';
import axios from 'axios';

function App() {
  const [resume, setResume] = useState({});

  useEffect(() => {
    axios.get('http://localhost:8000/api/resume/')
      .then(res => setResume(res.data))
      .catch(err => console.error(err));
  }, []);

  return (
    <div>
      <h1>{resume.name}</h1>
      <h2>{resume.job}</h2>
      <ul>
        {resume.skills && resume.skills.map((skill, i) => (
          <li key={i}>{skill}</li>
        ))}
      </ul>
    </div>
  );
}

export default App;