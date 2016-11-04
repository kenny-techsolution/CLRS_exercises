class Hash_table_mul(object):
	def hash_insert(self, key):
		#r = , w-bit w
		r = 2
		m = 2**r
		w = 32
		A = (2**(w-1)+2**w)/2
		print(A)
		print(((key*A)%(2**w)))
		val = '{0:032b}'.format((key*A)%(2**w))
		print(val)
		shift_bit = w-r
		print(shift_bit)
		hash_key = ((key*A)%(2**w))>>(w-r)
		print(hash_key)
htm = Hash_table_mul()
htm.hash_insert('{0:032b}'.format(56))

input_key = 56
print('{0:032b}'.format(56))