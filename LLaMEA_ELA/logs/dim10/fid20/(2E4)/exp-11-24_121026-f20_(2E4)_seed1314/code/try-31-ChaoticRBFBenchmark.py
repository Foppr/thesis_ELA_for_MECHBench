import numpy as np

class ChaoticRBFBenchmark:
    def __init__(self, dim):
        self.dim = dim
        # Precompute logistic map parameters for chaos generation
        self.r_values = np.linspace(3.5, 4.0, dim)
        
    def f(self, x):
        # Normalize input to [-1, 1]
        x_norm = x / 5.0
        
        # Logistic map chaos component - creates ergodic behavior
        chaos = 0.0
        for i in range(min(5, self.dim)):
            r = self.r_values[i % len(self.r_values)]
            # Use previous dimension value to seed next chaotic value
            if i == 0:
                prev_val = x_norm[i] if np.abs(x_norm[i]) < 1.0 else (x_norm[i] / np.abs(x_norm[i]))
            else:
                prev_val = x_norm[i-1] if np.abs(x_norm[i-1]) < 1.0 else (x_norm[i-1] / np.abs(x_norm[i-1]))
            
            chaos += r * prev_val * (1 - prev_val)
        
        # Radial Basis Function component with multiple local minima
        rbf = 0.0
        centers = np.linspace(-1, 1, 9)
        for i in range(9):
            center = centers[i % len(centers)]
            rbf += np.exp(-5 * (x_norm - center)**2) * np.sin(2 * np.pi * (x_norm - center))
        
        # Saddle-point structure component
        saddle = 0.0
        for i in range(self.dim):
            saddle += (x_norm[i]**2 - 1)**2 * (x_norm[i]**4 - 1)
            
        # Cross-term interaction to increase complexity
        cross_term = np.sum(x_norm**3 * np.sin(5 * x_norm))
        
        # Global conditioning term
        global_term = np.sum(np.abs(x_norm)**1.5)
        
        return 0.1 * chaos + 0.3 * rbf + 0.2 * saddle + 0.15 * cross_term + 0.25 * global_term