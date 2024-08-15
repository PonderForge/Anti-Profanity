import fasttext

# Load model and determine tone from words used
model = fasttext.load_model("profanity-detector.ftz")
print(model.predict("filthy"))