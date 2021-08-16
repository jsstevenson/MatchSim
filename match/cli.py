"""
Command-line interface for running match experiments.

TODO
 * supplement given config file w/ defaults
"""
import click
from match.match import Match
from match.generate_features import generate_applicant_ranks, generate_program_ranks, \
        generate_program_slots
from pathlib import Path
import json


DEFAULTS = {
    'num_applicants': 800,
    'num_programs': 100,
    'expected_num_slots': 7,
}


class CLI():

    @staticmethod
    @click.command()
    @click.option('-c', '--config', help='Path to config JSON')
    def create_experiment(config: str):
        """
        :param str config: path to JSON config file
        """
        if '--config' in click.get_os_args() or '-c' in click.get_os_args():
            config_path = Path(config)
            if not config_path.exists():
                raise FileNotFoundError('Invalid config file path')

            with open(config_path, 'r') as f:
                configs = json.load(f)
        else:
            configs = DEFAULTS

        num_applicants = configs['num_applicants']
        num_programs = configs['num_programs']

        applicant_ranks = generate_applicant_ranks(num_applicants, num_programs)
        program_ranks = generate_program_ranks(num_applicants, num_programs)
        program_slots = generate_program_slots(num_programs)

        match_experiment = Match(applicant_ranks, program_ranks, program_slots)
        applicant_matches, program_matches = match_experiment.perform_match()
