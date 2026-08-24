import numpy as np

class ChaoticOptimizationLandscape:
    def __init__(self, dim):
        self.dim = dim
        # Precompute constants for chaotic behavior
        self.constants = np.random.uniform(0.5, 2.0, dim)
        
    def f(self, x):
        # Ensure x is within bounds
        x = np.clip(x, -5.0, 5.0)
        
        # Base quadratic and polynomial terms
        result = np.sum((x - 1.0)**2) + 0.1 * np.sum(x**4) + 0.01 * np.sum(x**6)
        
        # Chaotic interaction terms using sinusoidal coupling
        for i in range(self.dim):
            for j in range(i+1, self.dim):
                coupling = np.sin(self.constants[i] * x[i]) * np.cos(self.constants[j] * x[j])
                result += 0.5 * coupling * (x[i] - x[j])**2
        
        # Add a dynamic global minimum that shifts with problem dimensions
        shift = np.sin(np.linspace(0, np.pi, self.dim)) * 0.5
        result += 0.3 * np.sum((x - shift)**2)
        
        # Incorporate a chaotic sinusoidal component with varying frequencies
        chaotic_term = 0.0
        for i in range(self.dim):
            freq = 2.0 + 3.0 * np.sin(i * 0.7)
            chaotic_term += np.sin(freq * x[i]) * np.cos(freq * x[i])
        result += 0.2 * chaotic_term
        
        # Add a high-frequency noise-like component for ruggedness
        ruggedness = 0.0
        for i in range(self.dim):
            ruggedness += np.sin(15.0 * x[i]) * np.cos(12.0 * x[i])
        result += 0.05 * ruggedness
        
        # Add a complex multimodal structure using multiple trigonometric combinations
        multimodal = 0.0
        for i in range(self.dim):
            multimodal += np.sin(2.0 * x[i]) * np.cos(3.0 * x[i]) + 0.5 * np.sin(4.0 * x[i])
        result += 0.1 * multimodal
        
        return result