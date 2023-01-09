#!/usr/bin/python3

multiple_returns = __import__('8-multiple_returns').multiple_returns

sentence = "At my first school, I first learnt C!"
length, first = multiple_returns(sentence)

print("Length: {:d} - First character: {}".format(length, first))


'''
#!/usr/bin/python3
def multiple_returns(sentence):
    if not sentence:
        sentence = None
        if sentence:
            sen_len = len(sentence)
        else:
            sen_len = 0
        return (sen_len, sentence if not sentence else sentence[:1])
'''
