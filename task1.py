def mood_response(mood):
  """Provides a custom message based on the user's entered mood.

  Args:
      mood: A string representing the user's mood.

  Returns:
      A string containing a message corresponding to the entered mood.
  """
  mood_messages = {
      "happy": "That's wonderful to hear! I hope you have a fantastic day!",
      "sad": "I'm sorry to hear that. Is there anything I can do to help?",
      "excited": "That's awesome! What are you excited about?",
      "angry": "It's okay to feel angry sometimes. Want to talk about it?",
      "stressed": "Take a deep breath. Remember, you've got this!"
  }

  if mood.lower() in mood_messages:
    return mood_messages[mood.lower()] 
  else:
    return "I'm not quite sure how to respond to that, but I hope you feel better soon."