import { useState } from "react";

function RandomWordButton() {
    const [loading, setLoading] = useState(false);
    const [word, setWord] = useState("Click to start...");

    const fetchWord = async () => {
        setLoading(true); 
        try {
            const response = await fetch("http://127.0.0.1:5100/get-word");
            const data = await response.json();
            setWord(data.word);
        } catch (error) {
            console.error("Error fetching data:", error);
            setWord("Error :(");
        } finally {
            setLoading(false); 
        }
    };

    return (
        <button onClick={fetchWord} disabled={loading} >
            {loading ? "Fetching..." : `Current word: ${word}`}
        </button>
    );
}

export default RandomWordButton;