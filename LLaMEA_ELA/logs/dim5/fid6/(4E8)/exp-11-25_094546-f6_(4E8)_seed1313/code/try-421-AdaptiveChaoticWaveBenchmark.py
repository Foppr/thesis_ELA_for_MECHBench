import numpy as np

class AdaptiveChaoticWaveBenchmark:
    def __init__(self, dim):
        self.dim = dim
        
    def f(self, x):
        # Normalize input to [-1, 1] range
        x_norm = x / 5.0
        
        result = 0.0
        for i in range(self.dim):
            xi = x_norm[i]
            
            # Base quadratic term with adaptive curvature
            base = 0.5 * xi**2 * (1.0 + 0.3 * np.sin(self.dim * 0.5 + i * 0.4))
            
            # Sinusoidal modulations with dynamic frequencies and amplitudes
            sin_terms = 0.0
            for k in range(1, 10):
                freq = k * (1.0 + 0.2 * np.sin(i * 0.3 + k * 0.2))
                amp = 1.0 / k * (1.0 + 0.1 * np.cos(i * 0.5 + k * 0.1))
                phase = k * 0.5 + 0.2 * np.sin(i * 0.4 + k * 0.3)
                sin_terms += amp * np.sin(freq * xi + phase)
            
            # Radial basis function interactions with adaptive sigma
            rbf_terms = 0.0
            for j in range(max(0, i-2), min(self.dim, i+3)):
                if i != j:
                    distance = abs(xi - x_norm[j])
                    sigma = 0.3 + 0.2 * np.sin(i * 0.4 + j * 0.5)
                    rbf_terms += np.exp(-0.5 * (distance/sigma)**2) * np.cos(3 * xi + 2 * x_norm[j])
            
            # Chaotic perturbation with logistic map modulation
            chaotic_factor = 1.0 + 0.2 * np.sin(xi * 7.0 + i * 0.6)
            for k in range(5):
                chaotic_factor *= (1.0 - 0.1 * np.sin(xi * 3.0 + i * 0.4 + k * 0.2))
            
            # Multi-scale interference pattern
            interference = 0.4 * np.sin(8 * xi + i * 0.3) + 0.3 * np.cos(12 * xi + i * 0.2) + 0.2 * np.sin(16 * xi + i * 0.1)
            
            # Dimensional coupling term
            coupling = 0.0
            for j in range(self.dim):
                if i != j:
                    coupling += (xi - x_norm[j])**3 * np.cos(xi + x_norm[j])
            
            # Combine all terms with adaptive weights
            result += base + sin_terms + rbf_terms + coupling + interference
            
        # Global scaling and noise injection
        global_scale = 1.0 + 0.2 * np.sin(self.dim * 0.7) + 0.1 * np.cos(self.dim * 0.3)
        noise = 0.02 * np.sum(np.sin(x_norm * 8.0 + self.dim * 0.1))
        
        return (global_scale * result / self.dim) + noise