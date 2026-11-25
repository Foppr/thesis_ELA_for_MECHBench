import numpy as np

class MultimodalBenchmark:
    def __init__(self, dim):
        self.dim = dim
        
    def f(self, x):
        # Normalize input to [-1, 1] range
        x_norm = x / 5.0
        
        # Gaussian radial basis components with varying widths and centers
        gaussian_terms = []
        for i in range(10):
            center = np.sin(i * 0.5) * np.ones(self.dim)
            width = 0.5 + 0.3 * np.cos(i * 0.3)
            gauss = np.exp(-np.sum(((x_norm - center) / width) ** 2))
            gaussian_terms.append(gauss)
        
        # Sum of Gaussian terms with varying amplitudes
        gaussian_component = np.sum(np.array(gaussian_terms) * (1 + 0.2 * np.sin(np.arange(10))))
        
        # Sinusoidal modulation with multiple frequencies and phase shifts
        sin_modulation = np.sum(np.sin(5 * x_norm + np.pi * np.arange(self.dim) / self.dim) *
                               np.cos(3 * x_norm + np.pi * np.arange(self.dim) / (self.dim * 2)))
        
        # Cross-dimensional polynomial coupling with mixed degrees
        poly_coupling = 0.0
        for i in range(self.dim):
            j = (i + 1) % self.dim
            k = (i + 2) % self.dim
            poly_coupling += x_norm[i] ** 3 * x_norm[j] ** 2 + x_norm[i] ** 2 * x_norm[k] ** 3
        
        # Chaotic sine-wave distortion with frequency modulation
        chaotic_distortion = 0.0
        for i in range(self.dim):
            freq = 2 + 3 * np.sin(x_norm[i] * 0.7)
            chaotic_distortion += np.sin(freq * x_norm[i]) * np.cos(freq * x_norm[i])
        
        # Fractional power interaction with exponential decay
        fractional_term = np.sum(np.abs(x_norm) ** 1.5 * np.exp(-0.1 * np.abs(x_norm)))
        
        # Combined function with adaptive weights and noise-like perturbations
        return (0.3 * gaussian_component + 
                0.25 * sin_modulation + 
                0.2 * poly_coupling + 
                0.15 * chaotic_distortion + 
                0.1 * fractional_term)