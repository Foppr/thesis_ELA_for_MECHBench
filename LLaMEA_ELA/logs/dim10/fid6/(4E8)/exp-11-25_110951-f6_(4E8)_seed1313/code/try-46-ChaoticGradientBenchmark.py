import numpy as np

class ChaoticGradientBenchmark:
    def __init__(self, dim):
        self.dim = dim
    
    def f(self, x):
        x = np.array(x)
        
        # Base quadratic term with adaptive conditioning
        quadratic = 0.5 * np.sum(x**2)
        
        # Exponentially decaying harmonic oscillations with chaotic phase shifts
        harmonic = 0
        for i in range(self.dim):
            freq = 2**(i % 3 + 1)  # Varying frequencies with exponential growth
            phase = np.sin(0.1 * x[i]) * np.cos(0.05 * x[(i+1) % self.dim])
            harmonic += np.sin(freq * x[i] + phase) * np.exp(-0.1 * np.abs(x[i]))
        
        # Saddle-point corridor with adaptive scaling
        saddle = 0
        for i in range(self.dim-1):
            saddle += (x[i]**2 - x[i+1]**2) * np.cos(0.5 * x[i]) * np.sin(0.3 * x[i+1])
        
        # Chaotic gradient modulation with exponential decay
        chaotic = 0
        for i in range(self.dim):
            chaotic += np.sin(x[i] * np.exp(-0.05 * i)) * np.cos(x[i] * np.exp(-0.03 * i))
        
        # Adaptive penalty term based on dimensionality and gradient behavior
        penalty = 0.1 * np.sum(np.abs(x)**(1.5 + 0.1 * np.arange(self.dim)))
        
        # Combined fitness function with balanced weights
        return quadratic + 0.3 * harmonic + 0.2 * saddle + 0.15 * chaotic + penalty