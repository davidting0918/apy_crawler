import pandas
import argparse


def run_crawl_pipeline(protocol):
    pass


if __name__ == '__main__':
    parser = argparse.ArgumentParser()
    parser.add_argument("--protocol")
    
    args = parser.parse_args()
    
    protocol_list = args.protocol.split(",")
    for protocol in protocol_list:
        run_crawl_pipeline(protocol=protocol)