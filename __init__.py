from Dart.sublime_plugin_lib import PluginLogger

from Dart.lib.editor_context import EditorContext

import logging


_logger = PluginLogger(__name__)
_logger.warn_aboug_logging_level()


editor_context = EditorContext()
