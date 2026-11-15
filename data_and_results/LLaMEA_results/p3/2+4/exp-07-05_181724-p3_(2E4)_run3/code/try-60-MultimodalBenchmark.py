import numpy as np

class MultimodalBenchmark:
    def __init__(self, dim):
        self.dim = dim
        self.global_min = 0.0
        
    def f(self, x):
        # Normalize input to [-1, 1] range
        x_norm = x / 5.0
        
        # Quadratic base term
        quadratic = np.sum(x_norm**2)
        
        # High-frequency sinusoidal components with varying amplitudes
        sin1 = np.sum(np.sin(10 * x_norm) * np.cos(7 * x_norm))
        sin2 = np.sum(np.sin(15 * x_norm) * np.cos(12 * x_norm))
        sin3 = np.sum(np.sin(20 * x_norm) * np.cos(18 * x_norm))
        
        # Polynomial interactions with mixed exponents
        poly = np.sum(0.5 * x_norm**6 + 0.3 * x_norm**5 + 0.2 * x_norm**4)
        
        # Coupling terms between adjacent dimensions
        coupling = np.sum(x_norm[:-1]**3 * x_norm[1:]**3)
        
        # Chaotic component using a modified logistic map
        chaotic = 0.0
        if self.dim > 1:
            for i in range(self.dim - 1):
                chaotic += np.sin(50 * x_norm[i] * x_norm[i+1] + np.sin(x_norm[i]))
        
        # Radial basis functions with varying widths
        rbf = np.sum(np.exp(-2.0 * x_norm**2) + np.exp(-5.0 * x_norm**2) + np.exp(-10.0 * x_norm**2))
        
        # Exponential decay with oscillatory modulation
        exp_mod = np.sum(np.exp(-x_norm**2) * np.sin(3 * x_norm))
        
        # Mixed trigonometric and polynomial term
        mixed = np.sum(np.sin(x_norm) * x_norm**3 + np.cos(x_norm) * x_norm**2)
        
        # Add noise for non-triviality
        noise = 0.001 * np.random.random()
        
        # Combine all components with carefully tuned weights
        return (0.2 * quadratic + 
                0.25 * sin1 + 
                0.2 * sin2 + 
                0.15 * sin3 + 
                0.15 * poly + 
                0.1 * coupling + 
                0.1 * chaotic + 
                0.08 * rbf + 
                0.05 * exp_mod + 
                0.05 * mixed + 
                noise)