import logging
import os

class LogGen:
    
    @staticmethod
    def loggen():
        # 1. Define the path (Use os.path.join for safety)
        log_path = os.path.join(os.path.abspath(os.curdir), "logs", "automation.log")
        
        # 2. Create the directory if it does not exist (Prevents FileNotFoundError)
        os.makedirs(os.path.dirname(log_path), exist_ok=True)

        # 3. Configure Logging
        # 'force=True' is important when using Pytest, as Pytest has its own logging defaults
        logging.basicConfig(
            filename=log_path,
            format='%(asctime)s: %(levelname)s: %(message)s',
            datefmt='%m/%d/%Y %I:%M:%S %p',
            force=True 
        )
        
        # 4. Create and return the logger object
        logger = logging.getLogger()
        # warn>Debug>info>error>fatal
        logger.setLevel(logging.INFO) # Set to INFO or DEBUG based on your need
        return logger