import numpy as np

class MultimodalBenchmark:
    def __init__(self, dim):
        self.dim = dim
        self.global_min = 0.0
        
    def f(self, x):
        # Normalize input to [-1, 1] range
        x_norm = x / 5.0
        
        # Fractal component with recursive self-similarity
        fractal = 0.0
        for i in range(1, 6):
            scale = 2 ** i
            fractal += np.sum(np.sin(scale * x_norm) * np.cos(scale * x_norm) * np.exp(-0.1 * scale * np.abs(x_norm)))
        
        # Complex gradient field with multiple directional components
        grad_field = np.sum(np.sin(10 * x_norm) * np.cos(15 * x_norm) + 
                           0.5 * np.sin(20 * x_norm) * np.cos(25 * x_norm) + 
                           0.3 * np.sin(30 * x_norm) * np.cos(35 * x_norm))
        
        # Scale-invariant polynomial interactions
        poly_scale = 0.0
        for i in range(1, 4):
            poly_scale += np.sum(x_norm[:-i]**(2*i) * x_norm[i:]**(2*i) + 
                               0.5 * x_norm[:-i]**(3*i) * x_norm[i:]**(3*i))
        
        # Multi-scale radial basis functions with varying bandwidths
        rbf_scale = 0.0
        for i, (center, bandwidth) in enumerate(zip([0.1, -0.3, 0.5, -0.7], [2.0, 3.0, 1.5, 2.5])):
            rbf_scale += np.sum(np.exp(-bandwidth * (x_norm - center)**2))
        
        # Chaotic coupling between dimensions with fractal-like behavior
        chaotic_coupling = 0.0
        if self.dim > 1:
            for i in range(self.dim - 1):
                chaotic_coupling += np.sin(50 * np.sin(x_norm[i]) * np.cos(x_norm[i+1])) * \
                                  np.cos(40 * np.cos(x_norm[i]) * np.sin(x_norm[i+1]))
        
        # High-frequency oscillatory component with amplitude modulation
        oscillatory = np.sum(np.sin(100 * x_norm) * np.cos(120 * x_norm) * 
                            (1 + 0.1 * np.sin(50 * x_norm)))
        
        # Asymmetric polynomial with mixed exponents
        asym_poly = np.sum(np.abs(x_norm)**3.5 * np.sign(x_norm) + 
                          0.3 * np.abs(x_norm)**4.2 * np.sign(x_norm))
        
        # Cross-dimensional interaction with fractal scaling
        cross_interaction = 0.0
        if self.dim > 2:
            for i in range(self.dim - 2):
                cross_interaction += np.sin(15 * x_norm[i] * x_norm[i+1] * x_norm[i+2]) * \
                                   np.cos(12 * x_norm[i] * x_norm[i+1] * x_norm[i+2]) * \
                                   np.exp(-0.05 * (x_norm[i]**2 + x_norm[i+1]**2 + x_norm[i+2]**2))
        
        # Add noise for non-triviality
        noise = 0.001 * np.random.random()
        
        # Combine all components with carefully tuned weights
        return (0.2 * fractal + 
                0.15 * grad_field + 
                0.12 * poly_scale + 
                0.1 * rbf_scale + 
                0.08 * chaotic_coupling + 
                0.06 * oscillatory + 
                0.05 * asym_poly + 
                0.04 * cross_interaction + 
                noise)