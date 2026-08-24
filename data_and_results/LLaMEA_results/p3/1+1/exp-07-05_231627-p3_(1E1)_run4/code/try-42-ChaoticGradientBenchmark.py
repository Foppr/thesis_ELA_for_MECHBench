import numpy as np

class ChaoticGradientBenchmark:
    def __init__(self, dim):
        self.dim = dim
        self.global_min = 0.0
        self.bounds = type('Bounds', (), {'lb': np.full(dim, -5.0), 'ub': np.full(dim, 5.0)})()
    
    def f(self, x):
        # Normalize input to [-1, 1]
        x_norm = x / 5.0
        
        # Base quadratic component
        quadratic = np.sum(x_norm**2)
        
        # Chaotic sine modulation with dynamic frequency
        chaotic_mod = np.sum(np.sin(10 * np.pi * x_norm * (1 + 0.5 * np.sin(5 * np.pi * x_norm))) * 
                            np.cos(8 * np.pi * x_norm * (1 + 0.3 * np.cos(7 * np.pi * x_norm))))
        
        # Multi-scale Gaussian peaks with dynamic positions and amplitudes
        peaks = 0
        for i in range(20):
            center = np.sin(i * np.pi / 10) * np.ones(self.dim)
            amp = 1.5 + 0.5 * np.sin(i * np.pi / 5)
            sigma = 0.3 + 0.2 * np.cos(i * np.pi / 8)
            peaks += amp * np.exp(-np.sum(((x_norm - center) / sigma)**2) / 2)
        
        # Adaptive polynomial with varying degree based on dimension
        poly = 0
        for i in range(1, 6):
            poly += (i + 1) * np.sum(x_norm**(2*i + 1))
        
        # Gradient-based interaction terms with directional bias
        grad_interaction = 0
        for i in range(self.dim - 1):
            grad_interaction += (x_norm[i] - x_norm[i+1])**4 * np.sin(15 * np.pi * (x_norm[i] + x_norm[i+1]))
        
        # Dynamic saddle point component with time-like parameter
        saddle = 0
        for i in range(self.dim):
            saddle += np.sin(20 * np.pi * x_norm[i]) * np.cos(15 * np.pi * x_norm[i]) * \
                     np.exp(-0.5 * np.sum(x_norm**2)) * (1 + 0.2 * np.sin(3 * np.pi * i))
        
        # Combine components with adaptive weights
        result = 0.4 * quadratic + 0.3 * chaotic_mod + 0.2 * peaks + 0.1 * poly + 0.05 * grad_interaction + 0.05 * saddle
        
        # Add dimensionality-dependent noise
        noise = 0.02 * (1 + 0.1 * self.dim) * np.random.random()
        
        return result + noise