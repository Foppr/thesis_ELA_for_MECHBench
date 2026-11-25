import numpy as np

class MultimodalBenchmark:
    def __init__(self, dim):
        self.dim = dim
        self.global_min = 0.0
        
    def f(self, x):
        # Normalize input to [-5, 5] domain
        x = np.array(x)
        
        # Shift variables to center the function
        shifted_x = x - 1.0
        
        # Compute multiple sinusoidal components with exponentially increasing frequencies
        term1 = np.sum(shifted_x**2) / self.dim
        term2 = np.sum(np.cos(2 * np.pi * shifted_x)) / self.dim
        term3 = np.sum(shifted_x**4) / (4 * self.dim)
        
        # Add exponential scaling to create more complex landscape
        exp_term = np.sum(np.exp(0.5 * shifted_x**2)) / self.dim
        result = term1 - term2 + term3 + exp_term
        
        # Introduce additional complexity with a modified sine component and polynomial interaction
        sine_component = np.sum(np.sin(5 * np.pi * shifted_x)) / self.dim
        poly_interaction = np.sum(shifted_x**3) / (3 * self.dim)
        result += 0.7 * sine_component + 0.3 * poly_interaction
        
        # Add cross-dimensional interaction terms to increase problem difficulty
        cross_term = 0.1 * np.sum(shifted_x[:-1] * shifted_x[1:]) / (self.dim - 1) if self.dim > 1 else 0
        result += cross_term
        
        # Add a radial term with high-frequency oscillation
        radius = np.sqrt(np.sum(shifted_x**2))
        radial_term = 0.2 * radius * np.sin(5 * radius)
        result += radial_term
        
        return float(result)