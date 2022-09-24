import random


def generator(request):
	characters = list('abcdefghijklmnopqrstuvwxyz')

	if request.GET.get('uppercase'):
		characters.extend(list('ABCDEFGHIJKLMNOPQRSTUVWXYZ'))
	if request.GET.get('special'):
		characters.extend(list('!@#$%^&*()_+-=№?'))
	if request.GET.get('numbers'):
		characters.extend(list('1234567890'))

	length = int(request.GET.get('length', 12))
	thepassword = ''

	for x in range(length):
		thepassword += random.choice(characters)

	return thepassword