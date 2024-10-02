def mad_libs_generator():
    story_template = "Once upon a time, there was a {adjective} {noun} who loved to {verb} {adverb}."
    
    print('Welcome to Mad Libs Generator!')
    print('Please provide the following:')
    
    adjective = input('An adjective: ')
    noun = input('A noun: ')
    verb = input('A verb: ')
    adverb = input('An adverb: ')
    
    story = story_template.format(adjective=adjective, noun=noun, verb=verb, adverb=adverb)
    
    print('\nHere\'s your Mad Libs story:')
    print(story)

mad_libs_generator()