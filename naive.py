states = ('a', 'b', 'c')

observations = ('00', '10', '11')

transition_probability = {
	'a' : {'a': 0.7, 'b': 0.2, 'c': 0.1},
	'b' : {'a': 0.2, 'b': 0.7, 'c': 0.1},
	'c' : {'a': 0.1, 'b': 0.1, 'c': 0.8}
	}

emission_probability = {
	'a' : {'00': 0.75, '10': 0.1, '11': 0.15},
	'b' : {'00': 0.15, '10': 0.6, '11': 0.25},
	'c' : {'00': 0.1, '10': 0.1, '11': 0.8},
	}

start_probability = {'a': 0.2, 'b': 0.2, 'c': 0.6}

def comb(List,n):
    T=[]
    if n==1:
        return List
    for i in List:
        for item in comb(List,n-1):
            a = i + item
            T.append(a)
    return T

def naive(states, obs_seq, start_prob, trans_prob, emit_prob):
    V = []
    m=len(states)**len(obs_seq)
    for state in comb(states,len(obs_seq)):
        p_em =1
        for j in range(len(obs_seq)):
            p_em = p_em * emit_prob[state[j]][obs_seq[j]]
        p_tra =1
        for j in range(len(obs_seq)-1):
            p_tra = p_tra * trans_prob[state[j]][state[j-1]]
        p = p_em * p_tra * start_probability[state[0]]
        V.append([p,state])
    P = max(V)
    return (P)

print(naive(states,['11','10','00','00','10','11'], start_probability, transition_probability, emission_probability))
