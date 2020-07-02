import tkinter as tk


states = ('N', 'M', 'V')

observations = ('Jane', 'Will', 'Spot')

transition_probability = {
        '<S>' : {'N': 3/4, 'M': 1/4, 'V': 0, '<E>' : 0},
	'N' : {'N': 1/9, 'M': 1/3, 'V': 1/9, '<E>' : 4/9},
	'M' : {'N': 1/4, 'M': 0, 'V': 3/4, '<E>' : 0},
	'V' : {'N': 1, 'M': 0, 'V': 0, '<E>' : 0}
	}

emission_probability = {
	'N' : {'Jane': 2/9, 'Will': 1/9, 'Spot': 2/9},
	'M' : {'Jane': 0, 'Will': 3/4, 'Spot': 0},
	'V' : {'Jane': 0, 'Will': 0, 'Spot': 1/4},
	}

start_probability = {'N': 2/9, 'M': 0, 'V': 0}

def viterbi(states, obs_seq, start_prob, trans_prob, emit_prob):
	V = [{}]
	path = {}
	for state in states:
		V[0][state]=start_prob[state]*emit_prob[state][obs_seq[0]]
		path[state]=[state];
	for t in range(1, len(obs_seq)):
		V.append({})
		newpath = {}
		for state in states:
			(p,s) = max([(V[t-1][i]*trans_prob[i][state]*emit_prob[state][obs_seq[t]],i) for i in states])
			V[t][state] = p;
			newpath[state] = path[s] + [state];
		path = newpath
	(p,s) = max([(V[len(obs_seq)-1][y], y) for y in states])
	return path[s]

print(viterbi(states,  ['Jane','Will','Spot','Will'], start_probability, transition_probability, emission_probability))
