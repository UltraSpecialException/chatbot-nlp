import spacy
from spacy.pipeline import EntityRecognizer
from FirebaseSetUp import all_entities
import plac
import random
from pathlib import Path
import spacy
import sys
from spacy.util import minibatch, compounding


# uncomment to train relatively mediocre language :C
# train_data = []
#
# for sentence in all_entities:
#     key = list(all_entities[sentence].keys())[0]
#     info = all_entities[sentence][key]
#     indices = list(info.keys())[0].split(" ")
#     indices[0], indices[1] = int(indices[0]), int(indices[1])
#     start, stop = indices[0], indices[1]
#     entity_list = {"entities": [(start, stop, "KEYWORD")]}
#     data = (sentence, entity_list)
#     train_data.append(data)
#
#
# @plac.annotations(
#     model=("Model name. Defaults to blank 'en' model.", "option", "m", str),
#     output_dir=("Optional output directory", "option", "o", Path),
#     n_iter=("Number of training iterations", "option", "n", int),
# )
#
#
# def main(model=None, output_dir=None, n_iter=20):
#     """
#     Load the model, set up the pipeline and train the entity recognizer.
#     """
#     output_dir = "entity_recognizer"
#     if model is not None:
#         nlp = spacy.load(model)  # load existing spaCy model
#         print("Loaded model '%s'" % model)
#     else:
#         nlp = spacy.blank("en")  # create blank Language class
#         print("Created blank 'en' model")
#
#     # create the built-in pipeline components and add them to the pipeline
#     # nlp.create_pipe works for built-ins that are registered with spaCy
#     if "ner" not in nlp.pipe_names:
#         ner = nlp.create_pipe("ner")
#         nlp.add_pipe(ner, last=True)
#     # otherwise, get it so we can add labels
#     else:
#         ner = nlp.get_pipe("ner")
#
#     # add labels
#     for _, annotations in train_data:
#         for ent in annotations.get("entities"):
#             ner.add_label(ent[2])
#
#     # get names of other pipes to disable them during training
#     other_pipes = [pipe for pipe in nlp.pipe_names if pipe != "ner"]
#     with nlp.disable_pipes(*other_pipes):  # only train NER
#         # reset and initialize the weights randomly – but only if we're
#         # training a new model
#         if model is None:
#             nlp.begin_training()
#         for itn in range(n_iter):
#             random.shuffle(train_data)
#             losses = {}
#             # batch up the examples using spaCy's minibatch
#             batches = minibatch(train_data, size=compounding(4.0, 32.0, 1.001))
#             for batch in batches:
#                 texts, annotations = zip(*batch)
#                 nlp.update(
#                     texts,  # batch of texts
#                     annotations,  # batch of annotations
#                     drop=0.5,  # dropout - make it harder to memorise data
#                     losses=losses,
#                 )
#             print("Losses", losses)
#
#     # test the trained model
#     for text, _ in train_data:
#         doc = nlp(text)
#         print("Entities", [(ent.text, ent.label_) for ent in doc.ents])
#         # print("Tokens", [(t.text, t.ent_type_, t.ent_iob) for t in doc])
#
#     # save model to output directory
#     if output_dir is not None:
#         output_dir = Path(output_dir)
#         if not output_dir.exists():
#             output_dir.mkdir()
#         nlp.to_disk(output_dir)
#         print("Saved model to", output_dir)
#
#         # test the saved model
#         print("Loading from", output_dir)
#         nlp2 = spacy.load(output_dir)
#         for text, _ in train_data:
#             doc = nlp2(text)
#             print("Entities", [(ent.text, ent.label_) for ent in doc.ents])
#             print("Tokens", [(t.text, t.ent_type_, t.ent_iob) for t in doc])


# if __name__ == "__main__":
#     plac.call(main)

nlp = spacy.load("en_core_web_sm")
nlp2 = spacy.load("/Users/tonynguyen/Desktop/ML/chatbot-nlp/entity_recognizer")
sentence = sys.argv[1]

doc = nlp(sentence)
if len(doc.ents) == 0:
    doc = nlp2(sentence)

for ent in doc.ents:
    print(ent)