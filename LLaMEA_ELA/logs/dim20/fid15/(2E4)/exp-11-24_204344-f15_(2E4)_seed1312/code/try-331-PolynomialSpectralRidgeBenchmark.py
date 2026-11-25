import numpy as np

class PolynomialSpectralRidgeBenchmark:
    def __init__(self, dim):
        self.dim = dim
        # Precompute spectral coefficients for different dimensions
        self.spectral_coeffs = np.random.uniform(-1, 1, (dim, 10))
        self.ridge_centers = np.random.uniform(-4.5, 4.5, (dim, 5))
        self.ridge_widths = np.random.uniform(0.5, 2.0, (dim, 5))
    
    def f(self, x):
        x = np.array(x)
        
        # Polynomial chaos expansion component with Hermite polynomials
        chaos_term = 0.0
        for i in range(self.dim):
            poly_val = 1.0
            for j in range(10):
                if j == 0:
                    poly_val = 1.0
                elif j == 1:
                    poly_val = x[i]
                else:
                    # Hermite polynomial recursion
                    poly_val = (x[i] * self.spectral_coeffs[i][j-1] - (j-1) * self.spectral_coeffs[i][j-2])
                chaos_term += self.spectral_coeffs[i][j] * poly_val
        
        # Spectral decomposition with frequency mixing and phase modulation
        spectral_term = 0.0
        for i in range(self.dim):
            freq = 1.0 + 3.0 * np.sin(i * 0.5)
            phase = 0.5 * np.cos(i * 0.3)
            spectral_term += np.sin(freq * x[i] + phase) * np.cos(freq * x[i] * 0.7 + phase * 1.2)
        
        # Adaptive ridge structure with dynamic curvature and position
        ridge_term = 0.0
        for i in range(self.dim):
            for j in range(5):
                center = self.ridge_centers[i][j]
                width = self.ridge_widths[i][j]
                curvature = 1.0 + 2.0 * np.sin(i * 0.4 + j * 0.3)
                ridge_term += np.exp(-0.5 * ((x[i] - center) / (width * curvature)) ** 2) * curvature
        
        # Cross-dimensional coupling with interaction weights
        coupling_term = 0.0
        for i in range(self.dim):
            for j in range(i+1, self.dim):
                weight = 0.5 + 0.5 * np.sin(i * j * 0.2 + self.dim * 0.1)
                coupling_term += weight * np.sin(x[i] + x[j]) * np.cos(x[i] - x[j])
        
        # Dynamic conditioning with dimensionality-dependent scaling
        condition_factor = 1.0 + 0.5 * np.sin(self.dim * 0.3) + 0.3 * np.cos(self.dim * 0.4)
        
        # Multi-peak attraction with varying strengths and positions
        peak_term = 0.0
        for i in range(self.dim):
            strength = 2.0 + 1.5 * np.sin(i * 0.6)
            position = -3.0 + 6.0 * np.cos(i * 0.5)
            width = 0.8 + 0.4 * np.sin(i * 0.7)
            peak_term += strength * np.exp(-0.5 * ((x[i] - position) / width) ** 2)
        
        # Final combination with dynamic weighting
        total = 0.25 * chaos_term + 0.2 * spectral_term + 0.25 * ridge_term + 0.15 * coupling_term + 0.15 * peak_term
        
        return total * condition_factor