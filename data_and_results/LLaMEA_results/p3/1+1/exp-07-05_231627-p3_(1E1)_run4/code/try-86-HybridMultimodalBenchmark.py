import numpy as np

class HybridMultimodalBenchmark:
    def __init__(self, dim):
        self.dim = dim
        self.global_min = 0.0
        self.bounds = type('Bounds', (), {'lb': np.full(dim, -5.0), 'ub': np.full(dim, 5.0)})()
    
    def f(self, x):
        # Normalize input to [-1, 1] for better numerical stability
        x_norm = x / 5.0
        
        # Radial component with multiple concentric peaks
        r = np.sqrt(np.sum(x_norm**2, axis=-1, keepdims=True))
        radial = np.exp(-5 * r) * np.sin(10 * np.pi * r)**2
        
        # Trigonometric oscillations in each dimension with varying frequencies
        trig_component = np.sum(np.sin(15 * np.pi * x_norm) * np.cos(12 * np.pi * x_norm) + 
                               np.sin(8 * np.pi * x_norm**2) * np.cos(6 * np.pi * x_norm**2), axis=-1)
        
        # Exponential decay with sinusoidal modulation
        exp_decay = np.sum(np.exp(-3 * np.abs(x_norm)) * np.sin(20 * np.pi * x_norm)**2, axis=-1)
        
        # Cross-dimensional interaction with polynomial coupling
        poly_interaction = np.sum((x_norm[:-1] * x_norm[1:])**3, axis=-1) if self.dim > 1 else 0
        
        # Gaussian mixture with varying covariances and positions
        mixture = 0
        for i in range(8):
            center = np.full(self.dim, (i - 3.5) / 4.0)
            cov = 0.5 + 0.3 * np.sin(i)
            diff = x_norm - center
            mixture += np.exp(-0.5 * np.sum((diff / cov)**2, axis=-1))
        
        # Fractional power and logarithmic distortion
        fractional = np.sum(np.abs(x_norm)**1.7 + 0.3 * np.log(1 + np.abs(x_norm)))
        
        # Combine components with adaptive weights based on input magnitude
        weights = 0.4 + 0.3 * np.sin(np.pi * r)
        result = weights * (0.3 * radial + 0.25 * trig_component + 0.2 * exp_decay + 
                           0.15 * poly_interaction + 0.1 * mixture + 0.05 * fractional)
        
        # Add dynamic noise that scales with function value
        noise = 0.02 * (1 + np.abs(result)) * np.random.uniform(-0.5, 0.5)
        
        return np.mean(result) + noise