import threading

def print_cube(num):
  print(f"Cube {num ** 3}")

def print_square(num):
  print(f"Square {num ** 2}")

def run():
  t1.start()

if __name__ == "__main__":
  t1 = threading.Thread(target=print_cube, args=(10,), daemon=True)
  t2 = threading.Thread(target=print_square, args=(3,))

  # start threading 1
  t1.start()
  # start threading 2
  t2.start()

  # wait until threading 1 complete
  t1.join()

  # wait until threading 2 complete
  t1.join()

  print("Done")

