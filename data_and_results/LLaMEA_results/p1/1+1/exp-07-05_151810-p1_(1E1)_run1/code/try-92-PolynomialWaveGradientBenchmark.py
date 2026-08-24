import numpy as np

class PolynomialWaveGradientBenchmark:
    def __init__(self, dim):
        self.dim = dim
        # Precompute polynomial chaos coefficients
        self.poly_coeffs = np.random.randn(dim, 5) * 0.5
        # Precompute wave interference patterns
        self.wave_freqs = np.random.uniform(1.0, 4.0, dim)
        self.wave_amps = np.random.uniform(0.5, 2.0, dim)
        # Precompute gradient field parameters
        self.grad_mags = np.random.uniform(0.1, 1.5, dim)
        self.grad_dirs = np.random.randn(dim, dim)
        self.grad_dirs = self.grad_dirs / np.linalg.norm(self.grad_dirs, axis=1, keepdims=True)
        
    def f(self, x):
        # Ensure x is within bounds
        x = np.clip(x, -5.0, 5.0)
        
        # Polynomial chaos expansion component
        poly_component = 0.0
        for i in range(self.dim):
            x_i = x[i]
            coeffs = self.poly_coeffs[i]
            poly_val = coeffs[0] + coeffs[1] * x_i + coeffs[2] * x_i**2 + coeffs[3] * x_i**3 + coeffs[4] * x_i**4
            poly_component += poly_val
        
        # Trigonometric wave interference component
        wave_component = 0.0
        for i in range(self.dim):
            freq = self.wave_freqs[i]
            amp = self.wave_amps[i]
            wave_component += amp * np.sin(freq * x[i]) * np.cos(freq * x[i])
        
        # Adaptive gradient field component
        grad_component = 0.0
        for i in range(self.dim):
            grad_mag = self.grad_mags[i]
            grad_dir = self.grad_dirs[i]
            # Dot product of gradient direction and position
            grad_proj = np.dot(grad_dir, x)
            grad_component += grad_mag * np.exp(-0.5 * grad_proj**2)
        
        # Cross-term coupling between dimensions
        coupling = 0.0
        for i in range(self.dim):
            for j in range(i+1, self.dim):
                coupling += 0.3 * np.sin(2.0 * x[i]) * np.cos(2.0 * x[j]) * np.exp(-0.1 * (x[i] - x[j])**2)
        
        # Global sinusoidal modulation
        global_mod = 1.0 + 0.5 * np.sin(0.5 * np.sum(x**2))
        
        # Combine all components
        result = poly_component + wave_component + grad_component + coupling * global_mod
        
        return result