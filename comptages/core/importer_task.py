import os

from datetime import datetime

from qgis.core import QgsTask, Qgis, QgsMessageLog

from comptages.datamodel import models
from comptages.core import importer


class ImporterTask(QgsTask):

    def __init__(self, file_path, count):
        self.basename = os.path.basename(file_path)
        super().__init__(
            'Importation fichier {}'.format(self.basename))

        self.file_path = file_path
        self.count = count

    def run(self):
        print("in run")
        try:
            importer.import_file(self.file_path, self.count, callback_progress=self.setProgress)
            return True
        except Exception as e:
            raise e
            self.exception = e
            return False

    def finished(self, result):
        if result:
            QgsMessageLog.logMessage(
                '{} - Import file {} ended'.format(
                    datetime.now(), self.basename),
                'Comptages', Qgis.Info)

        else:
            QgsMessageLog.logMessage(
                '{} - Import file {} ended with errors: {}'.format(
                    datetime.now(), self.basename, self.exception),
                'Comptages', Qgis.Info)

    def cancel(self):
        # TODO: Cancel needed?
        pass