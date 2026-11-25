import numpy as np

class ExponentialGaussianBenchmark:
    def __init__(self, dim):
        self.dim = dim
        # Generate multiple Gaussian peaks with random positions and widths
        self.peaks = np.random.uniform(-4.0, 4.0, (15, dim))
        self.widths = np.random.uniform(0.5, 2.0, 15)
        self.peak_heights = np.random.uniform(1.0, 5.0, 15)
        # Adaptive conditioning matrix
        self.conditioning = np.diag(np.random.uniform(0.1, 10.0, dim))
        # Trigonometric perturbation frequencies
        self.freqs = np.random.uniform(0.5, 3.0, dim)
        
    def f(self, x):
        # Ensure x is within bounds [-5, 5]
        x = np.clip(x, -5.0, 5.0)
        
        # Apply conditioning
        x_cond = self.conditioning @ x
        
        # Compute sum of exponentially decaying Gaussian peaks
        result = 0.0
        for i in range(15):
            peak_term = 0.0
            for j in range(self.dim):
                diff = x_cond[j] - self.peaks[i, j]
                peak_term += diff**2
            gaussian_val = np.exp(-0.5 * peak_term / (self.widths[i]**2))
            result += self.peak_heights[i] * gaussian_val
        
        # Add trigonometric perturbations
        trig_perturbation = 0.0
        for i in range(self.dim):
            trig_perturbation += np.sin(self.freqs[i] * x[i]) * np.cos(self.freqs[i] * x[i])
        
        # Combine components with different weights
        final_result = result + 0.3 * trig_perturbation
        
        return final_result