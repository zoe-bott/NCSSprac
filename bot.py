import re
import random

# ---
# REGISTER THE STATES
# Connects our states (eg. 'LOCKED OUT') with our functions (eg. locked_out_on_enter_state)
# ---

# What to do when we enter a state
def on_enter_state(state, context):
  if state == 'SETUP':
    return setup_state(context)
  elif state == 'PUNCHLINE':
    return punchline_state(context)
  # More states here
  # elif state == ...

# What to do when we receive input while in a state
def on_input(state, user_input, context):

  # Otherwise, check the state.
  if state == 'SETUP':
    return no_query_on_input(user_input, context)
  # More states here
  # elif state == ...


# ---
# START STATE
# The big start state that knows where to send the user.
# ---

def no_query_on_enter_state(context):
  return 'Let me tell you a joke.'

def setup_state(user_input, context):
  return 'PUNCHLINE', {}, context[setup]


# ---
# OTHER STATES
# ---

# TODO: Replace these states with your project's cool states

def punchline_state(context):
  return 'SETUP', {}, context[punchline]



# --- More states go here! --- #
