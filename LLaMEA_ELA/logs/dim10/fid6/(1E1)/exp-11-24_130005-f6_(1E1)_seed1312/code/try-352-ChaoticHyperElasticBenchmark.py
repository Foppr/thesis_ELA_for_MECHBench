import numpy as np

class ChaoticHyperElasticBenchmark:
    def __init__(self, dim):
        self.dim = dim
        
    def f(self, x):
        # Scale input to [-1, 1] range
        x_scaled = x / 5.0
        
        # Hyper-elastic potential energy component with polynomial and exponential terms
        potential = 0.0
        for i in range(self.dim):
            # Polynomial potential with varying degrees and coefficients
            potential += (x_scaled[i]**4 + 0.5 * x_scaled[i]**3 + 0.3 * x_scaled[i]**2 + 
                         0.1 * np.abs(x_scaled[i]) + 0.05 * np.exp(-x_scaled[i]**2))
        
        # Multi-scale harmonic oscillation component with frequency modulation
        harmonic = 0.0
        frequencies = [1.0, 2.0, 3.0, 4.0, 5.0]
        for i in range(self.dim):
            for freq in frequencies:
                # Frequency-modulated sine waves with amplitude decay
                amp = 1.0 / (1.0 + 0.1 * np.abs(x_scaled[i]))
                harmonic += amp * np.sin(freq * x_scaled[i]) * np.cos(freq * x_scaled[i] * 0.5)
        
        # Cross-term interactions with non-linear coupling
        cross_terms = 0.0
        for i in range(self.dim):
            for j in range(i+1, min(i+4, self.dim)):
                # Non-linear interaction terms with exponential coupling
                coupling = np.exp(-0.5 * (x_scaled[i]**2 + x_scaled[j]**2))
                cross_terms += coupling * np.sin(x_scaled[i] * x_scaled[j]) * \
                              np.cos(0.5 * (x_scaled[i]**2 - x_scaled[j]**2))
        
        # Non-smooth transition regions with piecewise polynomial functions
        transitions = 0.0
        for i in range(self.dim):
            # Piecewise cubic polynomials with sharp transitions at critical points
            if x_scaled[i] < -0.3:
                transitions += (x_scaled[i] + 0.3)**3 * np.exp(-x_scaled[i]**2)
            elif x_scaled[i] > 0.3:
                transitions += (x_scaled[i] - 0.3)**3 * np.exp(-x_scaled[i]**2)
            else:
                transitions += 0.5 * x_scaled[i]**4
        
        # Fractal-like self-similarity component with recursive structure
        fractal = 0.0
        for i in range(self.dim):
            # Recursive sine-cosine combinations with diminishing amplitude
            term = np.sin(x_scaled[i]) * np.cos(x_scaled[i] * 2) * np.sin(x_scaled[i] * 3)
            fractal += term * np.exp(-0.1 * np.abs(x_scaled[i]))
        
        # Combined function with carefully balanced weights for maximum complexity
        return 1.5 * potential + 1.2 * harmonic + 0.8 * cross_terms + 0.9 * transitions + 0.7 * fractal