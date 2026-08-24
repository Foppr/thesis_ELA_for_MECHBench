import numpy as np

class MultimodalBenchmark:
    def __init__(self, dim):
        self.dim = dim
    
    def f(self, x):
        # Ensure x is within bounds
        x = np.clip(x, -5.0, 5.0)
        
        # Chaotic sine-wave interaction component
        chaotic_term = np.sum(np.sin(10.0 * np.sin(x)) * np.cos(7.0 * np.cos(x)))
        
        # Radial polynomial decay with asymmetric exponents
        r = np.sqrt(np.sum(x**2))
        radial_decay = np.sum((1.0 + 0.5 * np.sin(3.0 * r)) * (x**3.2 + 0.3 * x**4.1))
        
        # Asymmetric Gaussian clustering with varying scales
        gaussian_clusters = 0.0
        for i in range(self.dim):
            gaussian_clusters += np.exp(-0.5 * ((x[i] - 2.0)**2 + (x[i] + 2.0)**2) / (0.5 + 0.3 * np.sin(i)))
        
        # Multi-scale periodic modulation
        periodic_mod = np.sum(np.sin(2.0 * x) * np.cos(3.0 * x) * np.sin(5.0 * x))
        
        # Hyperbolic tangent gradient enhancement
        tanh_grad = np.sum(np.tanh(x) * (x**2.7 + 0.5 * x**3.3))
        
        # Cross-dimensional coupling with exponential decay
        cross_coupling = np.sum(np.exp(-0.1 * np.abs(x)) * np.sin(4.0 * x) * np.cos(2.0 * x))
        
        # Fractal-like recursive sine component
        fractal_sine = np.sum(np.sin(np.sin(np.sin(x))) * np.cos(np.cos(np.cos(x))))
        
        # Combined objective function with weighted components
        return 0.3 * chaotic_term + 0.25 * radial_decay + 0.15 * gaussian_clusters + \
               0.1 * periodic_mod + 0.1 * tanh_grad + 0.05 * cross_coupling + 0.05 * fractal_sine