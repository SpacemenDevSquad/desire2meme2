from pathlib import Path
from dotenv import dotenv_values
import secrets

def get_config() -> type:
    package_dir: Path = Path(__file__).parent.resolve()
    project_dir: Path = package_dir.parent.parent.resolve()
    
    db_file: Path = project_dir / "data.db"

    from desire4memes.extensions import Hasher
    from desire4memes.authentication import Hasher
    
    pep_file: Path = project_dir / "pepper.bin"

    with open(pep_file, 'rb') as fin:
        pepper_key = fin.read()

    hasher = Hasher(pepper_key)
    
    appenv_path: Path = project_dir / ".appenv"
    env: dict[str, str | None] = dotenv_values(appenv_path)
    
    # make sure there is an appropriate value for SECRET_KEY
    if 'SECRET_KEY' not in env or env["SECRET_KEY"] is None:
        env["SECRET_KEY"] = secrets.token_urlsafe(32)
    
    class Config:
        SECRET_KEY: str = env["SECRET_KEY"]
        SQLALCHEMY_DATABASE_URI: str = f"sqlite:///{db_file}"
    
    return Config