def my_function(*args, **kwargs):
  """This function takes an arbitrary number of positional arguments and keyword arguments."""

  # Print the positional arguments
  for arg in args:
    print(arg)

  # Print the keyword arguments
  #item() method is used to iterate over the keyword arguments passed to the my_function() function
  for key, value in kwargs.items():
    print(f"{key}={value}")


if __name__ == "__main__":
  # Call the function with some positional arguments
  my_function(1, 2, 3)

  # Call the function with some keyword arguments
  my_function(a=1, b=2, c=3)
