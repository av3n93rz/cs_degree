class Example:
  x = 0

  def increase(self, x):
    self.x = self.x + x
    print('Current value:', self.x)

example = Example()

example.increase(2)
example.increase(3)
example.increase(4)