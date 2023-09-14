import torch
from torch import nn
from torch.nn import functional as F


class AdaptiveFilter(nn.Module):
    def __init__(self, weigths_init, size):
        super(AdaptiveFilter, self).__init__()
        
        # Calculate the size of the smoothing filter
        self.size = size * 4 + 1
        
        # Number of repetitions
        rep = 1
        
        # Convert the initial weights to a tensor and reshape it
        weights_init_torch = torch.tensor(weigths_init).view(1, 1, -1).float().repeat(rep, 1, 1)
        
        # Define the first filter and initialize with provided weights
        self.smooth_filtKH = torch.nn.Conv1d(in_channels=1, out_channels=rep, kernel_size=size, padding='same')
        self.smooth_filtKH.weight = torch.nn.Parameter(weights_init_torch)
        
        # Define the activation function - Parametric ReLU in this case
        self.prelu1 = torch.nn.PReLU()
        
        # Define the moving average and initialize it with uniform weights
        self.smooth_filt1 = torch.nn.Conv1d(in_channels=rep, out_channels=1, kernel_size=self.size, padding='same')
        self.smooth_filt1.weight = torch.nn.Parameter(torch.ones_like(self.smooth_filt1.weight) * 1/self.size * rep)
        
        # Disable training for the weights of the moving average
        self.smooth_filt1.weight.requires_grad = False

    def forward(self, x):
        # Compute the 95th and 5th percentiles for normalization
        myMax = torch.quantile(x, 0.95)
        myMin = torch.quantile(x, 0.05)
        
        # Normalize the input tensor
        x_norm = (x - myMin) / (myMax - myMin)
        
        # Apply the first filter
        smoothed_x = self.smooth_filtKH(F.pad(x_norm.view(1, 1, -1), (0, 0)))
        
        # Apply the activation function
        smoothed_x_energ = self.prelu1(smoothed_x)
        
        # Apply the moving average
        smoothed_x_energ_smooth = self.smooth_filt1(F.pad(smoothed_x_energ, (0, 0))).view(-1, 1)
        
        return smoothed_x_energ_smooth
