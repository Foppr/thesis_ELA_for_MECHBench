import numpy as np

class MultimodalBenchmark:
    def __init__(self, dim):
        self.dim = dim
        self.alpha = 0.5
        self.beta = 2.0
        self.gamma = 1.5
        
    def f(self, x):
        # Ensure x is within bounds
        x = np.clip(x, -5.0, 5.0)
        
        # Quadratic base with dimension-dependent scaling
        result = np.sum(x**2 * (1 + 0.1 * np.sin(np.arange(self.dim))))
        
        # Sinusoidal oscillations with varying frequencies and amplitudes
        sin_term = 0.0
        for i in range(self.dim):
            freq = 2**(i % 4) * (1 + 0.3 * np.cos(i))
            amp = 1.0 + 0.2 * np.sin(i)
            sin_term += amp * np.sin(freq * x[i]) * np.cos(freq * x[(i+1) % self.dim])
            
        # Radial basis function component with asymmetric weights
        rbf_term = 0.0
        for i in range(self.dim):
            for j in range(i+1, self.dim):
                dist = (x[i] - x[j])**2
                weight = 0.5 + 0.5 * np.sin(i * j)
                rbf_term += weight * np.exp(-self.gamma * dist) * np.sin(2 * np.pi * (x[i] + x[j]))
                
        # Cross-dimensional interaction with asymmetric coupling
        cross_term = 0.0
        for i in range(self.dim):
            for j in range(self.dim):
                if i != j:
                    diff = x[i] - x[j]
                    coupling = 0.3 * np.sin(i) * np.cos(j)
                    cross_term += coupling * diff**3 * np.exp(-0.1 * np.abs(diff))
                    
        # Asymmetric penalty term with polynomial and trigonometric components
        penalty = 0.0
        for i in range(self.dim):
            val = x[i]
            penalty += (val**5 + val**3 + val) * (1 + 0.2 * np.sin(i)) * np.cos(val)
            
        return result + self.alpha * sin_term + self.beta * rbf_term + self.gamma * cross_term + penalty