def check(func):
  def wrapper(*args):
    if args[1] == 0:
      print("Denominator can't be zero")
    else:
      return func(*args)
  return wrapper

@check
def div(a, b):
  return a/b


div(6,0)
