import numpy as np

class MultimodalBenchmark:
    def __init__(self, dim):
        self.dim = dim
    
    def f(self, x):
        # Shifted multimodal function with global minimum at origin
        if len(x) != self.dim:
            raise ValueError("Input dimension mismatch")
        
        # Normalize input to [-1, 1] for stability
        x_norm = x / 5.0
        
        # Sum of sinusoidal terms with different frequencies and amplitudes
        f_val = 0.0
        for i in range(self.dim):
            frequency = 2 ** (i % 4)  # Varying frequencies
            amplitude = 1.0 / (1.0 + i * 0.1)  # Decaying amplitudes
            f_val += amplitude * (x_norm[i]**2 - 10 * np.cos(2 * np.pi * frequency * x_norm[i]) + 10)
        
        # Add a quadratic term to ensure global minimum is at origin
        f_val += np.sum(x_norm**2) / 100
        
        return f_val