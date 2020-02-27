from StMachine import StateMachine
import collections



st = StateMachine.StateMachine()

dic = ['0', '1', '0', '2', '0', '2']

print("Dictionary:", ''.join(dic))
#print(''.join(dic))

st.translate(dic)

st.print()




