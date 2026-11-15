import numpy as np

class MultimodalBenchmark:
    def __init__(self, dim):
        self.dim = dim
        self.global_min = 0.0
        
    def f(self, x):
        # Normalize input to [-1, 1] range
        x_norm = x / 5.0
        
        # Quadratic base with conditioning
        quadratic = np.sum(x_norm**2)
        
        # Nested sinusoidal modulations with varying frequencies and amplitudes
        nested_sine = 0.0
        for i in range(self.dim):
            for j in range(i+1, self.dim):
                nested_sine += np.sin(10 * (x_norm[i] + x_norm[j])) * np.cos(5 * (x_norm[i] - x_norm[j]))
        
        # Polynomial chaos with mixed exponents and cross-terms
        poly_chaos = np.sum(0.5 * x_norm**6 + 0.3 * x_norm**5 + 0.2 * x_norm**4 + 0.1 * x_norm**3)
        
        # Multi-scale radial basis functions with varying widths and centers
        rbf_total = 0.0
        centers = np.linspace(-1, 1, 5)
        widths = [0.5, 1.0, 1.5, 2.0, 2.5]
        for c, w in zip(centers, widths):
            rbf_total += np.sum(np.exp(-w * (x_norm - c)**2))
        
        # Chaotic saddle point component using coupled logistic maps
        chaotic_saddle = 0.0
        if self.dim > 1:
            for i in range(self.dim - 1):
                chaotic_saddle += np.sin(20 * x_norm[i]) * np.cos(15 * x_norm[i+1]) * np.tan(0.5 * x_norm[i] * x_norm[i+1])
        
        # Multi-scale exponential decay with varying rates
        exp_decay = np.sum(np.exp(-x_norm**2) + 0.5 * np.exp(-0.5 * x_norm**2) + 0.3 * np.exp(-0.2 * x_norm**2))
        
        # Cross-dimensional interaction with higher-order coupling
        interaction = np.sum(x_norm[:-1]**3 * x_norm[1:]**3)
        
        # Add noise for non-triviality
        noise = 0.001 * np.random.random()
        
        # Combine all components with carefully tuned weights
        return (0.2 * quadratic + 
                0.3 * nested_sine + 
                0.2 * poly_chaos + 
                0.15 * rbf_total + 
                0.1 * chaotic_saddle + 
                0.05 * exp_decay + 
                0.05 * interaction + 
                noise)