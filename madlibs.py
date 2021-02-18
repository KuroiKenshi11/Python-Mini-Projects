"""
This is a madlib project where you can work with string and complete the sentence with the correct world.
"""
sentence = "I wake up early that morning and looked outside my window. There was a ____ amount of snow! I couldn't believe mye eyes. It looked so ____. I ran downstairs and turned on the television. School was  closed! I ____ly got dressed and hurriied outside. It was ____. The first thing I did was ____ a snowman. He looks like this."
print(sentence)
print("After you read the pragraph, see if you can complete it with the correct word.")
adj = input("Adjective:")
noun = input("Noun: ")
adj2 = input("Adjective: ")
noun2 = input("Noun: ")
verb = input("Verb: ")

sentence = f"I wake up early that morning and looked outside my window. There was a {adj} amount of snow! I couldn't believe mye eyes. It looked so {noun}. I ran downstairs and turned on the television. School was  closed! I {adj2}ly got dressed and hurriied outside. It was {noun2}. The first thing I did was {verb} a snowman. He looks like this."
print(sentence)
