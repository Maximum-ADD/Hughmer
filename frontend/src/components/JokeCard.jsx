import { useState } from "react"


export default function JokeCard() {
    const [setup, setSetup] = useState("")
    const [punchline, setPunchline] = useState("")
    const [score, setScore] = useState(null)
    const [loading, setLoading] = useState(false)

    async function handleScore(){
        try {
            const controller = new AbortController()
            const timeout = setTimeout(() => controller.abort, 10000)


            setLoading(true)
            const res = await fetch(`${import.meta.env.VITE_API_URL}/dad-joke-score`, {
                method: "POST",
                headers: {"Content-Type": "application/json"},
                body: JSON.stringify({setup, punchline}),
                signal: controller.signal
            })

            clearTimeout(timeout)

            const data = await res.json()
            setScore(data.score)
        } catch (error) {
            if (error.name === 'AbortError') {
                setScore('timeout')
            }
            
        } finally {
            setLoading(false)
        }
    }
    return (
    <section className= "bg-white/5 border border-white/10 rounded-2x1 p-8 flex flex-col gap-6">
        <h2 className="text-xl font-semibold text-amber-400">Test your joke</h2>
        <label className="flex flex-col gap-2 text-sm text-white/60">
            Setup
            <input
                placeholder="Setup..."
                value={setup}
                onChange={e => setSetup(e.target.value)}
                className="bg-black border border-white/20 rounded-lg px-4 py-3 text-white placeholder:text-white/20 focus:outline-none focus:border-amber-400"
            />
        </label>
        <label className="flex flex-col gap-2 text-sm text-white/60">
            Punchline
            <input
                placeholder="Punchline..."
                value={punchline}
                onChange={e => setPunchline(e.target.value)}
                className="bg-black border border-white/20 rounded-lg px-4 py-3 text-white placeholder:text-white/20 focus:outline-none focus:border-amber-400"

            />
        </label>
        <button 
        onClick={handleScore} 
        className="bg-amber-400 text-black font-bold py-3 rounded-lg hover:bg-amber-300 transition-colors"
        >
            {loading ? "Scoring..." : "Score my joke"}
        </button>
        {
            score === 'timeout' && (
            <output className="text-center text-2xl font-bold text-red-400">
            Timeout!! server is starting up. may be an over 60 second wait.
            </output>
            )
        }
        {
            score !== null && score !== 'timeout' && (
            <output className="text-center text-2xl font-bold text-amber-400">
            Unpredictability score: {score}
            </output>
            )
        }
    </section>
)
}
