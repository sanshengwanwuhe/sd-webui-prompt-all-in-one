from scripts.physton_prompt.translator.base_tanslator import BaseTranslator
import os


class TranslatorsTranslator(BaseTranslator):
    translator = None

    def set_translator(self, translator):
        self.translator = translator
        return self

    def translate(self, text):
        region = self.api_config.get('region', 'CN')
        os.environ['translators_default_region'] = region
        from scripts.physton_prompt.translators.server import translate_text, tss, AlibabaV1
        tss.server_region = region
        tss._bing.server_region = region
        tss._google.server_region = region

        return translate_text(text, from_language=self.from_lang, to_language=self.to_lang, translator=self.translator, timeout=30)
