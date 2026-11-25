import numpy as np

class MultimodalComplexBenchmark:
    def __init__(self, dim):
        self.dim = dim
        
    def f(self, x):
        # Ensure x is within bounds [-5, 5]
        x = np.clip(x, -5.0, 5.0)
        
        # Polynomial component with mixed degrees
        poly_component = np.sum(x**4 + 0.5 * x**3 + 2 * x**2 + 0.1 * x)
        
        # Trigonometric oscillations with varying frequencies and amplitudes
        trig_component = 0
        for i in range(self.dim):
            trig_component += (np.sin(5 * x[i]) * np.cos(3 * x[i]) + 
                             0.5 * np.sin(7 * x[i]) * np.cos(2 * x[i]) + 
                             0.3 * np.sin(11 * x[i]))
        
        # Radial basis function component with multiple centers
        rbf_component = 0
        centers = np.linspace(-4, 4, min(5, self.dim))
        for i in range(self.dim):
            center = centers[i % len(centers)] if len(centers) > 0 else 0
            rbf_component += np.exp(-0.5 * (x[i] - center)**2) * np.sin(2 * x[i])
        
        # Cross-terms creating interaction between dimensions
        cross_terms = 0
        for i in range(self.dim):
            for j in range(i+1, min(i+4, self.dim)):
                cross_terms += (x[i]**2 + x[j]**2) * np.sin(0.3 * x[i] * x[j])
        
        # Sigmoidal modulation to create sharp transitions
        sigmoid_component = 0
        for i in range(self.dim):
            sigmoid_component += 1 / (1 + np.exp(-x[i])) * np.cos(0.5 * x[i])
        
        # High-frequency noise component
        noise_component = 0
        for i in range(self.dim):
            noise_component += np.sin(20 * x[i]) * np.cos(15 * x[i]) * 0.05
        
        # Combine all components with different weights
        return (0.4 * poly_component + 
                0.3 * trig_component + 
                0.2 * rbf_component + 
                0.1 * cross_terms + 
                0.15 * sigmoid_component + 
                0.05 * noise_component + 
                2 * np.sum(np.abs(x)))