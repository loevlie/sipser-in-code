import { useState } from "react";
import RegexTab from "./RegexTab.jsx";
import CFGTab from "./CFGTab.jsx";
import TMTab from "./TMTab.jsx";

const TABS = [
  { id: "regex", label: "Regular", component: RegexTab },
  { id: "cfg", label: "Context-Free", component: CFGTab },
  { id: "tm", label: "Turing-Recognizable", component: TMTab },
];

export default function App() {
  const [active, setActive] = useState("regex");
  const Active = TABS.find((t) => t.id === active).component;
  return (
    <div style={{ fontFamily: "system-ui", padding: 24 }}>
      <h1>Chomsky Hierarchy Explorer</h1>
      <nav>
        {TABS.map((t) => (
          <button
            key={t.id}
            onClick={() => setActive(t.id)}
            style={{ fontWeight: active === t.id ? "bold" : "normal" }}
          >
            {t.label}
          </button>
        ))}
      </nav>
      <main style={{ marginTop: 24 }}>
        <Active />
      </main>
    </div>
  );
}
