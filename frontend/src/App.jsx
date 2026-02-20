import { useState } from "react";
import ubcLogo from "./assets/ubc.svg";
import "./App.css";

import RandomWordButton from "./components/RandomWordButton";
import Excel_Form from "./components/Excel_Form";
import TutorialTabs from "./components/TutorialTabs";
function App() {
    return (
        /* Use a div or main instead of a fragment so Flexbox can see it as one block */
        <div className="app-container">
            <main className="main-content spacing">
                
                <h1> Ubc Workday Excel To ICalendar Converter</h1>
                <p>
                    {" "}
                    Really? Ubc or Workday couldn't have done it
                    themselves?{" "}
                </p>

                <RandomWordButton />

                <Excel_Form />
                <div className="pdf-wrapper"><TutorialTabs /></div>
                
            </main>

            <footer className="footer">
                <p>
                    Check out the source code on{" "}
                    <a
                        className="footer-link"
                        href="https://www.youtube.com/watch?v=dQw4w9WgXcQ"
                        target="_blank"
                        rel="noreferrer noopener"
                    >
                        Github
                    </a>
                </p>
            </footer>
        </div>
    );
}
export default App;
