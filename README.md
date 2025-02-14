Exploring the application of fine-tuned mt5-base model for Polish to Japanese translation

Dataset used: [Tatoeba](https://opus.nlpl.eu/Tatoeba/corpus/version/Tatoeba)

Included in the repository is also a script used for filtering badly-aligned examples from the [Opensubtitles](https://opus.nlpl.eu/OpenSubtitles/en&ja/v2018/OpenSubtitles) (http://www.opensubtitles.org/) and [TED2020](https://opus.nlpl.eu/TED2020/pl&ja/v1/TED2020) datasets using the [wmt22-cometkiwi-da](https://huggingface.co/Unbabel/wmt22-cometkiwi-da) COMET quality estimation model.

The aforementioned filtered datasets ended up not being used here due to issues with unstable [curriculum learning](https://en.wikipedia.org/wiki/Curriculum_learning) when transitioning the model from learning on Tatoeba to the other datasets.

References:

* J. Tiedemann, 2012, [Parallel Data, Tools and Interfaces in OPUS](http://www.lrec-conf.org/proceedings/lrec2012/pdf/463_Paper.pdf). In Proceedings of the 8th International Conference on Language Resources and Evaluation (LREC 2012)
* P. Lison and J. Tiedemann, 2016, OpenSubtitles2016: [Extracting Large Parallel Corpora from Movie and TV Subtitles](http://www.lrec-conf.org/proceedings/lrec2016/pdf/947_Paper.pdf). In Proceedings of the 10th International Conference on Language Resources and Evaluation (LREC 2016)
* J. Tiedemann, 2016, [Finding Alternative Translations in a Large Corpus of Movie Subtitles](http://www.lrec-conf.org/proceedings/lrec2016/pdf/62_Paper.pdf). In Proceedings of the 10th International Conference on Language Resources and Evaluation (LREC 2016)
* Reimers, Nils and Gurevych, Iryna: [Making Monolingual Sentence Embeddings Multilingual using Knowledge Distillation](https://arxiv.org/abs/2004.09813)

Many thanks to [OPUS](https://opus.nlpl.eu/) for hosting the relevant NLP datasets and [Opensubtitles](https://www.opensubtitles.org/en/search/subs) for sharing their dataset
