import logging
from pathlib import Path
def logger_init():
    current_dir = Path(__file__).resolve().parent
    project_root = current_dir.parent.parent
    log_dir = project_root / "logs"
    log_file = log_dir / "app.log"
    logging.basicConfig(filename=log_file,level=logging.INFO, filemode= 'w',
                        format='%(asctime)s - %(name)s - %(levelname)s - %(message)s',encoding='utf-8')
    logging.info("Logger initialized successfully.")

def logger_info_get_moveto(path:str):
    return logging.info("You went to "+path+"!")
