from pathlib import Path

from dotenv import dotenv_values

def get_config() -> type:
    # Calculate the path to the package and project root directories
    package_dir: Path = Path(__file__).parent.resolve()
    project_dir: Path = package_dir.parent.parent.resolve()

    # The .appenv file should be located in the project root
    appenv_path: Path = project_dir / '.appenv'
    env: dict[str, str | None] = dotenv_values(appenv_path)
    
    # make sure there is an appropriate value for SECRET_KEY
    if 'SECRET_KEY' not in env or env['SECRET_KEY'] is None:
        raise ValueError('Config in .appenv must include a SECRET_KEY!')
    
    class Config:
        SECRET_KEY: str = env['SECRET_KEY']
    
    return Config