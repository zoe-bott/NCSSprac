import re
import random

TUTORS = ['Tim', 'Nicky', 'Kenni', 'Ben', 'Smerity']


# ---
# REGISTER THE STATES
# Connects our states (eg. 'LOCKED OUT') with our functions (eg. locked_out_on_enter_state)
# ---

# What to do when we enter a state
def on_enter_state(state, context):
  if state == 'NO QUERY':
    return no_query_on_enter_state(context)
  elif state == 'MAYBE':
    return maybe_on_enter_state(context)
  elif state == 'NO TIME GIVEN':
    return no_time_given_on_enter_state(context)

  # elif state == 'LOCKED OUT LOCATION':
    # return locked_out_location_on_enter_state(context)
  # More states here
  # elif state == ...

# What to do when we receive input while in a state
def on_input(state, user_input, context):
  # First up, if they're trying to quit, then quit.
  if user_input == 'quit':
    return 'END', {}, 'Bye!'

  # Otherwise, check the state.
  if state == 'NO QUERY':
    return no_query_on_input(user_input, context)
  elif state == 'MAYBE':
    return no_time_given_on_input(user_input, context)
  else: 
    return 'END', {}, "I don't understand"
  # elif state == 'LOCKED OUT LOCATION':
    # return locked_out_location_on_input(user_input, context)
  # More states here
  # elif state == ...


# ---
# START STATE
# The big start state that knows where to send the user.
# ---

def no_query_on_enter_state(context):
  return 'Are you still going to the event?' 

def no_query_on_input(user_input, context):
  pattern = r'remind me in (?P<time>[0-9]+) (?P<units>(minute|hour)s?)'
  match = re.search(pattern, user_input.lower())
  if 'yes' in user_input.lower(): 
    return 'END', {}, 'Okay, have fun.'
  elif 'no' in user_input.lower():
    return 'END', {}, 'Okay. I will tell the others.'
  elif match: 
    time = match.group('time')
    units = match.group('units')
    return 'END', {}, f'Setting a reminder in {time} {units}(s)'
  elif 'remind me' in user_input.lower(): 
    return 'MAYBE', {}, None

  else:
    return 'END', {}, 'Sorry, I don\'t understand!'


# ---
# OTHER STATES
# ---

# TODO: Replace these states with your project's cool states

# MAYBE state

def maybe_on_enter_state(context):
  return 'When do you want me to remind you?'


def maybe_on_input(user_input, context):
  #Store the full response text as the location.
  pattern = r'remind me in (?P<time>[0-9]+) (?P<units>(minute|hour)s?)'
  match = re.search(pattern, user_input.lower())
  if match: 
    remindtime = user_input
    time = match.group('time')
    units = match.group('units')
    return 'END', {'remindtime': remindtime}, f'Setting a reminder in {time} {units}(s)'
  else: 
    return 'END', {}, 'Sorry, I dont understand'

def no_time_given_on_input(user_input, context): 
  pattern = r'(?P<time>[0-9]+) (?P<units>(minute|hour)s?)'
  match = re.search(pattern, user_input.lower())
  if match: 
    remindtime = user_input
    time = match.group('time')
    units = match.group('units')
    return 'END', {'remindtime': remindtime}, f'Setting a reminder in {time} {units}(s)'
  # still need to add an else statement for if match is not found 

def locked_out_location_on_input(user_input, context):
  return 'END', {}, 'Bye!'


# --- More states go here! --- #
