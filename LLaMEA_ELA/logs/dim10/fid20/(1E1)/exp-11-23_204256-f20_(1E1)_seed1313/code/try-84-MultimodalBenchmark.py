import numpy as np

class MultimodalBenchmark:
    def __init__(self, dim):
        self.dim = dim
        
    def f(self, x):
        # Normalize input to [-1, 1] range for stability
        x_normalized = x / 5.0
        
        # Base quadratic term
        f1 = np.sum(x_normalized**2)
        
        # Enhanced sinusoidal perturbations with exponentially increasing frequencies
        freqs = np.arange(1, self.dim + 1)
        f2 = 0.5 * np.sum(np.sin(2**(freqs) * np.pi * x_normalized) ** 2)
        f3 = 0.3 * np.sum(np.sin(3**(freqs) * np.pi * x_normalized) ** 2)
        
        # Added higher-order polynomial terms with varying exponents
        f4 = 0.1 * np.sum(x_normalized**4)
        f5 = 0.06 * np.sum(x_normalized**6)
        f6 = 0.03 * np.sum(np.abs(x_normalized)**7)
        
        # Additional trigonometric terms with different phase and amplitude
        f7 = 0.2 * np.sum(np.cos(5 * np.pi * x_normalized) ** 2)
        f8 = 0.15 * np.sum(np.sin(7 * np.pi * x_normalized) ** 3)
        
        # Complex cross-terms with exponential interaction weights
        cross_terms = 0
        for i in range(self.dim - 2):
            weight = np.exp(-0.1 * i)
            cross_terms += weight * (x_normalized[i]**3 * x_normalized[i+1] * x_normalized[i+2]**2)
        f9 = 0.1 * cross_terms
        
        # Dynamic conditioning factor that increases with dimensionality and decreases near optimum
        distance_to_origin = np.linalg.norm(x_normalized)
        adaptive_scale = 1.0 + 0.5 * np.exp(0.1 * self.dim) * (1.0 / (1.0 + distance_to_origin**2))
        
        # Add a global minimum perturbation term
        f10 = 0.05 * np.sum((x_normalized - 0.1)**2)
        
        return adaptive_scale * (f1 + f2 + f3 + f4 + f5 + f6 + f7 + f8 + f9 + f10)