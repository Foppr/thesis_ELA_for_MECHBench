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
        
        # Chaotic tent map component for dynamic behavior
        tent_map = 0.0
        if self.dim > 1:
            for i in range(self.dim - 1):
                tent_map += np.abs(x_norm[i] - x_norm[i+1]) * np.sin(100 * x_norm[i] * x_norm[i+1])
        
        # High-frequency trigonometric terms with varying frequencies and amplitudes
        trig1 = np.sum(np.sin(30 * x_norm) * np.cos(25 * x_norm))
        trig2 = np.sum(np.sin(45 * x_norm) * np.cos(35 * x_norm))
        trig3 = np.sum(np.sin(60 * x_norm) * np.cos(50 * x_norm))
        
        # Adaptive radial basis functions with dimension-dependent widths
        rbf = 0.0
        for i in range(self.dim):
            width = 2.0 + 0.5 * np.sin(i * np.pi / self.dim)
            rbf += np.exp(-width * x_norm[i]**2)
        
        # Polynomial interaction terms with mixed exponents
        poly_interaction = np.sum(x_norm[:-1]**3 * x_norm[1:]**3)
        
        # Multi-scale exponential decay with varying rates
        exp_decay = np.sum(np.exp(-2.0 * x_norm**2) + np.exp(-0.5 * x_norm**2) + np.exp(-0.1 * x_norm**2))
        
        # Cross-dimensional coupling with sine modulation
        coupling = np.sum(np.sin(x_norm[:-1] * x_norm[1:]) * (x_norm[:-1]**2 + x_norm[1:]**2))
        
        # Non-linear transformation using sigmoid-like function
        sigmoid_term = np.sum(1.0 / (1.0 + np.exp(-5.0 * x_norm)))
        
        # Add chaotic modulation based on golden ratio
        golden_mod = np.sum(np.sin(np.pi * (1.618 * x_norm)) * np.cos(np.pi * (1.618 * x_norm)))
        
        # Combine all components with carefully tuned weights
        return (0.2 * quadratic + 
                0.25 * trig1 + 
                0.2 * trig2 + 
                0.15 * trig3 + 
                0.1 * tent_map + 
                0.1 * rbf + 
                0.08 * poly_interaction + 
                0.05 * exp_decay + 
                0.05 * coupling + 
                0.03 * sigmoid_term + 
                0.02 * golden_mod)