import { useState } from "react";
import reactLogo from "./assets/react.svg";
import viteLogo from "/vite.svg";
import "./App.css";

import RandomWordButton from "./components/RandomWordButton";
import Excel_Form from "./components/Excel_Form";

function App() {
    const [count, setCount] = useState(0);
    const handleFormSubmit = (e) => {
        e.preventDefault();
        console.log("Clicked submit");

        // This is where you would handle the file upload logic
        const fileInput = document.getElementById("fileInput");
        console.log("Selected file:", fileInput.files[0].name);
    };
    return (
        <>
            <div>
                <RandomWordButton />
                <button onClick={() => setCount((count) => count + 1)}>
                    count is {count}
                </button>
            </div>

            <div>
                <Excel_Form/>
            </div>

            <p>
                Edit <code>src/App.jsx</code> and save to test HMR
            </p>

            <p className="read-the-docs">
                Click on the Vite and React logos to learn more
            </p>
        </>
    );
}

export default App;
