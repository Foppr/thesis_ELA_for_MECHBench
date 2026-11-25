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
        f2 = np.sum(np.exp(-0.3 * np.abs(x_scaled)) * np.sin(3 * np.pi * x_scaled))
        
        # Cross-terms with cosine interaction creating additional complexity
        f3 = np.sum(np.cos(x_scaled[:-1] * x_scaled[1:]) * 0.5)
        
        # Additional high-frequency oscillations
        f4 = np.sum(np.sin(10 * x_scaled) * np.cos(7 * x_scaled))
        
        # Modified Gaussian term for enhanced conditioning
        f5 = np.sum(np.exp(-0.2 * x_scaled**2))
        
        # New radial barrier term to increase conditioning
        f6 = np.sum(1.0 / (1.0 + np.exp(5.0 * (np.sum(x_scaled**2) - 1.0))))
        
        # Chaotic exponential decay with sinusoidal coupling
        f7 = np.sum(np.exp(-0.4 * np.abs(x_scaled)) * np.sin(5 * np.pi * x_scaled))
        
        # Combined function with varying curvature and multiple local minima
        return 2.0 * f1 + 0.7 * f2 + 0.5 * f3 + 0.2 * f4 + 0.25 * f5 + 0.3 * f6 + 0.4 * f7