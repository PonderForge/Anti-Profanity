import fasttext

print("Training...")
model = fasttext.train_supervised('processed-train.txt',
                                      ws=1, wordNgrams=2, minn=2, maxn=10, lr=0.5, epoch=25, loss='hs')
print("Quantizing...")
model.quantize()
print("Saving...")
model.save_model('profanity-detector.ftz')

def print_results(N, p, r):
    print("Number of test examples: \t" + str(N))
    print("Precision: \t{}".format(p))
    print("Recall: \t{}".format(r))
print("Testing...")
print_results(*model.test('test.txt'))