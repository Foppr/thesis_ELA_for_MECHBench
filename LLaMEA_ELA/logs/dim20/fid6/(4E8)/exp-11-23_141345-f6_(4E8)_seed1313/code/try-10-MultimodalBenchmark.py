import numpy as np

class MultimodalBenchmark:
    def __init__(self, dim):
        self.dim = dim
        
    def f(self, x):
        # Normalize input to [-1, 1] range
        x_normalized = x / 5.0
        
        # Radial component with polynomial oscillations
        r = np.sqrt(np.sum(x_normalized**2))
        
        # Polynomial oscillation term
        poly_osc = np.sum((x_normalized**4 - 2*x_normalized**2 + 1)**2)
        
        # Radial exponential decay term
        exp_decay = np.exp(-r**2)
        
        # Angular component with multiple peaks
        if self.dim >= 2:
            angles = np.arctan2(x_normalized[1], x_normalized[0])
            angular_peaks = np.sum(np.cos(3 * angles) + np.sin(5 * angles))
        else:
            angular_peaks = 0.0
            
        # Combine all components with different weights
        result = 0.5 * r**4 + 0.3 * poly_osc + 0.2 * exp_decay + 0.1 * angular_peaks
        
        # Add small random perturbation for non-deterministic behavior
        result += 0.01 * np.random.random()
        
        return result