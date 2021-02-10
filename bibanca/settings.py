BOT_NAME = 'bibanca'

SPIDER_MODULES = ['bibanca.spiders']
NEWSPIDER_MODULE = 'bibanca.spiders'
FEED_EXPORT_ENCODING = 'utf-8'
LOG_LEVEL = 'ERROR'
DOWNLOAD_DELAY = 0

ROBOTSTXT_OBEY = True

ITEM_PIPELINES = {
	'bibanca.pipelines.BibancaPipeline': 100,

}