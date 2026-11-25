import numpy as np

class ChaoticGradientBenchmark:
    def __init__(self, dim):
        self.dim = dim
        # Precompute chaotic sequence for dynamic scaling
        self.chaotic_sequence = np.sin(np.arange(dim) * np.pi / 4) * 0.5 + 0.5
    
    def f(self, x):
        # Ensure x is within bounds [-5, 5]
        x = np.clip(x, -5.0, 5.0)
        
        # Chaotic gradient component with varying curvature
        chaotic_grad = 0.0
        for i in range(self.dim):
            xi = x[i]
            # Use chaotic scaling factor
            scale = self.chaotic_sequence[i % len(self.chaotic_sequence)]
            # Add chaotic sinusoidal influence
            chaotic_grad += scale * (xi**3 - 3*xi**2 + 2*xi) * np.sin(xi)
        
        # Saddle point structure with multiple interacting dimensions
        saddle = 0.0
        for i in range(self.dim):
            xi = x[i]
            x_next = x[(i + 1) % self.dim]
            # Create saddle-like behavior
            saddle += (xi**2 - 1)**2 * (x_next**2 - 1)**2
        
        # Dynamic curvature component with exponential scaling
        curvature = 0.0
        for i in range(self.dim):
            xi = x[i]
            # Exponential scaling based on chaotic sequence
            exp_scale = np.exp(-self.chaotic_sequence[i % len(self.chaotic_sequence)] * xi)
            curvature += exp_scale * xi**4
        
        # Cross-dimensional interaction with varying weights
        cross_interaction = 0.0
        for i in range(self.dim):
            xi = x[i]
            x_prev = x[(i - 1) % self.dim]
            x_next = x[(i + 1) % self.dim]
            # Add weighted interactions
            cross_interaction += 0.3 * xi * np.sin(x_prev + x_next)
        
        # Global structure with multiple local minima
        global_structure = 0.0
        for i in range(self.dim):
            xi = x[i]
            # Add periodic modulation
            global_structure += (xi - np.sin(xi))**2
        
        # Combine all components with dynamic weights
        return 0.7 * chaotic_grad + 1.2 * saddle + 0.8 * curvature + 0.5 * cross_interaction + 1.0 * global_structure