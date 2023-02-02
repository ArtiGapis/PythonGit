import logging

# logging.DEBUG is a constant, not the same as logging.debug() function
# ... if you are running this in collab, you need to constantly restart the environment
# ... to see the effects of log level changes
logging.basicConfig(filename='logs/main.log', level=logging.INFO)

def add(i, j):
  return i + j

def multiply(i, j):
  return i * j

res_add = add(3, 2)
res_multiply = multiply(3, 2)

logging.info('{} : {}'.format('Addition result', res_add))
logging.info('{} : {}'.format('Multiplication result', res_multiply))