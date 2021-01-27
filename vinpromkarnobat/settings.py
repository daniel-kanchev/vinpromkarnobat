BOT_NAME = 'vinpromkarnobat'
SPIDER_MODULES = ['vinpromkarnobat.spiders']
NEWSPIDER_MODULE = 'vinpromkarnobat.spiders'
ROBOTSTXT_OBEY = True
LOG_LEVEL = 'WARNING'
ITEM_PIPELINES = {
   'vinpromkarnobat.pipelines.DatabasePipeline': 300,
}
