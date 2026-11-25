import numpy as np

class PolynomialChaosRadialBenchmark:
    def __init__(self, dim):
        self.dim = dim
        # Precompute chaos polynomials for different dimensions
        self.chaos_coeffs = np.random.randn(dim, 5)
        
    def f(self, x):
        # Normalize to [-1, 1]
        x_norm = x / 5.0
        
        # Polynomial chaos expansion component
        chaos = 0.0
        for i in range(self.dim):
            poly_val = 0.0
            for j in range(5):
                poly_val += self.chaos_coeffs[i, j] * np.polynomial.hermite.hermval(x_norm[i], [0]*j + [1])
            chaos += poly_val**2
        
        # Stochastic radial basis function component
        rb = 0.0
        for i in range(self.dim):
            center = np.sin(i * 0.5) * 0.8 + 0.2
            width = 0.3 + 0.4 * np.random.rand()
            rb += np.exp(-0.5 * ((x_norm[i] - center) / width)**2)
        
        # Cross-dimensional coupling with varying strength
        coupling = 0.0
        for i in range(self.dim):
            for j in range(i+1, min(i+4, self.dim)):  # Limited coupling
                strength = 0.5 + 0.5 * np.sin(i * 0.3 + j * 0.2)
                coupling += strength * np.sin(3 * (x_norm[i] - x_norm[j])) * np.cos(2 * (x_norm[i] + x_norm[j]))
        
        # Fractional polynomial interaction terms
        frac_poly = 0.0
        for i in range(self.dim):
            for j in range(i+1, self.dim):
                frac_poly += (x_norm[i]**1.5) * (x_norm[j]**2.5) * np.sin(0.5 * (i + j))
        
        # Multi-scale sinusoidal modulation
        mod = 0.0
        for i in range(self.dim):
            freq = 2.0 + 3.0 * np.sin(i * 0.4)
            amp = 0.1 + 0.3 * np.cos(i * 0.3)
            mod += amp * np.sin(freq * x_norm[i]) * np.cos(freq * x_norm[i])
        
        # Add noise with chaotic behavior
        noise = 0.0
        for i in range(self.dim):
            r = 3.8 + 0.1 * np.sin(i)
            x_prev = 0.5 + 0.1 * np.random.rand()
            for _ in range(3):
                x_prev = r * x_prev * (1 - x_prev)
            noise += np.sin(10 * x_norm[i] + x_prev) * np.log(1.0 + 0.2 * x_norm[i]**2)
        
        # Combine all components with dynamic weights
        return (0.3 * chaos + 0.25 * rb + 0.2 * coupling + 
                0.15 * frac_poly + 0.08 * mod + 0.02 * noise)