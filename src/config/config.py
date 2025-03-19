import yaml


class Config:
    def __init__(self):
        self.input = None
        with open('src/config/data.yml', 'r') as data_file:
            self.input = yaml.safe_load(data_file)

        self.input_file_path = self.input['data']['input_file']

        self.node_count = self.input['data']['input_file_details']['node_count']
        self.source_id_raw = self.input['data']['input_file_details']['source_id']
        self.sink_id_raw = self.input['data']['input_file_details']['sink_id']

        self.source_id = self.node_count - 2
        self.sink_id = self.node_count - 1

        self.output_folder = self.input['data']['output_folder']