import numpy as np

class MultimodalBenchmark:
    def __init__(self, dim):
        self.dim = dim
        
    def f(self, x):
        # Normalize input to [-1, 1] range
        x_norm = x / 5.0
        
        # Polynomial chaos component with mixed degrees
        poly_chaos = np.sum((x_norm**2 + 0.5 * x_norm**4 + 0.1 * x_norm**6))
        
        # Radial basis function with multiple centers
        centers = np.linspace(-1, 1, min(5, self.dim))
        rbf = 0.0
        for i in range(len(centers)):
            rbf += np.exp(-10 * np.sum((x_norm - centers[i])**2))
        
        # Trigonometric coupling with varying frequencies
        trig_coupling = 0.0
        for i in range(self.dim):
            for j in range(i+1, self.dim):
                trig_coupling += np.sin(5 * (x_norm[i] - x_norm[j])) * np.cos(3 * (x_norm[i] + x_norm[j]))
        
        # Mixed conditioning and interaction terms
        cond_term = np.sum(x_norm**2 * np.exp(-0.5 * x_norm**2))
        
        # Nonlinear interaction with chaotic modulation
        chaotic_interaction = 0.0
        for i in range(self.dim):
            chaotic_interaction += np.sin(7 * x_norm[i]) * np.cos(11 * x_norm[i]) * np.sin(13 * x_norm[i])
        
        # Add a global scaling factor and combine all components
        return 0.5 * poly_chaos + 0.3 * rbf + 0.2 * trig_coupling + 0.1 * cond_term + 0.15 * chaotic_interaction