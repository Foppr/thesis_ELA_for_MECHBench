import numpy as np

class MultimodalChaoticBenchmark:
    def __init__(self, dim):
        self.dim = dim
    
    def f(self, x):
        # Ensure x is within bounds [-5, 5]
        x = np.clip(x, -5.0, 5.0)
        
        # Base quadratic term
        result = 0.1 * np.sum(x**2)
        
        # Add radial basis function components with varying centers and widths
        for i in range(min(self.dim, 20)):
            center = 3.0 * np.sin(i * 0.7) + 2.0 * np.cos(i * 0.5)
            width = 0.5 + 0.3 * np.sin(i * 0.3)
            result += 10.0 * np.exp(-0.5 * ((x[i % self.dim] - center) / width)**2)
        
        # Add asymmetric saddle points with periodic modulation
        for i in range(min(self.dim, 15)):
            freq = 2.0 + 0.5 * np.sin(i * 0.4)
            phase = i * 0.3
            saddle_pos = 2.5 * np.cos(freq * x[i % self.dim] + phase)
            result += 5.0 * (x[i % self.dim] - saddle_pos)**2 * np.exp(-0.1 * (x[i % self.dim] - saddle_pos)**2)
        
        # Add high-frequency sinusoidal coupling between dimensions
        coupling = 0.0
        for i in range(self.dim - 1):
            coupling += np.sin(10.0 * (x[i] + x[i+1])) * np.cos(5.0 * (x[i] - x[i+1]))
        result += 2.0 * coupling
        
        # Add fractal-like periodic component
        fractal = 0.0
        for i in range(self.dim):
            fractal += np.sin(30.0 * x[i]) * np.cos(15.0 * x[i]) * np.sin(7.0 * x[i])
        result += 1.5 * fractal
        
        # Add multi-scale chaotic modulation
        chaotic = 0.0
        for i in range(self.dim):
            chaotic += np.sin(20.0 * x[i] + np.sin(5.0 * x[i])) * np.cos(10.0 * x[i] + np.cos(3.0 * x[i]))
        result += 1.2 * chaotic
        
        # Add asymmetric polynomial terms
        for i in range(self.dim):
            result += 0.5 * x[i]**5 - 1.5 * x[i]**3 + 2.0 * x[i]**2
        
        return result