import numpy as np

class PolynomialChaosAttractionLandscape:
    def __init__(self, dim):
        self.dim = dim
        # Precompute polynomial chaos coefficients for different degrees
        self.poly_coeffs = np.random.randn(10, dim) * 0.5
        
    def f(self, x):
        # Normalize input to [-1, 1] range
        x_norm = x / 5.0
        
        # Polynomial chaos expansion with mixed degrees
        chaos_sum = 0
        for i in range(min(10, self.dim * 2)):
            poly_term = 1.0
            for j in range(self.dim):
                degree = (i + j) % 5 + 1  # Varying degrees
                poly_term *= np.polynomial.hermite.hermval(x_norm[j], [0]*degree + [1]) / (degree + 1)
            chaos_sum += self.poly_coeffs[i, 0] * poly_term
            
        # Gradient-based attraction fields with repulsion zones
        attraction = 0
        for i in range(self.dim):
            # Attraction towards multiple centers
            center_attraction = 0
            for c in range(3):
                center = np.sin(c * np.pi / 3) * 0.5
                dist = abs(x_norm[i] - center)
                center_attraction += np.exp(-dist**2 / 0.1) * (1 + 0.5 * np.sin(c * x_norm[i]))
            attraction += center_attraction
            
        # Spectral decomposition with frequency modulation
        spectral = 0
        for i in range(self.dim):
            freq = 2 + np.sin(x_norm[i] * np.pi)
            spectral += np.sin(freq * x_norm[i]) * np.cos(2 * x_norm[i]) * (1 + 0.3 * np.cos(x_norm[i]**2))
            
        # Cross-dimensional coupling with nonlinear interaction weights
        coupling = 0
        for i in range(self.dim):
            for j in range(i+1, self.dim):
                if j < self.dim:
                    dist = np.abs(x_norm[i] - x_norm[j])
                    weight = 1 / (1 + dist**2)
                    coupling += weight * np.sin(5 * dist) * np.cos(3 * x_norm[i]) * np.sin(2 * x_norm[j])
                    
        # High-order polynomial mixing with exponential scaling
        poly_mix = 0
        for i in range(self.dim):
            poly_mix += (x_norm[i]**7 - 3*x_norm[i]**5 + 3*x_norm[i]**3 - x_norm[i]) * np.exp(-x_norm[i]**2)
            
        # Add conditioning through higher-order terms and noise
        conditioning = 0.1 * np.sum(x_norm**6) + 0.05 * np.sum(np.sin(10 * x_norm)**2)
        
        # Fractal-like interaction with recursive scaling
        fractal = 0
        for i in range(self.dim):
            scale_factor = 0.5**(i+1)
            fractal += scale_factor * np.sin(2**i * x_norm[i]) * np.cos(3**i * x_norm[i])
            
        # Combine all components with dynamic weighting
        result = 0.3 * chaos_sum + 0.25 * attraction + 0.2 * spectral + \
                 0.15 * coupling + 0.05 * poly_mix + 0.05 * fractal
        
        return result + conditioning