import numpy as np

class MultimodalBenchmark:
    def __init__(self, dim):
        self.dim = dim
        self.global_min = 0.0
        
    def f(self, x):
        # Normalize input to [-1, 1] range
        x_norm = x / 5.0
        
        # Nested sinusoidal components with varying frequencies and amplitudes
        nested_sin = 0.0
        for i in range(1, 6):
            nested_sin += (1.0 / i) * np.sin(i * np.pi * x_norm)
            nested_sin += (0.5 / i) * np.cos(i * np.pi * x_norm)
        
        # Polynomial chaos with mixed exponents and cross-terms
        poly_chaos = np.sum(x_norm**4 + 0.5 * x_norm**3 + 0.3 * x_norm**2 + 0.1 * x_norm)
        
        # Cross-dimensional coupling with fractal-like behavior
        cross_coupling = 0.0
        if self.dim > 1:
            for i in range(self.dim - 1):
                cross_coupling += np.sin(10 * (x_norm[i]**2 + x_norm[i+1]**2)) * \
                                 np.cos(5 * (x_norm[i] * x_norm[i+1]))
        
        # Multi-scale radial basis functions with varying centers and widths
        rbf_scale = 0.0
        centers = np.linspace(-0.8, 0.8, 5)
        widths = np.linspace(0.5, 2.0, 5)
        for center, width in zip(centers, widths):
            rbf_scale += np.sum(np.exp(-width * (x_norm - center)**2))
        
        # Asymmetric polynomial with mixed exponents
        asym_poly = np.sum(np.abs(x_norm)**3.5 * np.sign(x_norm) + 0.5 * x_norm**4)
        
        # Fractal-like self-similarity component
        fractal = 0.0
        for i in range(1, 4):
            fractal += np.sin(2**(i+1) * x_norm) * np.cos(3**(i+1) * x_norm)
        
        # High-frequency oscillation with amplitude modulation
        high_freq_mod = np.sum(np.sin(50 * x_norm) * np.exp(-x_norm**2) + 
                              np.cos(40 * x_norm) * np.exp(-0.5 * x_norm**2))
        
        # Add noise for non-triviality
        noise = 0.001 * np.random.random()
        
        # Combine all components with carefully tuned weights
        return (0.3 * nested_sin + 
                0.2 * poly_chaos + 
                0.15 * cross_coupling + 
                0.15 * rbf_scale + 
                0.1 * asym_poly + 
                0.05 * fractal + 
                0.03 * high_freq_mod + 
                noise)