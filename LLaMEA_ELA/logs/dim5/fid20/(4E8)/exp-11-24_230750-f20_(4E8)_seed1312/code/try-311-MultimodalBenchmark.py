import numpy as np

class MultimodalBenchmark:
    def __init__(self, dim):
        self.dim = dim
    
    def f(self, x):
        # Ensure x is within bounds [-5, 5]
        x = np.clip(x, -5.0, 5.0)
        
        # Fractal-like terrain through recursive sine-wave modulations with altered frequencies
        fractal = 0.0
        for i in range(self.dim):
            modulated_x = x[i]
            for depth in range(1, 5):
                modulated_x = np.sin(modulated_x * (3 ** depth)) + 0.15 * modulated_x
            fractal += modulated_x ** 2
        
        # Dynamic Gaussian peak clustering with shifted centers and modified widths
        gaussian_peaks = 0.0
        num_clusters = min(6, self.dim)
        for i in range(num_clusters):
            center = 4.5 * np.sin(i * np.pi / (num_clusters + 1))
            width = 1.2 + 0.3 * np.cos(i * np.pi / num_clusters)
            amplitude = 2.5 + 0.8 * np.sin(i * np.pi / (num_clusters + 2))
            gaussian_peaks += amplitude * np.exp(-0.5 * ((x[i % self.dim] - center) ** 2) / (width ** 2))
        
        # Cross-dimensional polynomial couplings with increased interaction degrees
        poly_coupling = 0.0
        for i in range(self.dim):
            for j in range(i+1, min(i+5, self.dim)):
                degree = 3 + (i % 4)
                poly_coupling += (x[i] ** degree + x[j] ** degree) * np.cos(2 * (x[i] - x[j]))
        
        # Adaptive conditioning through enhanced scaling factors
        conditioning = 0.0
        for i in range(self.dim):
            scale_factor = 1.5 + 0.4 * np.sin(x[i])
            conditioning += scale_factor * (x[i] ** 4) * np.cos(3 * x[i])
        
        # Deceptive gradient components via enhanced asymmetric trigonometric mixing
        deception = 0.0
        for i in range(self.dim):
            asym_term = np.sin(x[i]) * np.cos(x[i]) + 0.4 * np.sin(4 * x[i])
            weight = 1.2 + 0.3 * np.cos(x[i])
            deception += weight * asym_term ** 3
        
        # Combine all components with updated weights
        return 0.25 * fractal + 0.3 * gaussian_peaks + 0.25 * poly_coupling + 0.15 * conditioning + 0.05 * deception