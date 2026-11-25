import numpy as np

class ChaoticSaddleBenchmark:
    def __init__(self, dim):
        self.dim = dim
    
    def f(self, x):
        # Ensure x is within bounds [-5, 5]
        x = np.clip(x, -5.0, 5.0)
        
        # Exponential potential wells with chaotic dynamics
        potential = 0.0
        for i in range(self.dim):
            potential += np.exp(-0.5 * (x[i] - 2)**2) + np.exp(-0.5 * (x[i] + 2)**2)
            potential += 0.3 * np.exp(-0.3 * (x[i] - 1)**2) * np.sin(5 * x[i])
        
        # Cross-dimensional coupling with chaotic sine-wave interactions
        coupling = 0.0
        for i in range(self.dim):
            j = (i + 1) % self.dim
            k = (i + 2) % self.dim
            coupling += 0.5 * np.sin(x[i]) * np.cos(x[j]) * np.exp(-0.1 * x[k]**2)
            coupling += 0.2 * np.tanh(x[i] * x[j]) * np.log(1 + x[k]**2)
        
        # Saddle-point structure with hyperbolic tangent and logistic components
        saddle = 0.0
        for i in range(self.dim):
            saddle += 0.8 * np.tanh(x[i])**3 + 0.4 * (np.log(1 + np.exp(x[i])) - x[i])
            saddle += 0.6 * np.sinh(0.5 * x[i]) * np.cos(0.7 * x[(i + 1) % self.dim])
        
        # Add noise with chaotic phase modulation
        noise = 0.0
        for i in range(self.dim):
            phase = np.sin(np.pi * x[i] * (i + 1)) + np.cos(np.pi * x[(i + 1) % self.dim] * (i + 2))
            noise += 0.15 * np.sin(10 * x[i] + phase) * np.cos(8 * x[(i + 1) % self.dim])
        
        # Combine all components with scaling factors
        return 1.2 * potential + 1.5 * coupling + 1.0 * saddle + 0.8 * noise