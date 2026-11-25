import numpy as np

class MultimodalBenchmark:
    def __init__(self, dim):
        self.dim = dim
        
    def f(self, x):
        # Scale input to [-1, 1] for stability
        x_scaled = x / 5.0
        
        # Radial component with exponential decay and modified amplitude
        r = np.sqrt(np.sum(x_scaled**2))
        radial = np.exp(-r**2) * (1.0 + 0.7 * np.sin(4 * r) + 0.3 * np.cos(2 * r))
        
        # Angular component with altered frequencies and added cross-terms
        angular = 0.0
        if self.dim > 1:
            angles = np.arctan2(x_scaled[1], x_scaled[0])
            for i in range(min(4, self.dim)):
                angular += np.sin((i+2) * angles) * np.cos((i+1) * angles)
            # Add cross-dimensional interactions
            if self.dim >= 3:
                angular += 0.5 * np.sin(x_scaled[0] * x_scaled[1]) * np.cos(x_scaled[2])
        
        # High-frequency oscillation component with modified coefficients
        oscillation = np.sum(0.8 * np.sin(12 * x_scaled)**2 + 0.6 * np.cos(9 * x_scaled)**2)
        
        # Cross-term interaction between dimensions
        cross_term = 0.05 * np.sum([x_scaled[i] * x_scaled[(i+1) % self.dim] for i in range(self.dim)])
        
        # Add a small perturbation term to increase complexity
        perturbation = 0.01 * np.sum(np.sin(7 * x_scaled) * np.cos(5 * x_scaled))
        
        # Combined function with multiple competing terms
        return radial + 0.4 * angular + 0.15 * oscillation + 0.002 * np.sum(x_scaled**4) + cross_term + perturbation