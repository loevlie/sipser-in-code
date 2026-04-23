import { useState } from "react";

export default function RegexTab() {
  const [pattern, setPattern] = useState("(a|b)*abb");
  const [input, setInput] = useState("aabb");
  const [result, setResult] = useState(null);

  async function run() {
    // TODO: POST /regex/match and display the trace + NFA diagram
    setResult("not-implemented");
  }

  return (
    <section>
      <h2>Regular languages</h2>
      <label>pattern <input value={pattern} onChange={e => setPattern(e.target.value)} /></label>
      <label>input   <input value={input} onChange={e => setInput(e.target.value)} /></label>
      <button onClick={run}>Match</button>
      <pre>{String(result)}</pre>
    </section>
  );
}
