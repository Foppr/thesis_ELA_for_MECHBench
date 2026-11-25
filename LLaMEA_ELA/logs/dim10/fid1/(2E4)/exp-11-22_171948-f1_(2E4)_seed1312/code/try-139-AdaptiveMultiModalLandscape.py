import numpy as np

class AdaptiveMultiModalLandscape:
    def __init__(self, dim):
        self.dim = dim
        # Precompute some constants for efficiency
        self.poly_exponents = np.arange(1, dim + 1)
        self.trig_freqs = np.arange(1, dim + 1) * np.pi / 2.0
        
    def f(self, x):
        # Ensure x is within bounds
        x = np.clip(x, -5.0, 5.0)
        
        # Polynomial component with varying exponents
        poly_term = np.sum((x ** self.poly_exponents) * np.exp(-0.1 * np.abs(x)))
        
        # Trigonometric component with varying frequencies
        trig_term = np.sum(np.sin(self.trig_freqs * x) * np.cos(self.trig_freqs * x))
        
        # Radial basis function component with adaptive widths
        rbfs = 0.0
        for i in range(self.dim):
            width = 1.0 + 0.5 * np.sin(i)
            rbfs += np.exp(-width * (x[i] - 2.0)**2) + np.exp(-width * (x[i] + 2.0)**2)
        
        # Asymmetric hill-climbing structures
        hills = 0.0
        for i in range(self.dim):
            if x[i] > 0:
                hills += (x[i] - 1.0)**4
            else:
                hills += (x[i] + 1.0)**4
        
        # Adaptive conditioning based on gradient magnitude
        grad_magnitude = np.sum(np.abs(np.gradient(x)))
        condition_factor = 1.0 + 0.3 * np.tanh(grad_magnitude)
        
        # Cross-term coupling with asymmetric weights
        cross_term = 0.0
        for i in range(self.dim - 1):
            weight = 1.0 + 0.2 * np.sin(i)
            cross_term += weight * (x[i] - x[i+1])**2
        
        # Final combined function with noise injection
        result = (poly_term + trig_term + rbfs + hills + cross_term) * condition_factor
        
        # Add controlled noise to increase complexity
        noise = np.sum(np.sin(10 * x) * np.cos(15 * x)) * 0.01
        
        return result + noise