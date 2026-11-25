import numpy as np

class FractalMultimodalBenchmark:
    def __init__(self, dim):
        self.dim = dim
        # Precompute fractal parameters
        self.fractal_dims = np.arange(1, dim + 1)
        self.scaling_factors = np.exp(-0.1 * self.fractal_dims)
        
    def f(self, x):
        # Normalize input to [-1, 1]
        x_norm = x / 5.0
        
        # Polynomial chaos expansion terms
        poly_term = np.sum((x_norm ** 4) * (1 + 0.1 * x_norm ** 2))
        
        # Radial basis function components with fractal scaling
        rbf_term = 0.0
        for i in range(self.dim):
            # Fractal-like radial basis with varying width
            width = 0.5 * np.exp(-0.05 * i)
            rbf_term += np.exp(-0.5 * np.sum(((x_norm - np.sin(i * np.pi / self.dim)) / width) ** 2))
        
        # Self-similar sinusoidal components at multiple scales
        fractal_term = 0.0
        for scale in [1, 2, 3]:
            freq = 2 ** scale
            for i in range(self.dim):
                fractal_term += np.sin(freq * x_norm[i]) * self.scaling_factors[i]
        
        # Cross-dimensional coupling with dimension-dependent strength
        cross_term = 0.0
        for i in range(self.dim):
            for j in range(i+1, min(i+4, self.dim)):  # Limited coupling
                coupling = 0.3 * (1 - np.exp(-0.2 * (j - i)))
                cross_term += coupling * np.sin(4 * x_norm[i]) * np.cos(3 * x_norm[j])
        
        # Dimension-dependent global minimum shift
        shift = 0.2 * np.log(self.dim + 1)
        shift_term = 0.5 * np.sum((x_norm - shift) ** 3)
        
        return poly_term + rbf_term + fractal_term + cross_term + shift_term