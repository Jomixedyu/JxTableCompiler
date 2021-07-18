

class ConfigAbstact:
    def __init__(self, is_combine) -> None:
        self.configs = []
        self.is_combine = is_combine

    def add(self, type: str, out_path: str):
        self.configs.append((type, out_path))


class ModelConfig:

    generator_names: list[str]

    def __init__(self, outdir: str, out_filename: str = None) -> None:
        self.outdir = outdir
        self.out_filename = out_filename
        self.is_combine = out_filename != None
        self.generator_names = []

    def add(self, generator_name: str):
        self.generator_names.append(generator_name)


class CompilerConfig(ConfigAbstact):

    def __init__(self, outdir: str) -> None:
        self.outdir = outdir
        self.names = []

    def add(self, name: str):
        self.names.append(name)
