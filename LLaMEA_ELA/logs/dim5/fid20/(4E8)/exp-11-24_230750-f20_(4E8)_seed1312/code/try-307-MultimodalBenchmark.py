import numpy as np

class MultimodalBenchmark:
    def __init__(self, dim):
        self.dim = dim
    
    def f(self, x):
        # Ensure x is within bounds [-5, 5]
        x = np.clip(x, -5.0, 5.0)
        
        # Fractal-like terrain through recursive sine-wave modulations
        fractal = 0.0
        for i in range(self.dim):
            modulated_x = x[i]
            for depth in range(1, 4):
                modulated_x = np.sin(modulated_x * (2 ** depth)) + 0.1 * modulated_x
            fractal += modulated_x ** 2
        
        # Dynamic Gaussian peak clustering with time-varying centers and widths
        gaussian_peaks = 0.0
        num_clusters = min(5, self.dim)
        for i in range(num_clusters):
            center = 5.0 * np.sin(i * np.pi / num_clusters)
            width = 1.0 + 0.5 * np.cos(i * np.pi / num_clusters)
            amplitude = 2.0 + 1.0 * np.sin(i * np.pi / (num_clusters + 1))
            gaussian_peaks += amplitude * np.exp(-0.5 * ((x[i % self.dim] - center) ** 2) / (width ** 2))
        
        # Cross-dimensional polynomial couplings with varying interaction degrees
        poly_coupling = 0.0
        for i in range(self.dim):
            for j in range(i+1, min(i+4, self.dim)):
                degree = 2 + (i % 3)
                poly_coupling += (x[i] ** degree + x[j] ** degree) * np.cos(3 * (x[i] - x[j]))
        
        # Adaptive conditioning through variable scaling factors
        conditioning = 0.0
        for i in range(self.dim):
            scale_factor = 1.0 + 0.5 * np.sin(x[i])
            conditioning += scale_factor * (x[i] ** 4) * np.cos(2 * x[i])
        
        # Deceptive gradient components via asymmetric trigonometric mixing
        deception = 0.0
        for i in range(self.dim):
            asym_term = np.sin(x[i]) * np.cos(x[i]) + 0.3 * np.sin(3 * x[i])
            weight = 1.0 + 0.2 * np.cos(x[i])
            deception += weight * asym_term ** 3
        
        # Combine all components with adaptive weights
        return 0.3 * fractal + 0.25 * gaussian_peaks + 0.2 * poly_coupling + 0.15 * conditioning + 0.1 * deception