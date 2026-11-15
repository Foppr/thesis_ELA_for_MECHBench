import numpy as np

class MultimodalBenchmark:
    def __init__(self, dim):
        self.dim = dim
    
    def f(self, x):
        # Ensure x is within bounds [-5, 5]
        x = np.clip(x, -5.0, 5.0)
        
        # Base quadratic term
        f_val = np.sum(x**2)
        
        # Add chaotic sine-wave interactions with varying frequencies
        for i in range(self.dim):
            f_val += 0.3 * np.sin(7 * x[i]) * np.cos(4 * x[i]) * np.sin(2 * x[i])
        
        # Add radial basis function components with random centers and widths
        centers = np.random.uniform(-5, 5, self.dim)
        widths = np.random.uniform(0.5, 2.0, self.dim)
        for i in range(self.dim):
            f_val += 0.1 * np.exp(-0.5 * ((x[i] - centers[i]) / widths[i])**2) * np.sin(3 * x[i])
        
        # Add asymmetric polynomial modulations
        for i in range(self.dim):
            if x[i] >= 0:
                f_val += 0.05 * (x[i]**4) * np.cos(1.5 * x[i])
            else:
                f_val += 0.08 * (x[i]**5) * np.sin(2 * x[i])
        
        # Add coupled exponential and trigonometric terms
        for i in range(self.dim):
            for j in range(i+1, min(i+3, self.dim)):  # Limited coupling
                f_val += 0.06 * np.exp(-0.2 * (x[i]**2 + x[j]**2)) * np.cos(5 * (x[i] - x[j]))
        
        # Add a global sinusoidal modulation based on the norm of x
        norm_x = np.linalg.norm(x)
        f_val += 0.1 * np.sin(0.5 * norm_x) * np.cos(0.3 * norm_x)
        
        return f_val