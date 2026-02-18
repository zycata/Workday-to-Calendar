import { useState } from 'react'
import reactLogo from './assets/react.svg'
import viteLogo from '/vite.svg'
import './App.css'

function App() {
  const [count, setCount] = useState(0)
  
  const [loading, setLoading] = useState(false);
  const [word, setWord] = useState("Click to start...");
  
  const fetchWord = async () => {
    try {
      const response = await fetch("http://127.0.0.1:5100/get-word");
      const data = await response.json();
      setWord(data.word);
    } catch (error) {
      console.error("Error fetching data:", error);
      setWord("Error :(");
    }
  };

 
  return (
    <>
      
      
      <div className="card">
        <button onClick={() => setCount((count) => count + 1)}>
          count is {count}
        </button>
        <button onClick={fetchWord} disabled={loading}>
          {loading ? "Fetching..." : `Current word: ${word}`}
        </button>
        
        <p>
          Edit <code>src/App.jsx</code> and save to test HMR
        </p>
      </div>
      <p className="read-the-docs">
        Click on the Vite and React logos to learn more
      </p>
    </>
  )
}

export default App
