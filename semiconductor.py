class exc(Exception):
	types = {}
	types["NV"] = "Not Enough or too many Values. Required at least 2."
	types["NB"] = "Non base 2 numbers. . ."
class calculate(exc):
	def __init__(self, instance_numbers=[0, 1], output_answer=True):
		for items in [(len(instance_numbers) != 2, "NV"), (len([bob for bob in instance_numbers if bob not in [1, 0]]) != 0, "NB")]:
			if items[0] != False:
				raise exc(exc.types[items[1]])
		self.orinst = instance_numbers[0] or instance_numbers[1]
		print("[DATA] Number value: %d. . .[DISJUNCTION]"%(self.orinst))
		self.andinst = instance_numbers[0] and instance_numbers[1]
		print("[DATA] Number value: %d . . .[CONJUCTION]"%(self.andinst))
	@property
	def calculateIt(self):
		cases = {1:0, 0:1}[self.andinst]
		print("[DATA] Negative: %d. . ."%(cases) + "\r\x0A" + "\x2D"*25)
		final_answer = self.orinst and cases
		print("\r\x0A\r\x0A[DATA] Final answer: %d"%(final_answer))

