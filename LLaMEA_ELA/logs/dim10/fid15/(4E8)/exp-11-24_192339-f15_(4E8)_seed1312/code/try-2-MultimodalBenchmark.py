import numpy as np

class MultimodalBenchmark:
    def __init__(self, dim):
        self.dim = dim
        
    def f(self, x):
        # Normalize input to [-1, 1] range
        x_norm = x / 5.0
        
        # Sum of sinusoidal terms with different frequencies
        sin_term = np.sum(np.sin(2 * np.pi * x_norm) + 0.5 * np.sin(4 * np.pi * x_norm))
        
        # Sum of Gaussian peaks with different positions and heights
        gaussian_peaks = 0
        peak_positions = np.linspace(-1, 1, 5)
        peak_heights = np.array([1.0, 0.8, 1.2, 0.6, 1.0])
        
        for i, (pos, height) in enumerate(zip(peak_positions, peak_heights)):
            gaussian_peaks += height * np.exp(-50 * (x_norm - pos)**2)
            
        # Combine terms with different weights
        result = 0.3 * sin_term + 0.7 * gaussian_peaks
        
        # Add a quadratic term to make the function bowl-shaped
        quadratic_term = 0.1 * np.sum(x_norm**2)
        
        return result + quadratic_term