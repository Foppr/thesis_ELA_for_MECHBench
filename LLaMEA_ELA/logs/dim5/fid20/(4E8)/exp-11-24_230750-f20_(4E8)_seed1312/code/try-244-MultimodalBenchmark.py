import numpy as np

class MultimodalBenchmark:
    def __init__(self, dim):
        self.dim = dim
    
    def f(self, x):
        # Ensure x is within bounds [-5, 5]
        x = np.clip(x, -5.0, 5.0)
        
        # Chaotic oscillator component with logistic map
        chaotic = 0.0
        r = 3.9
        for i in range(self.dim):
            if i == 0:
                chaotic += (r * 0.5 * (1 - 0.5)) ** 2
            else:
                chaotic += (r * x[i-1] * (1 - x[i-1])) ** 2
        
        # Radial basis function with Gaussian peaks
        radial = 0.0
        for i in range(self.dim):
            radial += np.exp(-0.5 * ((x[i] - 2.0) ** 2 + (x[i] + 2.0) ** 2))
        
        # Asymmetric saddle points with polynomial gradients
        saddle = 0.0
        for i in range(self.dim):
            saddle += x[i] ** 4 - 2 * x[i] ** 2 + 0.5 * x[i] ** 3
        
        # Cross-dimensional coupling with trigonometric interactions
        cross = 0.0
        for i in range(self.dim):
            for j in range(i+1, min(i+3, self.dim)):  # Limited coupling
                cross += np.sin(x[i]) * np.cos(x[j]) * (x[i] ** 2 + x[j] ** 2)
        
        # Logarithmic spiral gradient structure
        spiral = 0.0
        for i in range(self.dim):
            if x[i] != 0:
                spiral += np.log(np.abs(x[i])) * np.sin(x[i])
        
        # Hyperbolic tangent modulation of the landscape
        tanh_mod = 0.0
        for i in range(self.dim):
            tanh_mod += np.tanh(x[i]) ** 3
        
        # Combine all components with dynamic weights
        return 0.25 * chaotic + 0.2 * radial + 0.2 * saddle + 0.15 * cross + 0.1 * spiral + 0.1 * tanh_mod