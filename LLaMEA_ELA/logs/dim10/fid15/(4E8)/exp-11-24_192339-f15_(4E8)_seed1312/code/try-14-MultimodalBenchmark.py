import numpy as np

class MultimodalBenchmark:
    def __init__(self, dim):
        self.dim = dim
        
    def f(self, x):
        # Normalize input to [-1, 1] range
        x_norm = x / 5.0
        
        # Multiple sinusoidal terms with different frequencies and phases
        sin_term = np.sum(np.sin(2 * np.pi * x_norm) + 
                         0.5 * np.sin(4 * np.pi * x_norm) + 
                         0.3 * np.sin(6 * np.pi * x_norm))
        
        # Multiple Gaussian peaks with varying positions, heights, and widths
        gaussian_peaks = 0
        peak_positions = np.linspace(-1, 1, 7)
        peak_heights = np.array([1.0, 0.8, 1.2, 0.6, 1.0, 0.9, 1.1])
        peak_widths = np.array([0.1, 0.2, 0.15, 0.25, 0.12, 0.18, 0.14])
        
        for i, (pos, height, width) in enumerate(zip(peak_positions, peak_heights, peak_widths)):
            gaussian_peaks += height * np.exp(-np.power(x_norm - pos, 2) / (2 * width**2))
            
        # Add a more complex harmonic term
        harmonic_term = np.sum(np.cos(3 * np.pi * x_norm) + 
                              0.4 * np.cos(5 * np.pi * x_norm))
        
        # Combine terms with different weights
        result = 0.2 * sin_term + 0.5 * gaussian_peaks + 0.3 * harmonic_term
        
        # Add a quartic term to increase the complexity of the landscape
        quartic_term = 0.05 * np.sum(x_norm**4)
        
        # Add a cross-term interaction between dimensions
        cross_term = 0.1 * np.sum(x_norm[:-1] * x_norm[1:])
        
        return result + quartic_term + cross_term