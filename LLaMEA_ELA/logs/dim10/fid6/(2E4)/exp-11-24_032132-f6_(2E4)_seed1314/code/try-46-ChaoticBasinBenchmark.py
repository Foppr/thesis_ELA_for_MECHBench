import numpy as np

class ChaoticBasinBenchmark:
    def __init__(self, dim):
        self.dim = dim
        # Precompute constants for chaotic behavior
        self.coefficients = np.random.uniform(0.5, 2.0, dim)
        self.frequencies = np.random.uniform(1.0, 5.0, dim)
        
    def f(self, x):
        if len(x) != self.dim:
            raise ValueError("Input dimension mismatch")
        
        # Radial basin component
        radial_term = np.sum(x**2) * 0.1
        
        # Sinusoidal oscillations with varying frequencies and amplitudes
        sin_term = 0.0
        for i in range(self.dim):
            sin_term += self.coefficients[i] * np.sin(self.frequencies[i] * x[i]) * np.cos(self.frequencies[i] * x[i])
        
        # Chaotic component using logistic map-like behavior
        chaotic_term = 0.0
        for i in range(self.dim):
            xi = x[i] / 5.0  # Normalize to [-1, 1]
            chaotic_term += np.sin(10 * np.pi * xi) * np.cos(10 * np.pi * xi)
        
        # Combine all terms with a nonlinear transformation
        result = radial_term + 0.5 * sin_term + 0.3 * chaotic_term
        
        # Add a small noise component to make it more challenging
        noise = 0.01 * np.sum(np.sin(x) * np.cos(x))
        
        return result + noise