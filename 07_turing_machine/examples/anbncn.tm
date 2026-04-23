# TODO: TM that decides { a^n b^n c^n : n >= 0 }.
# Non-context-free. Classic exercise: mark one a, one b, one c per pass.
states: q0, q_accept, q_reject
input_alphabet: a, b, c
tape_alphabet: a, b, c, A, B, C, _
start: q0
accept: q_accept
reject: q_reject

# transitions go here — leave blank for now, fill in as you build
