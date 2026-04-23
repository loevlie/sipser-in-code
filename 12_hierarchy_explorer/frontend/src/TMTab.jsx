import { useState } from "react";

export default function TMTab() {
  const [tm, setTm] = useState("");
  const [input, setInput] = useState("aabbaa");
  const [state, setState] = useState(null);

  async function step() {
    // TODO: POST /tm/step, animate the tape one cell at a time
    setState("not-implemented");
  }

  return (
    <section>
      <h2>Turing-recognizable languages</h2>
      <label>TM spec
        <textarea value={tm} onChange={e => setTm(e.target.value)} rows={10} cols={50} />
      </label>
      <label>input <input value={input} onChange={e => setInput(e.target.value)} /></label>
      <button onClick={step}>Step</button>
      <pre>{String(state)}</pre>
    </section>
  );
}
