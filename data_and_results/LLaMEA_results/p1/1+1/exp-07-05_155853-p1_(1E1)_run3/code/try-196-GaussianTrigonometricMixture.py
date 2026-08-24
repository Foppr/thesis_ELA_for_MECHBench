import numpy as np

class GaussianTrigonometricMixture:
    def __init__(self, dim):
        self.dim = dim
        # Precompute correlation matrix for adaptive weighting
        self.corr_matrix = np.random.rand(dim, dim) * 0.5 + 0.25
        self.corr_matrix = (self.corr_matrix + self.corr_matrix.T) / 2
        np.fill_diagonal(self.corr_matrix, 1.0)
    
    def f(self, x):
        # Ensure x is within bounds
        x = np.clip(x, -5.0, 5.0)
        
        # Gaussian mixture components with adaptive covariance
        gaussian_sum = 0
        num_components = min(8, self.dim)
        for i in range(num_components):
            center = -4.0 + 8.0 * (i / max(1, num_components - 1))
            variance = 0.5 + 0.5 * np.sin(i * 0.6)
            exponent = -0.5 * np.sum(((x - center) ** 2) / variance)
            gaussian_sum += np.exp(exponent)
        
        # Trigonometric wave interference patterns
        wave_sum = 0
        for i in range(self.dim):
            freq = 1.0 + 0.3 * np.sin(i * 0.5)
            wave_sum += np.sin(freq * x[i]) * np.cos(freq * x[i]) + 0.5 * np.sin(2.0 * freq * x[i])
        
        # Multi-scale periodic components with varying amplitudes
        periodic_sum = 0
        for i in range(self.dim):
            scale = 1.0 + 0.5 * np.sin(i * 0.3)
            periodic_sum += scale * (np.sin(x[i]) + 0.3 * np.cos(3.0 * x[i]) + 0.1 * np.sin(5.0 * x[i]))
        
        # Adaptive correlation-based interaction terms
        corr_interaction = 0
        for i in range(self.dim):
            for j in range(i+1, self.dim):
                corr_interaction += self.corr_matrix[i, j] * np.sin(x[i] - x[j]) * np.cos(x[i] + x[j])
        
        # Cross-dimensional coupling with dynamic weights
        coupling_sum = 0
        for i in range(self.dim - 1):
            weight = 0.5 + 0.5 * np.cos(i * 0.4)
            coupling_sum += weight * (x[i] * x[i+1] + 0.5 * (x[i]**2 + x[i+1]**2))
        
        # Adaptive polynomial terms with chaotic exponents
        poly_sum = 0
        for i in range(self.dim):
            exp_factor = 1.0 + 0.4 * np.sin(i * 0.7)
            poly_sum += 0.01 * x[i]**(3 + int(exp_factor * 2)) + 0.02 * x[i]**(2 + int(exp_factor))
        
        # Phase-shifted harmonic components for enhanced ruggedness
        phase_sum = 0
        for i in range(self.dim):
            phase = 0.2 * np.sin(i * 0.8) + 0.1 * np.cos(i * 0.6)
            phase_sum += np.sin(x[i] + phase) * np.cos(x[i] + phase) * (1.0 + 0.1 * np.sin(x[i]))
        
        # Global scaling and combination of all components
        return 1.2 * gaussian_sum + 0.8 * wave_sum + 0.6 * periodic_sum + 0.4 * corr_interaction + 0.3 * coupling_sum + 0.2 * poly_sum + 0.1 * phase_sum