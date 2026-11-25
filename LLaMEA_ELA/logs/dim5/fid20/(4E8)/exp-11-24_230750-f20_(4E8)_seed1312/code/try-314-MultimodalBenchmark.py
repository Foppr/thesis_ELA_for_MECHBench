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
            for depth in range(1, 5):  # Increased recursion depth
                modulated_x = np.sin(modulated_x * (2 ** depth)) + 0.1 * modulated_x
            fractal += modulated_x ** 2
        
        # Dynamic Gaussian peak clustering with time-varying centers and widths
        gaussian_peaks = 0.0
        num_clusters = min(7, self.dim)  # Increased number of clusters
        for i in range(num_clusters):
            center = 5.0 * np.sin(i * np.pi / num_clusters)
            width = 1.0 + 0.3 * np.cos(i * np.pi / num_clusters)  # Reduced width variation
            amplitude = 2.5 + 0.8 * np.sin(i * np.pi / (num_clusters + 1))  # Increased amplitude
            gaussian_peaks += amplitude * np.exp(-0.5 * ((x[i % self.dim] - center) ** 2) / (width ** 2))
        
        # Cross-dimensional polynomial couplings with varying interaction degrees
        poly_coupling = 0.0
        for i in range(self.dim):
            for j in range(i+1, min(i+5, self.dim)):  # Increased coupling range
                degree = 3 + (i % 2)  # Changed degree pattern
                poly_coupling += (x[i] ** degree + x[j] ** degree) * np.cos(2 * (x[i] - x[j]))  # Different frequency
        
        # Adaptive conditioning through variable scaling factors
        conditioning = 0.0
        for i in range(self.dim):
            scale_factor = 1.0 + 0.7 * np.sin(x[i])  # Increased scaling factor
            conditioning += scale_factor * (x[i] ** 4) * np.cos(3 * x[i])  # Changed frequency
        
        # Deceptive gradient components via asymmetric trigonometric mixing
        deception = 0.0
        for i in range(self.dim):
            asym_term = np.sin(x[i]) * np.cos(x[i]) + 0.4 * np.sin(4 * x[i])  # Increased asymmetry
            weight = 1.0 + 0.3 * np.cos(x[i])  # Increased weight variation
            deception += weight * asym_term ** 3
        
        # Combine all components with modified weights
        return 0.25 * fractal + 0.3 * gaussian_peaks + 0.18 * poly_coupling + 0.17 * conditioning + 0.1 * deception