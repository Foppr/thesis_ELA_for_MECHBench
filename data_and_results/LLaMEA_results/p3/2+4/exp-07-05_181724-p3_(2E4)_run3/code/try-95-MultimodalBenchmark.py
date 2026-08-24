import numpy as np

class MultimodalBenchmark:
    def __init__(self, dim):
        self.dim = dim
        self.global_min = 0.0
        
    def f(self, x):
        # Normalize input to [-1, 1] range
        x_norm = x / 5.0
        
        # Polynomial chaos component with mixed exponents
        poly_chaos = np.sum(0.5 * x_norm**6 + 0.3 * x_norm**5 + 0.2 * x_norm**4 + 0.1 * x_norm**3)
        
        # Gaussian radial basis functions with varying widths and centers
        rbf_sum = 0.0
        centers = np.linspace(-1, 1, min(5, self.dim))
        for i, center in enumerate(centers):
            if i < self.dim:
                width = 0.5 + 0.5 * np.sin(i * np.pi / 4)
                rbf_sum += np.exp(-width * (x_norm[i] - center)**2)
        
        # Quaternion-inspired gradient component with complex interaction
        quat_grad = 0.0
        if self.dim >= 4:
            for i in range(0, self.dim - 3, 4):
                if i + 3 < self.dim:
                    quat_grad += (x_norm[i]**2 + x_norm[i+1]**2) * (x_norm[i+2]**2 + x_norm[i+3]**2)
        
        # Trigonometric chaos with exponential modulation
        trig_chaos = np.sum(np.sin(10 * x_norm) * np.exp(-x_norm**2))
        
        # Asymmetric polynomial with cross-terms
        asym_poly = 0.0
        for i in range(self.dim):
            asym_poly += (x_norm[i]**3 + 0.5 * x_norm[i]**2 + 0.1 * x_norm[i]) * (1 + 0.1 * np.sin(i))
        
        # Multi-scale exponential decay with varying rates
        exp_decay = np.sum(np.exp(-0.1 * x_norm**2) + np.exp(-0.5 * x_norm**2) + np.exp(-2.0 * x_norm**2))
        
        # Cross-dimensional interaction with non-linear coupling
        cross_interaction = 0.0
        for i in range(self.dim - 1):
            cross_interaction += (x_norm[i]**2 + x_norm[i+1]**2) * np.sin(5 * (x_norm[i] - x_norm[i+1]))
        
        # Add noise for non-triviality
        noise = 0.001 * np.random.random()
        
        # Combine all components with carefully tuned weights
        return (0.25 * poly_chaos + 
                0.2 * rbf_sum + 
                0.15 * quat_grad + 
                0.15 * trig_chaos + 
                0.1 * asym_poly + 
                0.1 * exp_decay + 
                0.05 * cross_interaction + 
                noise)