import numpy as np

class ChaoticBenchmark:
    def __init__(self, dim):
        self.dim = dim
        
    def f(self, x):
        # Scale input to [-1, 1] range
        x_scaled = x / 5.0
        
        # High-dimensional chaotic sine-wave with varying frequencies and amplitudes
        chaotic_wave = np.sum(np.sin(10 * np.pi * x_scaled + np.sin(7 * x_scaled)) * 
                             np.cos(5 * np.pi * x_scaled + np.cos(3 * x_scaled)))
        
        # Fractal-like polynomial distortion with recursive self-similarity
        fractal_poly = np.sum((x_scaled**2 + 0.1 * np.sin(20 * x_scaled))**3 - 
                             2 * (x_scaled**2 + 0.1 * np.sin(20 * x_scaled))**2 + 
                             0.5 * x_scaled**4)
        
        # Multi-scale trigonometric modulation with exponentially increasing frequencies
        multi_trig = np.sum(np.sin(2**np.arange(self.dim) * np.pi * x_scaled) * 
                           np.cos(3**np.arange(self.dim) * np.pi * x_scaled))
        
        # Enhanced exponential decay with non-uniform basis functions
        exp_decay = np.sum(np.exp(-x_scaled**2 / (1 + 0.5 * np.abs(x_scaled))) * 
                          np.sin(4 * x_scaled) * np.cos(6 * x_scaled))
        
        # Irregular gradient landscape with discontinuous second derivatives
        irregular_grad = np.sum(np.sin(15 * x_scaled) * np.exp(-0.1 * x_scaled**2) + 
                               0.3 * np.cos(25 * x_scaled) * np.log(1 + np.abs(x_scaled)))
        
        # Multi-modal Gaussian peaks with varying heights and widths
        gaussian_peaks = np.sum(0.5 * np.exp(-0.5 * (x_scaled - 0.3)**2 / 0.1**2) + 
                               0.3 * np.exp(-0.5 * (x_scaled + 0.4)**2 / 0.2**2) + 
                               0.2 * np.exp(-0.5 * x_scaled**2 / 0.15**2))
        
        # Combine all terms with non-linear weighting and global offset
        return 0.25 * chaotic_wave + 0.2 * fractal_poly + 0.15 * multi_trig + \
               0.15 * exp_decay + 0.1 * irregular_grad + 0.1 * gaussian_peaks + 2.0