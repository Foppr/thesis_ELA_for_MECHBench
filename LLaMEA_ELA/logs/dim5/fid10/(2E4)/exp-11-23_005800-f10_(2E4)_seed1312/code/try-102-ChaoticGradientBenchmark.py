import numpy as np

class ChaoticGradientBenchmark:
    def __init__(self, dim):
        self.dim = dim
        self.c1 = 0.5
        self.c2 = 2.0
        self.c3 = 0.1
        self.lambda_ = 3.8
        self.beta = 1.5
        
    def f(self, x):
        x = np.clip(x, -5.0, 5.0)
        
        # Chaotic component based on logistic map
        chaotic = 0.0
        for i in range(self.dim):
            xi = x[i]
            for _ in range(3):
                xi = self.lambda_ * xi * (1 - xi)
            chaotic += xi**2
            
        # Gradient-based harmonic terms with variable curvature
        gradient = 0.0
        for i in range(self.dim):
            # Sine and cosine terms with varying frequencies and amplitudes
            freqs = [1.0, 2.0, 3.0]
            amps = [1.0, 0.5, 0.25]
            for f, a in zip(freqs, amps):
                gradient += a * np.sin(f * x[i]) * np.cos(f * x[i])
                
        # Saddle point structure with alternating convexity
        saddle = 0.0
        for i in range(self.dim):
            # Add cubic and quartic terms to create variable curvature
            saddle += self.c1 * x[i]**3 + self.c2 * x[i]**4
            
        # Cross-dimensional coupling with chaotic modulation
        coupling = 0.0
        for i in range(self.dim):
            for j in range(i+1, min(i+3, self.dim)):
                diff = x[i] - x[j]
                coupling += np.sin(diff) * np.cos(diff) * (1.0 + self.c3 * np.sin(x[i] + x[j]))
                
        # Adaptive scaling based on distance from origin
        norm_x = np.linalg.norm(x)
        scale_factor = 1.0 + self.beta * np.exp(-norm_x**2 / (2.0 * self.dim))
        
        # Combine components with chaotic offset
        result = scale_factor * (chaotic + gradient + saddle + coupling)
        
        # Add cubic polynomial terms for conditioning
        cubic_terms = np.sum(x**3)
        
        # Return final value with small random noise
        return result + 0.1 * cubic_terms + np.random.normal(0, 0.01)