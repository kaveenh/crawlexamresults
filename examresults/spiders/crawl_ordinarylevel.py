# Parallel running of the 4 ordinary level web crawler spiders

import os
from multiprocessing import Pool


processes = ('scrapy crawl ordinarylevel1', 'scrapy crawl ordinarylevel2',
             'scrapy crawl ordinarylevel3', 'scrapy crawl ordinarylevel4')


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
