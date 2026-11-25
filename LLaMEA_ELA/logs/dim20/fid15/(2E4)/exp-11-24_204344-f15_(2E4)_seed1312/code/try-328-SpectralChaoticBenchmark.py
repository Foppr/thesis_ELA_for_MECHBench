import numpy as np

class SpectralChaoticBenchmark:
    def __init__(self, dim):
        self.dim = dim
        # Precompute spectral coefficients for chaos generation
        self.spectral_coeffs = np.random.randn(dim, 5)
    
    def f(self, x):
        x = np.array(x)
        
        # Polynomial chaos expansion with adaptive weights
        chaos_poly = 0.0
        for i in range(self.dim):
            for j in range(5):
                chaos_poly += self.spectral_coeffs[i, j] * np.polynomial.hermite.hermval(x[i], [0]*j + [1])
        
        # Spectral decomposition using discrete cosine transform components
        dct_components = np.fft.dct(x, type=2, norm='ortho')
        spectral_term = np.sum(dct_components ** 2 * np.exp(-0.1 * np.arange(len(dct_components))))
        
        # Adaptive noise injection with dynamic amplitude modulation
        noise_amp = 0.5 + 0.5 * np.sin(self.dim * 0.3)
        adaptive_noise = noise_amp * np.random.randn() * np.exp(-0.5 * np.sum(x**2))
        
        # Multi-scale radial basis with varying influence
        radial_sum = 0.0
        for i in range(self.dim):
            scale = 1.0 + 0.5 * np.sin(i * 0.7)
            center = -4.0 + 8.0 * np.random.rand()
            width = 0.5 + 0.5 * np.cos(i * 0.4)
            radial_sum += np.exp(-0.5 * ((x[i] - center) / (width * scale)) ** 2)
        
        # Coupling terms with directional sensitivity
        coupling = 0.0
        for i in range(self.dim):
            for j in range(i+1, self.dim):
                coupling += np.sin(x[i] * x[j]) * np.cos(x[i] + x[j]) * (1.0 + 0.2 * np.sin(i - j))
        
        # Nonlinear transformation with dynamic exponent
        transformed = np.zeros(self.dim)
        for i in range(self.dim):
            exp_factor = 1.5 + 0.5 * np.cos(i * 0.6)
            transformed[i] = np.sign(x[i]) * np.abs(x[i]) ** exp_factor
        
        # Final landscape combining all components
        total = 0.4 * chaos_poly + 0.3 * spectral_term + 0.1 * adaptive_noise + \
                0.1 * radial_sum + 0.05 * coupling + 0.05 * np.sum(transformed**2)
        
        # Global conditioning factor
        cond_factor = 1.0 + 0.3 * np.sin(self.dim * 0.4) * np.cos(self.dim * 0.2)
        
        return total * cond_factor