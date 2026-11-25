import numpy as np

class PolynomialRBFMixtureBenchmark:
    def __init__(self, dim):
        self.dim = dim
        # Precompute polynomial chaos coefficients and RBF centers
        self.poly_coeffs = np.random.randn(5, dim) * 0.5
        self.rbf_centers = np.random.uniform(-4.0, 4.0, (3, dim))
        self.rbf_widths = np.random.uniform(0.5, 2.0, 3)
        # Spectral filtering parameters
        self.filter_freqs = np.linspace(0.1, 3.0, min(dim, 10))
        
    def f(self, x):
        # Scale input to [-5, 5]
        x = np.clip(x, -5.0, 5.0)
        
        # Polynomial chaos expansion component
        poly_chaos = 0.0
        for i in range(5):
            term = 1.0
            for j in range(self.dim):
                term *= np.polyval(self.poly_coeffs[i, j], x[j])
            poly_chaos += term
        
        # Radial basis function coupling
        rbf_coupling = 0.0
        for i in range(3):
            dist_sq = np.sum((x - self.rbf_centers[i])**2)
            rbf_coupling += np.exp(-dist_sq / (2 * self.rbf_widths[i]**2))
        
        # Spectral band filtering with cosine modulation
        spectral_filter = 0.0
        for i in range(min(self.dim, 10)):
            freq = self.filter_freqs[i]
            spectral_filter += np.cos(freq * x[i % self.dim]) * \
                              np.sin(0.5 * freq * x[(i + 1) % self.dim])
        
        # Multi-scale polynomial valleys with varying steepness
        valley_structure = 0.0
        for i in range(self.dim):
            # Create a combination of quadratic and quartic terms with varying coefficients
            coeff_quad = 0.5 + 0.3 * np.sin(0.3 * i)
            coeff_quart = 0.1 + 0.05 * np.cos(0.4 * i)
            valley_structure += coeff_quad * x[i]**2 + coeff_quart * x[i]**4
        
        # Enhanced coupling between dimensions using cross-polynomial terms
        cross_coupling = 0.0
        for i in range(self.dim - 1):
            cross_coupling += (x[i]**2 * x[i+1] + x[i] * x[i+1]**2) * \
                             np.exp(-0.1 * (x[i]**2 + x[i+1]**2))
        
        # Fractal-like dimension scaling with exponential modulation
        fractal_scaling = 0.0
        for i in range(self.dim):
            modulator = np.exp(-0.2 * i)
            fractal_scaling += (np.abs(x[i])**1.5 + np.abs(x[i])**2.5) * modulator
        
        # High-frequency oscillatory component with amplitude modulation
        high_freq = 0.0
        for i in range(self.dim):
            freq = 8.0 + 2.0 * np.sin(0.7 * i)
            amp_mod = 1.0 + 0.3 * np.cos(0.5 * i)
            high_freq += amp_mod * np.sin(freq * x[i]) * np.cos(0.3 * freq * x[i])
        
        # Isolated local minima with varying depths and positions
        isolated_minima = 0.0
        for i in range(self.dim):
            # Create a mixture of sine and cosine based local minima
            minima_pos = -4.0 + 8.0 * np.random.rand()
            isolated_minima += (np.sin(3 * (x[i] - minima_pos)) * 
                               np.cos(2 * (x[i] - minima_pos)) + 
                               0.5 * np.sin(5 * (x[i] - minima_pos)))
        
        # Combined objective with carefully tuned weights
        return 0.8 * poly_chaos + 1.2 * rbf_coupling + 0.9 * spectral_filter + \
               1.5 * valley_structure + 0.7 * cross_coupling + 1.0 * fractal_scaling + \
               1.3 * high_freq + 0.6 * isolated_minima