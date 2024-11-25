from pathlib import Path


BOT_NAME = 'pep_parse'
NEWSPIDER_MODULE = BOT_NAME + '.spiders'
SPIDER_MODULES = [NEWSPIDER_MODULE]
ROBOTSTXT_OBEY = True
BASE_DIR = Path(__file__).parent.parent
RESULTS_DIR_NAME = 'results'
RESULTS_DIR = BASE_DIR / RESULTS_DIR_NAME
DATETIME_FORMAT = '%Y-%m-%d_%H-%M-%S'

FEEDS = {
    RESULTS_DIR_NAME + '/pep_%(time)s.csv': {
        'format': 'csv',
        'fields': ['number', 'name', 'status'],
        'overwrite': True
    },
}

ITEM_PIPELINES = {
    'pep_parse.pipelines.PepParsePipeline': 300,
}
