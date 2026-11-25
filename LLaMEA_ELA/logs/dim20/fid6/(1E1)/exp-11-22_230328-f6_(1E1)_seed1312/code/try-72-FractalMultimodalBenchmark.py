import numpy as np

class FractalMultimodalBenchmark:
    def __init__(self, dim):
        self.dim = dim
        # Precompute fractal parameters for different dimensions
        self.fractal_dims = np.linspace(1.2, 2.8, min(dim, 10))
        if dim > 10:
            self.fractal_dims = np.concatenate([self.fractal_dims, np.full(dim - 10, 2.8)])
    
    def f(self, x):
        # Normalize input to [-1, 1] range
        x_norm = x / 5.0
        
        # Fractal radial component with varying fractal dimensions
        r = np.sqrt(np.sum(x_norm**2))
        fractal_radial = np.sum([
            np.sin((i + 1) * np.pi * r) * np.exp(-((i + 1) * r)**(self.fractal_dims[i % len(self.fractal_dims)]))
            for i in range(min(self.dim, 20))
        ])
        
        # Multi-scale sinusoidal modulation with varying frequencies and amplitudes
        scale_mod = 0.0
        for i in range(self.dim):
            freq = (i + 1) * 3.0
            amp = 1.0 / (1.0 + 0.1 * (i + 1))
            scale_mod += amp * np.sin(freq * x_norm[i]) * np.cos(freq * x_norm[i] * 0.5)
        
        # Local optima density variation using a chaotic logistic map
        density_factor = 1.0
        for i in range(min(self.dim, 15)):
            logistic_input = 3.8 * (x_norm[i % self.dim] + 0.5) % 1.0
            density_factor *= (1.0 + 0.3 * np.sin(20 * logistic_input))
        
        # Cross-dimensional coupling with power-law interactions
        cross_coupling = 0.0
        for i in range(self.dim - 1):
            diff = x_norm[i] - x_norm[i + 1]
            cross_coupling += np.abs(diff) ** (1.5 + 0.2 * np.sin(i))
        
        # Global scaling with dimension-dependent factor
        global_scale = 1.0 + 0.5 * np.sin(self.dim * 0.3)
        
        # Combine all components
        result = global_scale * (fractal_radial + scale_mod + cross_coupling) * density_factor
        
        # Add a small noise term for increased complexity
        noise = 0.01 * np.random.rand()
        
        return result + noise