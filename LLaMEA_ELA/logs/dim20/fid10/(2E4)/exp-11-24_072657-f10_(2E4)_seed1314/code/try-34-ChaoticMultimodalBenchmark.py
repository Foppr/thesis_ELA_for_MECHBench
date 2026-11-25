import numpy as np

class ChaoticMultimodalBenchmark:
    def __init__(self, dim):
        self.dim = dim
        # Precompute logistic map seeds for chaos generation
        self.logistic_seeds = np.random.uniform(0.1, 0.9, dim)
        
    def f(self, x):
        # Normalize input to [-1, 1]
        x_norm = x / 5.0
        
        # Logistic map chaotic component
        chaotic = 0.0
        for i in range(self.dim):
            seed = self.logistic_seeds[i]
            for _ in range(10):  # Iterate logistic map
                seed = 4.0 * seed * (1.0 - seed)
            chaotic += np.sin(seed * np.pi * x_norm[i])**2
        
        # Radial basis function component with varying widths
        rbf = 0.0
        centers = np.linspace(-1, 1, min(5, self.dim))
        for i in range(min(5, self.dim)):
            dist = np.sum((x_norm - centers[i])**2)
            rbf += np.exp(-dist * (i + 1)**2)
        
        # Multi-scale sinusoidal modulation
        modulated = 0.0
        frequencies = [1, 3, 7, 11, 19]
        for i, freq in enumerate(frequencies[:self.dim]):
            modulated += np.sin(freq * x_norm[i]) * np.cos(freq * x_norm[i]**2)
        
        # Cross-dimensional polynomial coupling
        coupling = 0.0
        for i in range(self.dim - 1):
            coupling += (x_norm[i]**3 + x_norm[i+1]**3) * (x_norm[i] - x_norm[i+1])**2
        
        # Asymmetric cubic terms
        cubic = np.sum(x_norm**3 * np.exp(-x_norm**2))
        
        # Combine all components with adaptive weights
        result = 0.6 * chaotic + 0.4 * rbf + 0.5 * modulated + 0.3 * coupling + 0.2 * cubic
        
        # Add small noise for robustness
        result += 0.001 * np.random.random()
        
        return result