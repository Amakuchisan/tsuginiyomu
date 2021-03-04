def get():
    stop_words = []
    with open('/work/stop_words/stop_words.csv', 'r') as f:
        for line in f:
            line = line.rstrip()
            l = line.split(",")
            stop_words.extend(l)
    return stop_words

# nd = d
# for i, n in enumerate(nd):
#     print(i)
#     nd[n] = i
#     print(nd)

# s = sum(d.values())
# for k, v in d.items():
#     nd[k] = v/s
# return d

# def hoge():
#     return 1, 2

# entries = [{'link': "http://hoge", 'title': "美術の世界"}, {'link': "http://fuga", 'title': "fuga"}]
# url_list = ["http://hoge", "http://nyan"]