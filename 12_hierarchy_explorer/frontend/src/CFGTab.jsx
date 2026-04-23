import { useState } from "react";

export default function CFGTab() {
  const [grammar, setGrammar] = useState('{\n  "start": "S",\n  "rules": {"S": [["a","S","b"], ["ab"]]}\n}');
  const [input, setInput] = useState("aabb");
  const [result, setResult] = useState(null);

  async function run() {
    // TODO: POST /cfg/parse and render the CYK chart / parse tree
    setResult("not-implemented");
  }

  return (
    <section>
      <h2>Context-free languages</h2>
      <label>grammar (JSON)
        <textarea value={grammar} onChange={e => setGrammar(e.target.value)} rows={8} cols={40} />
      </label>
      <label>input <input value={input} onChange={e => setInput(e.target.value)} /></label>
      <button onClick={run}>Parse</button>
      <pre>{String(result)}</pre>
    </section>
  );
}
