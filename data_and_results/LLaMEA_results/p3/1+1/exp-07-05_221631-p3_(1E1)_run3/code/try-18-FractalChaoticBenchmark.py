import numpy as np

class FractalChaoticBenchmark:
    def __init__(self, dim):
        self.dim = dim
        np.random.seed(42)
        # Precompute coefficients for chaotic behavior
        self.coeffs = np.random.uniform(0.5, 2.0, dim)
        self.phase_shifts = np.random.uniform(0, 2 * np.pi, dim)
        self.fractal_dims = np.random.uniform(0.1, 0.9, dim)
        
    def f(self, x):
        x = np.clip(x, -5.0, 5.0)
        
        # Initialize function value
        f_val = 0.0
        
        # Exponential decay terms with chaotic modulation
        for i in range(self.dim):
            x_i = x[i]
            # Chaotic modulation using sine and cosine
            mod = np.sin(self.coeffs[i] * x_i + self.phase_shifts[i]) * \
                  np.cos(self.coeffs[i] * x_i + self.phase_shifts[i] * 1.5)
            f_val += np.exp(-0.1 * np.abs(x_i)) * mod
            
        # Logarithmic spiral components
        for i in range(self.dim - 1):
            x_i, x_i1 = x[i], x[i+1]
            # Spiral pattern in 2D subspace
            r = np.sqrt(x_i**2 + x_i1**2)
            theta = np.arctan2(x_i1, x_i)
            spiral = np.sin(3 * theta + 0.5 * r) * np.cos(2 * theta - 0.3 * r)
            f_val += 0.5 * spiral
            
        # Self-similar fractal terms
        for i in range(self.dim):
            x_i = x[i]
            # Nested fractal pattern with multiple scales
            fractal_term = 0.0
            for scale in [0.1, 0.3, 0.7, 1.0]:
                fractal_term += np.sin(scale * x_i) * np.cos(scale * x_i) * \
                                np.sin(scale**2 * x_i) * np.cos(scale**2 * x_i)
            f_val += 0.3 * fractal_term
            
        # Add a global scaling factor and noise
        f_val *= 1.0 + 0.1 * np.random.rand()
        f_val += 0.01 * np.sum(x**6)
        
        # Ensure positive fitness
        f_val = max(f_val, 1e-8)
        
        return f_val