import numpy as np

class ChaoticBasinBenchmark:
    def __init__(self, dim):
        self.dim = dim
        self.global_min = 0.0
        self.bounds = type('Bounds', (), {'lb': np.full(dim, -5.0), 'ub': np.full(dim, 5.0)})()
    
    def f(self, x):
        # Normalize input to [-1, 1] for internal computations
        x_norm = x / 5.0
        
        # Base quadratic component with adaptive scaling
        base = np.sum(x_norm**2)
        
        # Chaotic modulation using logistic map-like behavior with position-dependent parameters
        chaos_mod = 0
        for i in range(self.dim):
            # Dynamic parameter based on position
            r = 3.8 + 0.2 * np.sin(x_norm[i] * np.pi)
            chaos_mod += np.sin(r * x_norm[i] * (1 - x_norm[i]**2)) * np.cos(2 * x_norm[i])
        
        # Multi-scale sinusoidal interference creating dynamic valleys and ridges
        interference = 0
        scales = [2, 5, 8, 12]
        for scale in scales:
            interference += np.sin(scale * np.pi * x_norm) * np.cos(scale * np.pi * x_norm**2)
        
        # Adaptive basin structure with position-dependent depth and width
        basin = 0
        for i in range(self.dim):
            # Create varying basin depths based on position
            depth = 2.0 + 1.5 * np.sin(3 * x_norm[i])
            width = 1.0 + 0.5 * np.cos(2 * x_norm[i])
            basin += depth * np.exp(-0.5 * (x_norm[i] / width)**2)
        
        # Dynamic gradient component that shifts based on input
        grad_shift = np.sum(np.sin(10 * x_norm) * np.cos(7 * x_norm))
        
        # Cross-dimensional coupling with varying strength
        coupling = 0
        for i in range(self.dim - 1):
            coupling += (x_norm[i] - x_norm[i+1])**4 + 0.5 * (x_norm[i] + x_norm[i+1])**3
        
        # Time-varying harmonic component
        time_harmonic = np.sin(15 * np.sum(x_norm)) * np.cos(12 * np.sum(x_norm**2))
        
        # Combine all components with dynamic weights
        result = 0.3 * base + 0.25 * chaos_mod + 0.2 * interference + 0.15 * basin + 0.08 * grad_shift + 0.05 * coupling + 0.02 * time_harmonic
        
        # Add position-dependent noise
        noise = 0.01 * np.abs(np.sum(x_norm**3)) * np.random.uniform(-1, 1)
        
        return result + noise