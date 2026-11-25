import numpy as np

class MultimodalBenchmark:
    def __init__(self, dim):
        self.dim = dim
        
    def f(self, x):
        # Scale input to [-1, 1] range
        x_scaled = x / 5.0
        
        # Polynomial interaction terms with modified scaling
        f1 = np.sum(x_scaled**4) * 1.5
        
        # Sinusoidal modulations with altered exponential decay
        f2 = np.sum(np.exp(-0.7 * np.abs(x_scaled)) * np.sin(3 * np.pi * x_scaled))
        
        # Cross-terms with cosine interaction creating additional complexity
        f3 = np.sum(np.cos(x_scaled[:-1] * x_scaled[1:]) * 0.7)
        
        # Additional high-frequency oscillations
        f4 = np.sum(np.sin(12 * x_scaled) * np.cos(8 * x_scaled))
        
        # Modified Gaussian term for enhanced conditioning
        f5 = np.sum(np.exp(-0.4 * x_scaled**2))
        
        # Combined function with varying curvature and multiple local minima
        return 2.0 * f1 + 0.5 * f2 + 0.3 * f3 + 0.2 * f4 + 0.25 * f5