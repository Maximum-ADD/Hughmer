import { useState } from "react"


export default function JokeCard() {
    const [setup, setSetup] = useState("")
    const [punchline, setPunchline] = useState("")
    const [score, setScore] = useState(null)
    const [loading, setLoading] = useState(false)

    async function handleScore(){
        setLoading(true)
        const res = await fetch(`${import.meta.env.VITE_API_URL}/dad-joke-score`, {
            method: "POST",
            headers: {"Content-Type": "application/json"},
            body: JSON.stringify({setup, punchline})
        })
        const data = await res.json()
        setScore(data.score)
        setLoading(false)
    }
    return (
    <section>
        <h2>Test your joke</h2>
        <label>
            Setup
            <input
                placeholder="Setup..."
                value={setup}
                onChange={e => setSetup(e.target.value)}
            />
        </label>
        <label>
            Punchline
            <input
                placeholder="Punchline..."
                value={punchline}
                onChange={e => setPunchline(e.target.value)}
            />
        </label>
        <button onClick={handleScore}>
            {loading ? "Scoring..." : "Score my joke"}
        </button>
        {score !== null && <output>Unpredictability score: {score}</output>}
    </section>
)
}
