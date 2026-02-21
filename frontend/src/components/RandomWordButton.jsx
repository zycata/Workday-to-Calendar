import { useState } from "react";
import './interactive_parts.css';
function RandomWordButton() {
    const [loading, setLoading] = useState(false);
    const [word, setWord] = useState("Click this for words of encouragement!");

    const fetchWord = async () => {
        setLoading(true); 
        try {
            const response = await fetch("/get-word");
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
        <h3 onClick={fetchWord} disabled={loading} className="prevent-select fun-text">
            {loading ? "Fetching..." : `${word}`}
        </h3>
    );
}

export default RandomWordButton;