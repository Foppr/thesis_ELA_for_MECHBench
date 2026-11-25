import numpy as np

class FractalPolynomialBenchmark:
    def __init__(self, dim):
        self.dim = dim
        # Precompute polynomial chaos coefficients
        self.chaos_coeffs = np.random.randn(dim, 5) * 0.5
        
    def f(self, x):
        # Normalize input to [-1, 1] range
        x_norm = x / 5.0
        
        # Fractal Brownian motion component with Hurst parameter
        fbm = 0.0
        hurst = 0.3 + 0.4 * np.sin(self.dim * np.pi / 8.0)
        for i in range(self.dim):
            # Simple fractal-like behavior using fractional noise
            fbm += (x_norm[i] ** 2) * np.sin(10 * x_norm[i]) * np.cos(5 * x_norm[i])
        
        # Polynomial chaos expansion with adaptive degree
        chaos = 0.0
        for i in range(self.dim):
            poly_vals = np.array([x_norm[i]**j for j in range(5)])
            chaos += np.dot(self.chaos_coeffs[i], poly_vals)
        
        # Quantum-inspired tunneling effect with probabilistic barrier penetration
        tunneling = 0.0
        for i in range(self.dim - 1):
            xi = x_norm[i]
            xi1 = x_norm[i + 1]
            # Tunneling probability based on potential energy difference
            potential_diff = (xi**2 - 1)**2 + (xi1**2 - 1)**2
            tunnel_prob = np.exp(-potential_diff / 0.5)
            tunneling += tunnel_prob * np.sin(xi * xi1 * 10)
        
        # Cross-dimensional coupling with spectral filtering
        spectral_coupling = 0.0
        for i in range(self.dim):
            # Apply frequency-domain coupling
            freq_component = np.sin(2 * np.pi * x_norm[i] * (i + 1))
            spectral_coupling += freq_component * np.cos(3 * np.pi * x_norm[i])
        
        # High-dimensional conditioning with exponential growth
        condition_factor = 1.0 + 0.3 * np.exp(self.dim / 5.0) + 0.2 * np.sin(self.dim * np.pi / 3.0)
        
        # Combine all terms with dynamic weighting
        total = condition_factor * (fbm + chaos + tunneling + spectral_coupling)
        
        # Add a global minimum at the origin with perturbed landscape
        global_min = np.sum(x_norm**2) * 0.1
        
        return total + global_min