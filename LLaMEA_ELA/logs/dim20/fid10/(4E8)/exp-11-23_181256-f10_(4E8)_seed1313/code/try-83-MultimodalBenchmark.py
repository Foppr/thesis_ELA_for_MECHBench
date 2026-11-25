import numpy as np

class MultimodalBenchmark:
    def __init__(self, dim):
        self.dim = dim
        
    def f(self, x):
        # Scale input to [-1, 1] range
        x_scaled = x / 5.0
        
        # Gaussian radial basis functions with varying widths and centers
        gaussian_terms = []
        centers = np.linspace(-1, 1, min(5, self.dim))
        for i, center in enumerate(centers):
            if i < len(x_scaled):
                width = 0.5 + 0.3 * np.sin(i)
                gaussian_terms.append(np.exp(-width * (x_scaled[i] - center)**2))
        
        # Quaternion-inspired rotational symmetry with complex angular coupling
        rotation_symmetry = 0
        for i in range(0, self.dim - 1, 2):
            if i + 1 < self.dim:
                xi, yi = x_scaled[i], x_scaled[i+1]
                rotation_symmetry += (xi**2 + yi**2) * np.sin(3 * np.arctan2(yi, xi))
        
        # Adaptive noise term that changes based on position and dimensionality
        noise_amplitude = 0.1 * (1 + 0.5 * np.sin(self.dim))
        adaptive_noise = np.sum(noise_amplitude * np.random.randn(self.dim) * (1 + 0.2 * x_scaled**2))
        
        # Multi-scale polynomial interactions with exponential modulation
        poly_interaction = 0
        for i in range(self.dim):
            poly_interaction += (x_scaled[i]**5 + 0.7 * x_scaled[i]**3 + 0.3 * x_scaled[i]) * np.exp(-0.1 * i)
        
        # Clustered minima with distance-dependent attraction
        cluster_penalty = 0
        for i in range(0, self.dim - 2, 3):
            if i + 2 < self.dim:
                xi, yi, zi = x_scaled[i], x_scaled[i+1], x_scaled[i+2]
                dist = np.sqrt(xi**2 + yi**2 + zi**2)
                cluster_penalty += 0.5 * np.exp(-dist) * np.sin(4 * dist)
        
        # Combined function with diverse curvature and multiple interacting components
        return (np.sum(gaussian_terms) + 0.8 * rotation_symmetry + 
                0.3 * adaptive_noise + 0.6 * poly_interaction + 
                0.4 * cluster_penalty + 0.1 * np.sum(x_scaled**4))