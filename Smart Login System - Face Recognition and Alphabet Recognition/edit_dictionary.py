import pickle


def edit_in_dictionary(name,email):

	a_file = open("data.pkl", "rb")
	dictionary = pickle.load(a_file)


	dictionary[name] = email

	a_file = open("data.pkl", "wb")
	pickle.dump(dictionary, a_file)
	a_file.close()
	return

def get_email(name):
	a_file = open("data.pkl", "rb")
	dictionary = pickle.load(a_file)


	email = dictionary[name]

	a_file = open("data.pkl", "wb")
	pickle.dump(dictionary, a_file)
	a_file.close()

	return email


def get_dict():
	a_file = open("data.pkl", "rb")
	dictionary = pickle.load(a_file)


	

	print(dictionary)

	a_file = open("data.pkl", "wb")
	pickle.dump(dictionary, a_file)
	a_file.close()


