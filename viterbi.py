states = ('a', 'b', 'c')

observations = ('00', '10', '11')

transition_probability = {
	'a' : {'a': 0.7, 'b': 0.2, 'c': 0.1},
	'b' : {'a': 0.2, 'b': 0.7, 'c': 0.1},
	'c' : {'a': 0, 'b': 0.1, 'c': 0.9}
	}

emission_probability = {
	'a' : {'00': 0.75, '10': 0.1, '11': 0.15},
	'b' : {'00': 0.15, '10': 0.6, '11': 0.25},
	'c' : {'00': 0.1, '10': 0.1, '11': 0.8},
	}

start_probability = {'a': 0.2, 'b': 0.2, 'c': 0.6}

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
	return (p,path[s])


print(viterbi(states,  ['11','10','00','00','10','11'], start_probability, transition_probability, emission_probability))
