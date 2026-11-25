import numpy as np

class MultimodalBenchmark:
    def __init__(self, dim):
        self.dim = dim
        
    def f(self, x):
        # Normalize input to [-1, 1] range for better conditioning
        x_norm = x / 5.0
        
        # Quadratic base term with varying coefficients
        f1 = np.sum((0.5 + 0.5 * np.sin(np.arange(1, self.dim + 1))) * x_norm**2)
        
        # Chaotic sine interactions with non-linear frequency modulation
        frequencies = 5 * (1 + np.sin(np.arange(1, self.dim + 1) * np.pi / 4))
        f2 = np.sum(np.sin(frequencies * x_norm)**3)
        
        # Radial polynomial term creating concentric valleys
        radial = np.sum(x_norm**2)
        f3 = 0.5 * radial**2.5 + 0.3 * radial**3
        
        # Cross-dimensional coupling with exponential interactions
        f4 = np.sum(np.exp(-np.abs(x_norm)) * np.sin(3 * np.pi * x_norm))
        
        # Additional chaotic noise component
        noise = 0.1 * np.random.random()
        
        # Combine all terms with varying weights
        return 0.8 * f1 + 1.2 * f2 + 0.6 * f3 + 0.4 * f4 + noise