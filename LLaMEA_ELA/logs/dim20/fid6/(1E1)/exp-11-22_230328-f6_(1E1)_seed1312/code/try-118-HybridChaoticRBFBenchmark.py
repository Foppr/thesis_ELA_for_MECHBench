import numpy as np

class HybridChaoticRBFBenchmark:
    def __init__(self, dim):
        self.dim = dim
        # Initialize adaptive conditioning parameters
        self.conditioning_factors = np.random.uniform(0.5, 2.0, dim)
        self.oscillation_frequencies = np.random.uniform(1.0, 3.0, dim)
        self.rbf_centers = np.random.uniform(-3.0, 3.0, (dim, dim))
        self.rbf_widths = np.random.uniform(0.5, 2.0, dim)
    
    def f(self, x):
        # Normalize input to [-1, 1] range
        x_norm = x / 5.0
        
        # Sinusoidal oscillation component with adaptive frequencies
        sin_term = 0.0
        for i in range(self.dim):
            freq = self.oscillation_frequencies[i]
            sin_term += np.sin(freq * x_norm[i]) * np.cos(freq * x_norm[i])
        
        # Radial Basis Function component with adaptive widths and centers
        rbf_term = 0.0
        for i in range(self.dim):
            center = self.rbf_centers[i]
            width = self.rbf_widths[i]
            rbf_term += np.exp(-0.5 * np.sum(((x_norm - center) ** 2) / (width ** 2)))
        
        # Adaptive conditioning component
        cond_term = 0.0
        for i in range(self.dim):
            cond_term += self.conditioning_factors[i] * (x_norm[i] ** 2)
        
        # Cross-dimension interaction with chaotic modulation
        cross_term = 0.0
        for i in range(self.dim):
            for j in range(i+1, self.dim):
                interaction = np.sin(np.pi * (x_norm[i] + x_norm[j])) * \
                             np.cos(np.pi * (x_norm[i] - x_norm[j]))
                cross_term += interaction * (1.0 + 0.2 * np.sin(x_norm[i] * x_norm[j]))
        
        # Fractal-like scaling with multiple resolution levels
        fractal_term = 0.0
        for scale in [1, 2, 3]:
            if scale <= self.dim:
                fractal_term += np.sum(np.sin(scale * x_norm) * np.cos(scale * x_norm))
        
        # Combine all terms with dynamic weighting
        combined = sin_term + rbf_term + cond_term + cross_term + fractal_term
        
        # Add chaotic noise and bias
        noise = 0.01 * np.random.uniform(-1, 1)
        bias = 0.5 * np.sum(np.sin(x_norm) * np.cos(x_norm))
        
        return combined + noise + bias