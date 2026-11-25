import numpy as np

class ChaoticFractalBenchmark:
    def __init__(self, dim):
        self.dim = dim
        
    def f(self, x):
        # Scale input to [-1, 1] range
        x_scaled = x / 5.0
        
        # Logistic map component for chaotic behavior
        logistic_term = 0.0
        r = 3.9  # Chaos parameter
        for i in range(self.dim):
            xi = x_scaled[i]
            # Apply logistic map iteratively
            for _ in range(5):
                xi = r * xi * (1.0 - xi)
            logistic_term += xi**2
        
        # Radial basis function with varying widths and centers
        rbf_term = 0.0
        centers = np.linspace(-1, 1, min(5, self.dim))
        for i in range(self.dim):
            center = centers[i % len(centers)] if self.dim > 5 else x_scaled[i]
            width = 0.5 + 0.5 * np.sin(i)
            rbf_term += np.exp(-width * (x_scaled[i] - center)**2)
        
        # Fractal-like sine-wave interactions with diminishing frequencies
        fractal_term = 0.0
        for i in range(self.dim):
            freq = 2.0**(i % 4 + 1)  # Increasing frequency
            phase = np.pi * (i / self.dim) if self.dim > 1 else 0
            fractal_term += np.sin(freq * x_scaled[i] + phase) * \
                           np.cos(freq * x_scaled[i] * 0.5 + phase * 0.7)
        
        # Cross-dimensional coupling with chaotic modulation
        cross_term = 0.0
        for i in range(self.dim):
            for j in range(i+1, min(i+3, self.dim)):  # Limited interaction
                modulator = np.sin(x_scaled[i] * x_scaled[j])
                cross_term += (np.sin(2.0 * x_scaled[i] + x_scaled[j]) * 
                              np.cos(x_scaled[i] + 2.0 * x_scaled[j]) * 
                              modulator)
        
        # Add noise-like perturbations for irregularity
        noise = np.sum(np.sin(10.0 * x_scaled) * np.cos(7.0 * x_scaled))
        
        # Combine all terms with different weights
        return 0.8 * logistic_term + 1.2 * rbf_term + 0.6 * fractal_term + \
               0.9 * cross_term + 0.3 * noise + 1.5