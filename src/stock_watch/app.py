import multiprocessing
import logging
import src.stock_watch as stock_watch
from . import helpers
from . import docker
from . import data_scraper
from src.stock_watch.gui.gui import GUI

class StockWatch:

    def __init__(self):
        self.gui = None
        self._message_bus = None

        self.docker_manager = None
        self.scraper_manager = None
        self.main_window = None

    def run(self):
        logging.info('Starting StockWatch')
        self._message_bus = stock_watch.message_bus.get_instance()

        self.initiate_docker_containers()
        self.initiate_data_scrapers()
        self.initiate_gui()

        # By now all initiate functions should have added any connections to message bus
        # Start the message bus
        self._message_bus.start()

    def initiate_docker_containers(self):
        # Docker commands
        database_commands = []

        # Database down command
        docker_directory = helpers.find_file('docker-compose-database.yml', './')
        database_commands.append(
            docker.models.DockerComposeCommand(
            command=docker.models.DockerComposeCommandOption.DOWN,
            files=[docker_directory]
        ))

        # Database up command
        docker_directory = helpers.find_file('docker-compose-database.yml', './')
        database_commands.append(
            docker.models.DockerComposeCommand(
            command=docker.models.DockerComposeCommandOption.UP,
            files=[docker_directory],
            child_options={'--build': None, '--force-recreate': None, '--detach': None}
        ))

        # Docker containers command sequence
        database_command_sequence = docker.models.CommandSequence(database_commands)

        # Docker container to pass to docker_manager
        database_container = docker.DockerContainer(database_command_sequence)

        # Docker container manager to manage the docker containers
        self.docker_manager = docker.ContainerManager([database_container])
        self.docker_manager.start_containers()

    def initiate_data_scrapers(self):
        self.scraper_manager = data_scraper.ScraperManager()

        # Create scrapers
        reddit_scraper = data_scraper.scrapers.reddit_scraper.RedditScraper()
        self.scraper_manager.add_scraper(scraper=reddit_scraper)

        # Setup pipe connection between main process and data scraper
        scraper_parent_conn, child_conn = multiprocessing.Pipe(duplex=True)
        self._message_bus.add_connection(connection=scraper_parent_conn)

        # Start data scraper process
        data_scraper_process = multiprocessing.Process(target=self.scraper_manager.start_scrapers,
                                                       args=(child_conn,))
        data_scraper_process.start()

    def initiate_gui(self):
        self.gui = GUI()
        gui_process = multiprocessing.Process(target=self.gui.show)
        gui_process.start()