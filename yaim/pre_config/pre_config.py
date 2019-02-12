import argparse
import yaml
from models.config_file import ConfigFile
from categories import wn_info_static, wn_info_queried
def parse_args():
    parser = argparse.ArgumentParser()
    parser.add_argument('--site_config', help="Compiled Site Level Configuration YAML file")
    parser.add_argument('--execution_id', help="Execution ID of Lightweight Component")
    parser.add_argument('--output_dir', help="Output directory")
    args = parser.parse_args()
    return {
        'augmented_site_level_config_file': args.site_config,
        'execution_id': args.execution_id,
        'output_dir': args.output_dir
    }


def get_wn_info_file_categories(data, execution_id):
    categories = []
    static = wn_info_static.get(data)
    queried = wn_info_queried.get(data, execution_id)
    categories.append(static)
    categories.append(queried)
    return static + queried


if __name__ == "__main__":
    args = parse_args()
    execution_id = args['execution_id']
    augmented_site_level_config_file = args['augmented_site_level_config_file']
    output_dir = args['output_dir']

    site_config_filename = args['augmented_site_level_config_file']
    site_config = open(site_config_filename, 'r')
    data = yaml.load(site_config)
    wn_info_file = ConfigFile(output_dir + '/wn-info.def', data)

    wn_info_file.add_categories(get_wn_info_file_categories(data, execution_id))

    wn_info_file.generate_output_file()