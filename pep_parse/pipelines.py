from collections import defaultdict
import csv
import datetime as dt

from pep_parse.settings import RESULTS_DIR, DATETIME_FORMAT


class PepParsePipeline:

    def open_spider(self, spider):
        self.results = defaultdict(int)

    def process_item(self, item, spider):
        self.results[item['status']] += 1
        return item

    def close_spider(self, spider):
        RESULTS_DIR.mkdir(exist_ok=True)
        now = dt.datetime.now()
        now_formatted = now.strftime(DATETIME_FORMAT)
        file_name = f'status_summary_{now_formatted}.csv'
        file_path = RESULTS_DIR / file_name
        with open(file_path, 'w', encoding='utf-8') as f:
            writer = csv.writer(f, dialect='unix')
            writer.writerows(
                [
                    ('Статус', 'Количество'),
                    *self.results.items(),
                    ('Всего', sum(self.results.values())),
                ]
            )
