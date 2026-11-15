import numpy as np

class MultimodalBenchmark:
    def __init__(self, dim):
        self.dim = dim
        
    def f(self, x):
        # Ensure x is within bounds
        x = np.clip(x, -5.0, 5.0)
        
        # Base quadratic term
        f_val = np.sum(x**2)
        
        # Add chaotic sinusoidal perturbations with varying frequencies and amplitudes
        for i in range(self.dim):
            f_val += 0.3 * np.sin(13 * x[i]) * np.cos(9 * x[i]) * np.sin(5 * x[i]) * np.cos(3 * x[i])
            
        # Introduce asymmetric saddle points using polynomial and trigonometric mix
        for i in range(self.dim):
            f_val += 0.15 * (x[i]**3) * np.sin(8 * x[i]) * np.cos(6 * x[i])
            
        # Add fractal-like global minimum structure with recursive-like perturbations
        f_val += 0.2 * np.sum(np.sin(20 * x) * np.cos(15 * x) * np.sin(10 * x))
        
        # Include a complex landscape with varying amplitude and phase shifts
        f_val += 0.1 * np.sum((x**5) * np.sin(7 * x) * np.cos(4 * x))
        
        # Add a chaotic component to increase sensitivity to initial conditions
        chaotic_term = 0.08 * np.sum(np.sin(25 * x) * np.cos(20 * x) * np.sin(15 * x))
        f_val += chaotic_term
        
        return f_val