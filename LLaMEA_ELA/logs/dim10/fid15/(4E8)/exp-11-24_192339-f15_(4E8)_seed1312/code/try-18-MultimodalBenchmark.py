import numpy as np

class MultimodalBenchmark:
    def __init__(self, dim):
        self.dim = dim
        
    def f(self, x):
        # Normalize input to [-1, 1] range for stability
        x_normalized = x / 5.0
        
        # Quadratic term for global basin attraction
        quadratic_term = np.sum(x_normalized**2)
        
        # Multiple sinusoidal modulations with varying frequencies and amplitudes
        freq1 = 3 * np.pi
        freq2 = 7 * np.pi
        sinusoidal_term = np.sum(np.sin(freq1 * x_normalized)**2 + 0.5 * np.sin(freq2 * x_normalized)**2)
        
        # Add Gaussian-like peaks to increase local minima density
        gaussian_peaks = np.sum(np.exp(-5 * x_normalized**2) * np.cos(2 * np.pi * x_normalized))
        
        # Include a quartic polynomial term for additional curvature
        quartic_term = np.sum(x_normalized**4)
        
        # Combine all terms with strategic weights to create a challenging landscape
        return 0.8 * quadratic_term + 0.3 * sinusoidal_term + 0.1 * gaussian_peaks + 0.2 * quartic_term