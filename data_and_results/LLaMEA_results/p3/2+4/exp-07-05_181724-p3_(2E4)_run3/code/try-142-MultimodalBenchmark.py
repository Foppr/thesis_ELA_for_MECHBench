import numpy as np

class MultimodalBenchmark:
    def __init__(self, dim):
        self.dim = dim
        self.global_min = 0.0
        
    def f(self, x):
        # Normalize input to [-1, 1] range
        x_norm = x / 5.0
        
        # Sinusoidal base with varying frequencies and amplitudes
        sin_term = np.sum(np.sin(10 * x_norm) * np.cos(15 * x_norm) + 
                         0.5 * np.sin(25 * x_norm) * np.cos(35 * x_norm) + 
                         0.3 * np.sin(45 * x_norm) * np.cos(55 * x_norm))
        
        # Polynomial chaos with mixed exponents
        poly_chaos = np.sum(x_norm**3 + 0.8 * x_norm**5 + 0.6 * x_norm**7 + 0.4 * x_norm**9)
        
        # Radial basis functions with varying widths and centers
        rbf = np.sum(np.exp(-5.0 * (x_norm - 0.3)**2) + 
                    0.7 * np.exp(-4.0 * (x_norm + 0.2)**2) + 
                    0.5 * np.exp(-6.0 * (x_norm - 0.7)**2) + 
                    0.3 * np.exp(-3.0 * (x_norm + 0.8)**2))
        
        # Cross-dimensional coupling using chaotic sine products
        coupling = 0.0
        if self.dim > 1:
            for i in range(self.dim - 1):
                coupling += np.sin(20 * x_norm[i]) * np.cos(25 * x_norm[i+1]) * \
                           np.sin(15 * x_norm[i] * x_norm[i+1]) + \
                           0.5 * np.cos(30 * x_norm[i]) * np.sin(35 * x_norm[i+1]) * \
                           np.cos(25 * x_norm[i] * x_norm[i+1])
        
        # Multi-scale chaotic interaction with exponential decay
        chaotic_interaction = 0.0
        if self.dim > 2:
            for i in range(self.dim - 2):
                chaotic_interaction += np.exp(-2.0 * (x_norm[i] - x_norm[i+1])**2) * \
                                     np.sin(50 * x_norm[i] * x_norm[i+1] * x_norm[i+2]) + \
                                     0.3 * np.exp(-1.5 * (x_norm[i+1] - x_norm[i+2])**2) * \
                                     np.cos(40 * x_norm[i] * x_norm[i+1] * x_norm[i+2])
        
        # Asymmetric polynomial terms with higher-order components
        asym_poly = np.sum(np.abs(x_norm)**3.5 * np.sign(x_norm) + 
                          0.4 * np.abs(x_norm)**4.5 * np.sign(x_norm) + 
                          0.2 * np.abs(x_norm)**5.5 * np.sign(x_norm))
        
        # Dimensionality-dependent scaling factor
        scale_factor = 1.0 + 0.05 * (self.dim - 1)
        
        # Add noise for non-triviality
        noise = 0.001 * np.random.random()
        
        # Combine all components with carefully tuned weights
        return (0.3 * sin_term * scale_factor + 
                0.25 * poly_chaos * scale_factor + 
                0.2 * rbf * scale_factor + 
                0.15 * coupling * scale_factor + 
                0.1 * chaotic_interaction * scale_factor + 
                0.1 * asym_poly * scale_factor + 
                noise)