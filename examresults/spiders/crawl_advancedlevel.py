# Parallel running of the 4 advanced level web crawler spiders


import os
from multiprocessing import Pool


processes = ('scrapy crawl advancedlevel1', 'scrapy crawl advancedlevel2',
             'scrapy crawl advancedlevel3', 'scrapy crawl advancedlevel4')


def run_process(process):
    try:
        while True:
            os.system(f'{process}')
    except KeyboardInterrupt:
        pass


if __name__ == '__main__':

    pool = Pool(processes=4)
    pool.map(run_process, processes)
    pool.close()
