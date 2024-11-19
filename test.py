import torch
import torchvision
import torchaudio
import torchtext

print(f"torch version: {torch.__version__}")
print(f"torchvision version: {torchvision.__version__}")
print(f"torchaudio version: {torchaudio.__version__}")
print(f"torchtext version: {torchtext.__version__}")

print(f"CUDA version: {torch.version.cuda}")


import torch
print(torch.backends.cudnn.version())
