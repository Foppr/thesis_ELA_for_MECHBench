from pathlib import Path

SAVE_DIR = Path(__file__).parent / "saved_models"
# DATA_DIR = Path(__file__).parent.parent / "data_p{problem}"  

def get_save_path(filename: str) -> Path:
    SAVE_DIR.mkdir(parents=True, exist_ok=True)
    return SAVE_DIR / filename

def get_data_path(problem: int, size: int, dim: int, seed: int) -> Path:
    return (
        Path(__file__).parent.parent  # project root
        / f"data_p{problem}"
        / f"{size}D"
        / f"{size}d{dim}_p{problem}_seed{seed}.csv"
    )