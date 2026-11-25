import numpy as np

class ChaoticPolynomialBenchmark:
    def __init__(self, dim):
        self.dim = dim
        
    def f(self, x):
        # Ensure x is within bounds [-5, 5]
        x = np.clip(x, -5.0, 5.0)
        
        # Base quadratic component
        quadratic = np.sum(x**2)
        
        # Chaotic sine-wave interactions with varying frequencies
        chaotic = 0
        for i in range(self.dim):
            freq = 2 * (i + 1)  # Increasing frequency
            chaotic += np.sin(freq * x[i]) * np.cos(freq * x[i] * 0.5) * np.exp(-0.1 * x[i]**2)
        
        # Polynomial coupling with mixed degrees
        poly_coupling = 0
        for i in range(self.dim):
            for j in range(i+1, min(i+4, self.dim)):  # Limited coupling
                poly_coupling += (x[i]**3 + x[j]**3) * np.sin(0.2 * x[i] * x[j]) * (i + j + 1)
        
        # Adaptive noise component that scales with dimensionality
        noise = 0
        for i in range(self.dim):
            noise += np.sin(x[i] * np.pi * (i + 1)) * np.cos(x[i] * np.pi * (i + 1) * 0.7)
        
        # High-order polynomial with mixed signs for increased complexity
        high_order = 0
        for i in range(self.dim):
            high_order += x[i]**5 - 10 * x[i]**3 + 5 * x[i]
        
        # Cross-term interactions with exponential decay
        cross_terms = 0
        for i in range(self.dim):
            for j in range(i+1, self.dim):
                cross_terms += np.exp(-0.05 * (x[i] - x[j])**2) * np.sin(3 * x[i] + 2 * x[j])
        
        # Asymmetric sigmoidal component
        sigmoidal = 0
        for i in range(self.dim):
            sigmoidal += 1 / (1 + np.exp(-x[i])) * np.sin(x[i]**2)
        
        # Combine all components with carefully tuned weights
        return (0.8 * quadratic + 
                0.6 * chaotic + 
                0.4 * poly_coupling + 
                0.3 * noise + 
                0.5 * high_order + 
                0.2 * cross_terms + 
                0.1 * sigmoidal + 
                15 * np.sum(np.sin(x)**6))