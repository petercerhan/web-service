

def class_implements_method(subject_class, method_name):
		if not hasattr(subject_class, method_name):
			return False
		method = getattr(subject_class, method_name)
		return callable(method)