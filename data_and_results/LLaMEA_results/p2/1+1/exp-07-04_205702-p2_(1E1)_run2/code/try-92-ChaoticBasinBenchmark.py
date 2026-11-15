import numpy as np

class ChaoticBasinBenchmark:
    def __init__(self, dim):
        self.dim = dim
        # Precompute constants for chaotic behavior
        self.c1 = 3.8
        self.c2 = 0.5
        self.c3 = 2.0
        self.c4 = 1.2
        
    def f(self, x):
        # Ensure x is within bounds
        x = np.clip(x, -5.0, 5.0)
        
        # Base quadratic term
        f1 = 0.5 * np.sum(x**2)
        
        # Fractal basin structure using recursive sine-cosine combinations
        f2 = 0.0
        for i in range(self.dim):
            f2 += np.sin(self.c1 * x[i]) * np.cos(self.c2 * x[i]) * np.exp(-0.1 * x[i]**2)
        
        # Chaotic gradient field using logistic map modulation
        f3 = 0.0
        for i in range(self.dim):
            # Logistic map for chaotic behavior
            chaotic_factor = 0.5 + 0.5 * np.sin(self.c3 * x[i] + self.c4 * np.sin(x[i]))
            f3 += chaotic_factor * np.sin(2.0 * x[i]) * np.cos(1.5 * x[i])
        
        # Dynamic saddle points with time-like parameter
        f4 = 0.0
        for i in range(self.dim):
            for j in range(i+1, self.dim):
                # Dynamic interaction based on position and dimension
                dynamic_term = np.sin(0.3 * (x[i] + x[j])) * np.cos(0.2 * (x[i] - x[j]))
                f4 += dynamic_term * (1.0 + 0.2 * np.sin(0.5 * (i + j)))
        
        # Asymmetric peaks with fractal-like structure
        f5 = 0.0
        for i in range(self.dim):
            # Fractal-like peak with varying amplitude and width
            amplitude = 2.0 + np.sin(0.7 * i) * 1.5
            width = 0.5 + 0.3 * np.cos(0.4 * i)
            peak = amplitude * np.exp(-0.5 * ((x[i] - np.sin(0.6 * i)) / width)**2)
            f5 += peak
        
        # Cross-term interactions with exponential decay
        f6 = 0.0
        for i in range(self.dim):
            for j in range(i+1, self.dim):
                cross_interaction = np.exp(-0.1 * (x[i] - x[j])**2) * np.sin(0.5 * x[i] * x[j])
                f6 += cross_interaction
        
        # Add noise for robustness
        noise = 0.02 * np.random.rand()
        
        # Combine all components
        return f1 + f2 + f3 + f4 + f5 + f6 + noise