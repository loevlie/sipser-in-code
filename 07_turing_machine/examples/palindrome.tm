# TODO: TM that recognizes palindromes over {a,b}.
# Sketch: repeatedly strip matching first/last characters.
states: q0, q_accept, q_reject
input_alphabet: a, b
tape_alphabet: a, b, _
start: q0
accept: q_accept
reject: q_reject

# transitions go here — leave blank for now, fill in as you build
