import numpy as np

class RuggedMultiscaleBenchmark:
    def __init__(self, dim):
        self.dim = dim
        self.global_min = np.zeros(dim)
        
    def f(self, x):
        # Normalize input to [-1, 1] for easier computation
        x_norm = x / 5.0
        
        # Radial polynomial basin with varying exponents
        radial_term = 0
        exponents = [2, 3, 4, 5]
        for i in range(self.dim):
            if i < len(exponents):
                radial_term += 0.1 * (x_norm[i]**2 + 0.01)**exponents[i % len(exponents)]
        
        # High-frequency sinusoidal oscillations with varying amplitudes and periods
        oscillation_term = 0
        for i in range(self.dim):
            freqs = [10, 15, 20, 25]
            amps = [1.5, 1.2, 1.8, 1.0]
            for f, a in zip(freqs, amps):
                oscillation_term += a * np.sin(f * x_norm[i]) * np.cos(f * x_norm[i]**2)
        
        # Cross-dimensional coupling with exponential decay
        coupling_term = 0
        for i in range(self.dim):
            for j in range(i+1, self.dim):
                dist = np.sqrt((x_norm[i] - x_norm[j])**2 + 0.01)
                coupling_term += np.sin(30 * x_norm[i]) * np.cos(25 * x_norm[j]) * np.exp(-dist**2)
        
        # Sharp ridges and valleys using absolute value and step functions
        ridge_term = 0
        for i in range(self.dim):
            ridge_term += 0.5 * np.abs(x_norm[i])**1.5 + 0.3 * np.sin(50 * x_norm[i])
        
        # Multi-scale fractal-like perturbation
        fractal_term = 0
        for i in range(self.dim):
            fractal_term += np.sin(100 * np.sin(20 * x_norm[i])) * np.cos(80 * np.cos(15 * x_norm[i]))
        
        # Combine all terms with dimensionality-dependent weights
        result = (0.6 * radial_term + 
                 0.8 * oscillation_term + 
                 0.5 * coupling_term + 
                 0.4 * ridge_term + 
                 0.3 * fractal_term)
        
        # Add small random noise for robustness
        noise = np.random.normal(0, 0.001 * (1 + 0.05 * self.dim))
        
        return result + noise