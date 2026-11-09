import importlib
import shutil
import sys
print(f"Python: {sys.version.split()[0]}")
print(f"Executable: {sys.executable}")
for package in ("torch","pyannote.audio","pyannote.metrics","soundfile","dotenv"):
    try:
        module=importlib.import_module(package)
        version=getattr(module,"__version__","version not exposed")
        print(f"[Ok] {package}: {version}")
    except Exception as exc:
        print(f"[Fail] {package}: {type(exc).__name__}: {exc}")
try:
    import torch
    print(f"Pytorch CUDA available: {torch.cuda.is_available()}")
    if torch.cuda.is_available():
        print(f"CUDA device: {torch.cuda.get_device_name(0)}")
    else:
        print("Using CPU for inference.")
except Exception:
    pass
ffmpeg=shutil.which('ffmpeg')
print(f"Ffmpeg: {ffmpeg if ffmpeg else 'Not Found'}")