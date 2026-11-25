import numpy as np

class HybridChaoticRBFBenchmark:
    def __init__(self, dim):
        self.dim = dim
        # Initialize adaptive conditioning parameters
        self.conditioning_factors = np.random.uniform(0.5, 2.0, dim)
        self.oscillation_frequencies = np.random.uniform(1.0, 10.0, dim)
        self.rbf_centers = np.random.uniform(-3.0, 3.0, (dim, dim))
        self.rbf_widths = np.random.uniform(0.5, 2.0, dim)
        
    def f(self, x):
        # Normalize input to [-1, 1] range
        x_norm = x / 5.0
        
        # Sinusoidal oscillation component with adaptive frequencies
        sin_term = 0.0
        for i in range(self.dim):
            freq = self.oscillation_frequencies[i]
            sin_term += np.sin(freq * x_norm[i]) * np.cos(freq * x_norm[i]) * self.conditioning_factors[i]
        
        # Radial basis function component with adaptive widths and centers
        rbf_term = 0.0
        for i in range(self.dim):
            center = self.rbf_centers[i]
            width = self.rbf_widths[i]
            rbf_term += np.exp(-0.5 * np.sum(((x_norm - center) / width) ** 2)) * (1.0 + 0.2 * np.sin(x_norm[i]))
        
        # Cross-dimension coupling with chaotic interaction
        coupling_term = 0.0
        for i in range(self.dim):
            for j in range(i+1, self.dim):
                coupling_strength = np.sin(np.pi * (i + j) / self.dim) * (1.0 + 0.3 * np.cos(x_norm[i] * x_norm[j]))
                coupling_term += coupling_strength * np.exp(-0.1 * (x_norm[i] - x_norm[j])**2)
        
        # Adaptive conditioning with time-like parameter
        adaptive_term = 0.0
        time_param = np.sum(x_norm) * 0.1
        for i in range(self.dim):
            adaptive_term += self.conditioning_factors[i] * np.exp(-0.2 * (x_norm[i] - time_param)**2)
        
        # Fractal-like scaling with multi-resolution structure
        fractal_term = 0.0
        scales = [1, 2, 3, 4]
        for scale in scales:
            if scale <= self.dim:
                fractal_term += np.sum(np.sin(scale * x_norm) * np.cos(scale * x_norm) * 
                                     np.exp(-0.1 * scale * np.abs(x_norm)))
        
        # Combine all terms with dynamic weighting
        combined = sin_term + rbf_term + coupling_term + adaptive_term + fractal_term
        
        # Add chaotic noise and bias
        noise = 0.02 * np.random.uniform(-1, 1) * (1.0 + 0.1 * np.sin(np.sum(x_norm)))
        bias = 0.5 * np.sum(np.sin(x_norm) * np.cos(x_norm))
        
        return combined + noise + bias