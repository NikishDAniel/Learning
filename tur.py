import pgmpy.models
'''import pgmpy.inference
import networkx as nx'''
#import pylabs as plt 
model = pgmpy.models.BayesianModel([('Burglary', 'Alarm'),('Earthquake', 'Alarm'),('Alarm', 'JohnCalls'),('Alarm', 'MaryCalls')])

cpd_burglary = pgmpy.factors.discrete.TabularCPD('Burglary', 2, [[0.001], [0.999]])

cpd_earthquake = pgmpy.factors.discrete.TabularCPD('Earthquake', 2, [[0.002], [0.998]])

cpd_alarm = pgmpy.factors.discrete.TabularCPD('Alarm', 2, [[0.95, 0.94, 0.29, 0.001],[0.05, 0.06, 0.71, 0.999]],evidence=['Burglary', 'Earthquake'],evidence_card=[2, 2])

cpd_john = pgmpy.factors.discrete.TabularCPD('JohnCalls', 2, [[0.90, 0.05],[0.10, 0.95]],evidence=['Alarm'],evidence_card=[2])

cpd_mary = pgmpy.factors.discrete.TabularCPD('MaryCalls', 2, [[0.70, 0.01],[0.30, 0.99]],evidence=['Alarm'],evidence_card=[2])

model.add_cpds(cpd_burglary, cpd_earthquake, cpd_alarm, cpd_john, cpd_mary)

model.check_model()

'''print('Probability distribution, P(Burglary)')
print(cpd_burglary)
print()
print('Probability distribution, P(Earthquake)')
print(cpd_earthquake)
print()
print('Joint probability distribution, P(Alarm | Burglary, Earthquake)')
print(cpd_alarm)
print()
print('Joint probability distribution, P(JohnCalls | Alarm)')
print(cpd_john)
print()
print('Joint probability distribution, P(MaryCalls | Alarm)')
print(cpd_mary)
print()
nx.draw(model, with_labels=True)
plt.savefig('C:\\DATA\\Python-data\\bayesian-networks\\alarm.png')
plt.close()

infer = pgmpy.inference.VariableElimination(model)

posterior_probability = infer.query(['Burglary'], evidence={'JohnCalls': 0, 'MaryCalls': 0})

print('Posterior probability of Burglary if JohnCalls(True) and MaryCalls(True)')
print(posterior_probability)
print()
posterior_probability = infer.query(['Alarm'], evidence={'Burglary': 0, 'Earthquake': 0})

print('Posterior probability of Alarm sounding if Burglary(True) and Earthquake(True)')
print(posterior_probability)
print()
'''