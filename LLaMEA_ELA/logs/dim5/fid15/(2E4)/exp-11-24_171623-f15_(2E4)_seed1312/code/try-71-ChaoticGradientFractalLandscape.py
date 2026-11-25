import numpy as np

class ChaoticGradientFractalLandscape:
    def __init__(self, dim):
        self.dim = dim
        # Initialize chaotic parameters for gradient dynamics
        self.chaotic_params = np.random.rand(dim) * 0.1 + 0.05
        # Fractal dimension scaling
        self.fractal_dims = [np.log2(i + 2) for i in range(dim)]
        
    def f(self, x):
        # Normalize to [-1, 1]
        x_norm = x / 5.0
        
        # Chaotic gradient component with fractal scaling
        chaotic_grad = 0.0
        for i in range(self.dim):
            scaled_x = x_norm[i] * self.fractal_dims[i % len(self.fractal_dims)]
            # Chaotic sine-based gradient influence
            chaotic_term = np.sin(scaled_x * self.chaotic_params[i % len(self.chaotic_params)]) * \
                          np.cos(scaled_x**2 * self.chaotic_params[i % len(self.chaotic_params)]**2)
            chaotic_grad += chaotic_term
        
        # Embedded fractal patterns using recursive cosine
        fractal_pattern = 0.0
        for i in range(self.dim):
            pos = x_norm[i]
            # Multi-scale fractal cosine pattern
            for scale in [1, 2, 3]:
                fractal_pattern += np.cos(pos * scale * self.fractal_dims[i % len(self.fractal_dims)]) * \
                                  np.exp(-scale * (pos**2))
        
        # Adaptive conditioning based on dimensionality
        conditioning = 0.0
        for i in range(self.dim):
            # Dimension-specific conditioning with exponential scaling
            conditioning += (i + 1) * np.exp(-x_norm[i]**2) * np.sin(x_norm[i] * np.pi)
        
        # Multi-modal peaks with varying amplitudes and widths
        multimodal = 0.0
        num_peaks = min(8, self.dim)
        for i in range(num_peaks):
            peak_pos = np.sin(i * np.pi / num_peaks) * 0.8
            amplitude = 1.0 / (i + 1)
            width = 0.5 / (i + 1)
            distance = x_norm[i % self.dim] - peak_pos
            multimodal += amplitude * np.exp(-distance**2 / (2 * width**2))
        
        # Cross-dimensional coupling with asymmetric interaction
        cross_coupling = 0.0
        for i in range(self.dim):
            for j in range(i+1, min(i+4, self.dim)):
                diff = x_norm[i] - x_norm[j]
                # Asymmetric coupling: different influence based on dimension order
                asym_factor = (i + 1) / (j + 1)
                cross_coupling += diff**2 * np.exp(-abs(diff)) * asym_factor
        
        # Basin connectivity with polynomial attraction fields
        basin_attraction = 0.0
        for i in range(self.dim):
            # Create varying basin depths
            basin_depth = 1.0 + np.sin(i * np.pi / self.dim) * 0.5
            basin_attraction += basin_depth * (x_norm[i]**4 - 2*x_norm[i]**2)
        
        # Combine all components with dynamic weights
        result = 0.25 * chaotic_grad + 0.3 * fractal_pattern + 0.15 * conditioning + \
                 0.15 * multimodal + 0.1 * cross_coupling + 0.05 * basin_attraction
        
        # Add global conditioning through higher-order polynomial
        global_conditioning = 0.01 * np.sum(np.abs(x_norm)**4)
        
        return result + global_conditioning