import numpy as np

class PolynomialSpectralAdaptiveBenchmark:
    def __init__(self, dim):
        self.dim = dim
        # Precompute spectral coefficients for adaptive conditioning
        self.spectral_coeffs = np.random.randn(dim, 4)
        self.polynomial_coeffs = np.random.randn(dim, 3)
        
    def f(self, x):
        x = np.array(x)
        
        # Polynomial chaos expansion component with adaptive weights
        poly_term = 0.0
        for i in range(self.dim):
            coeffs = self.polynomial_coeffs[i]
            poly_term += coeffs[0] * x[i]**2 + coeffs[1] * x[i]**3 + coeffs[2] * x[i]**4
        
        # Spectral decomposition with frequency modulation
        spec_term = 0.0
        for i in range(self.dim):
            freq_mod = 1.0 + 0.5 * np.sin(i * 0.7 + self.dim * 0.3)
            amp_mod = 0.8 + 0.4 * np.cos(i * 0.6 + self.dim * 0.2)
            spec_term += amp_mod * np.sin(freq_mod * x[i]) * np.cos(freq_mod * x[i] * 0.5)
        
        # Adaptive conditioning layer with dynamic scaling
        cond_term = 0.0
        for i in range(self.dim):
            scale_factor = 1.0 + 0.3 * np.sin(i * 0.8 + self.dim * 0.4)
            cond_term += scale_factor * (x[i] ** 2) * np.exp(-0.1 * x[i] ** 2)
        
        # Coupled oscillatory fields with phase shifts
        osc_term = 0.0
        for i in range(self.dim):
            for j in range(i+1, self.dim):
                phase_shift = np.sin(i * 0.5 + j * 0.3) * np.cos(i * 0.4 + j * 0.6)
                osc_term += np.sin(x[i] + x[j] + phase_shift) * np.cos(x[i] - x[j] + phase_shift)
        
        # Multi-scale Gaussian peaks with varying amplitudes and positions
        peak_term = 0.0
        for i in range(self.dim):
            amp = 2.0 + 3.0 * np.sin(i * 0.9)
            width = 0.5 + 1.5 * np.cos(i * 0.8)
            pos = -3.0 + 6.0 * np.sin(i * 0.7)
            peak_term += amp * np.exp(-0.5 * ((x[i] - pos) / width) ** 2)
        
        # Gradient-enhanced radial component with non-uniform distribution
        grad_radial = 0.0
        for i in range(self.dim):
            center = -2.0 + 4.0 * np.sin(i * 0.6)
            width = 0.3 + 0.8 * np.cos(i * 0.5)
            grad_radial += (x[i] - center) ** 2 * np.exp(-0.5 * ((x[i] - center) / width) ** 2)
        
        # Chaotic component with enhanced nonlinearity
        chaotic_term = 0.0
        for i in range(self.dim):
            chaotic_term += np.sin(x[i] * (1 + 0.1 * np.sin(i * 0.3))) * np.cos(x[i] * (1 + 0.1 * np.cos(i * 0.4)))
        
        # Final weighted combination with dynamic balance
        total = 0.25 * poly_term + 0.2 * spec_term + 0.15 * cond_term + 0.12 * osc_term + 0.1 * peak_term + 0.08 * grad_radial + 0.1 * chaotic_term
        
        # Global modulation with chaotic component
        global_mod = 1.0 + 0.2 * np.sin(np.sum(x) * 0.3 + self.dim * 0.5)
        
        return total * global_mod