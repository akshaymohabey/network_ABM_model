import main
import parameters as p
import matplotlib.pyplot as plt


main_instance = main.main()
main_instance.create_agents()
main_instance.random_network_2()
main_instance.record_agents_states()

for t in range(p.time_steps):
	main_instance.game()
	main_instance.record_agents_states()

all_states = main_instance.agents_states

ratios_list = []

for t in range(p.time_steps):
	states = all_states[t]
	n = float(len(states))
	zeros = float(states.count(0))
	ratio = zeros/n
	ratios_list.append(ratio)

plt.plot(ratios_list[:40])
plt.xlabel("Time steps")
plt.ylabel("Ratio (zero/one)")
plt.show()


