import numpy as np

class MultimodalBenchmark:
    def __init__(self, dim):
        self.dim = dim
        np.random.seed(42)
        self.rbf_centers = np.random.uniform(-5, 5, (4, dim))
        self.rbf_widths = np.random.uniform(0.5, 2.0, 4)
        self.poly_coeffs = np.random.uniform(-1, 1, (3, dim))
        self.oscillation_freqs = np.random.uniform(1.0, 6.0, dim)
        self.scale_factors = np.random.uniform(0.5, 2.0, dim)
    
    def f(self, x):
        x = np.clip(x, -5.0, 5.0)
        f_val = 0.0
        
        # Quadratic base
        f_val += np.sum(x**2) * 0.1
        
        # Sinusoidal oscillations with dynamic frequencies
        for i in range(self.dim):
            f_val += 0.5 * np.sin(self.oscillation_freqs[i] * x[i]) * np.cos(2 * x[i])
        
        # Polynomial chaos terms with variable scaling
        for i in range(self.dim):
            f_val += self.poly_coeffs[0, i] * x[i]**3 + self.poly_coeffs[1, i] * x[i]**4 + self.poly_coeffs[2, i] * x[i]**5
        
        # Radial basis functions with dynamic centers and widths
        for i in range(4):
            dist = np.sum((x - self.rbf_centers[i])**2)
            f_val += 0.3 * np.exp(-self.rbf_widths[i] * dist) * np.sin(3 * np.sum(x - self.rbf_centers[i]))
        
        # Cross-variable interaction with dynamic scaling
        for i in range(self.dim):
            for j in range(i+1, self.dim):
                f_val += 0.2 * np.sin(self.scale_factors[i] * x[i]) * np.cos(self.scale_factors[j] * x[j]) * np.exp(-0.1 * (x[i] - x[j])**2)
        
        # Global multimodal modulation
        f_val += 0.25 * np.sin(0.5 * np.sum(x**2)) * np.cos(0.3 * np.sum(x**2)) * np.exp(-0.02 * np.sum(x**2))
        
        return f_val