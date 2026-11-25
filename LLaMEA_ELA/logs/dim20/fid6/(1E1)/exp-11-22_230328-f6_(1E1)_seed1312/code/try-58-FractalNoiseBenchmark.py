import numpy as np

class FractalNoiseBenchmark:
    def __init__(self, dim):
        self.dim = dim
        # Precompute fractal parameters for different dimensions
        self.fractal_dims = np.linspace(1.2, 2.8, min(10, dim))
        
    def f(self, x):
        # Normalize input to [-1, 1] range
        x_norm = x / 5.0
        
        # Fractal radial component with varying dimensionality
        r = np.sqrt(np.sum(x_norm**2))
        fractal_radial = np.exp(-r**2) * np.sin(r * 10) * np.cos(r * 5)
        
        # Multi-scale fractal structure using self-similarity
        fractal_structure = 0.0
        for i in range(min(5, self.dim)):
            scale = 2**(i - 2)
            freq = 2**(i + 1)
            fractal_structure += np.sin(scale * x_norm[i] * freq) * np.cos(scale * x_norm[i] * freq)
        
        # Adaptive noise component that changes based on position
        noise_amp = 0.3 * (1 + 0.5 * np.sin(r * 3))
        adaptive_noise = noise_amp * np.random.normal(0, 0.1, self.dim)
        noise_component = np.sum(adaptive_noise**2)
        
        # Cross-dimensional coupling with exponential decay
        cross_coupling = 0.0
        for i in range(self.dim - 1):
            cross_coupling += np.exp(-0.5 * (x_norm[i] - x_norm[i+1])**2) * np.sin(3 * (x_norm[i] + x_norm[i+1]))
        
        # Asymmetric basin structure with multiple local minima
        basin_term = 0.0
        for i in range(min(8, self.dim)):
            offset = 0.5 * np.sin(i * np.pi / 4)
            basin_term += (x_norm[i] - offset)**2 * (1 + 0.3 * np.cos(5 * x_norm[i]))
        
        # Global scaling with dimension-dependent factor
        dim_factor = 1.0 + 0.2 * np.log(self.dim + 1)
        
        return dim_factor * (fractal_radial + fractal_structure + noise_component + 
                           cross_coupling + basin_term) + 0.1 * np.sum(x_norm**4)