from ovos_plugin_manager.templates.language import LanguageDetector
from lingua import Language, LanguageDetectorBuilder


class LinguaPyDetector(LanguageDetector):
    def __init__(self):
        super(LinguaPyDetector, self).__init__()
        # TODO from config
        # loading all supported languages would take 3GB of memory...
        languages = [Language.ENGLISH, Language.FRENCH, Language.UKRAINIAN, Language.RUSSIAN,
                     Language.GERMAN, Language.SPANISH, Language.PORTUGUESE, Language.ITALIAN]
        self.detector = LanguageDetectorBuilder.from_languages(*languages).build()

    def detect(self, text):
        return self.detector.detect_language_of(text).iso_code_639_1.name.lower()

    def detect_probs(self, text):
        confidence_values = self.detector.compute_language_confidence_values(text)
        return {k.iso_code_639_1.name.lower(): v for k, v in confidence_values}

