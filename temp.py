import numpy as np
import torch

x = torch.tensor([0, 1, 2, 3, 4])
torch.save(x, 'tensor.pt')
# # Save to io.BytesIO buffer
# buffer = io.BytesIO()
# torch.save(x, buffer)


