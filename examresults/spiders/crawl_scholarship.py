# Parallel running of the 4 scholarship spiders

import os
from multiprocessing import Pool


processes = ('scrapy crawl scholarship1', 'scrapy crawl scholarship2',
             'scrapy crawl scholarship3', 'scrapy crawl scholarship4')


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
