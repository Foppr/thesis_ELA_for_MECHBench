import numpy as np

class MultimodalGaussianSineBenchmark:
    def __init__(self, dim):
        self.dim = dim
        # Precompute peak positions and weights for each dimension
        self.peaks = np.random.uniform(-5.0, 5.0, (10, dim))
        self.weights = np.random.exponential(1.0, 10)
        self.weights /= np.sum(self.weights)  # Normalize weights
        
    def f(self, x):
        # Scale input to [-5, 5]
        x = np.clip(x, -5.0, 5.0)
        
        # Gaussian peak component with varying widths and heights
        gaussian = 0.0
        for i in range(10):
            peak = self.peaks[i]
            weight = self.weights[i]
            # Exponentially decaying width based on peak index
            sigma = 1.0 / (1.0 + 0.2 * i)
            # Multidimensional Gaussian
            diff = x - peak
            gaussian += weight * np.exp(-0.5 * np.sum((diff / sigma)**2))
        
        # Sinusoidal modulation to create additional ruggedness
        sine_mod = 0.0
        for i in range(self.dim):
            # Combine multiple sine frequencies with varying amplitudes
            sine_mod += (0.5 * np.sin(2.0 * x[i]) + 
                        0.3 * np.sin(5.0 * x[i]) + 
                        0.2 * np.sin(8.0 * x[i]) + 
                        0.1 * np.sin(12.0 * x[i]))
        
        # Combine components with different scaling factors
        return gaussian + 0.3 * sine_mod