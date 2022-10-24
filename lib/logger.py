import logging
logging.basicConfig(format='\033[92m%(levelname)s\033[0m: %(message)s')

log = logging.getLogger()
log.setLevel(logging.INFO)
