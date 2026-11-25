import numpy as np

class MultimodalBenchmark:
    def __init__(self, dim):
        self.dim = dim
        
    def f(self, x):
        # Normalize input to [-1, 1] range
        x_norm = x / 5.0
        
        # Base quadratic term with adaptive scaling
        f1 = np.sum(x_norm**2 * (1 + 0.1 * np.abs(x_norm)))
        
        # Chaotic sine-cosine wave structure with variable frequencies
        freqs = np.linspace(5, 15, self.dim)
        f2 = 0.4 * np.sum(np.sin(freqs * x_norm) * np.cos(freqs * x_norm))
        
        # Asymmetric quartic potentials with dynamic exponents
        exponents = 4 + 2 * np.sin(x_norm * np.pi)
        f3 = 0.3 * np.sum(np.where(x_norm > 0, x_norm**exponents, -x_norm**exponents))
        
        # Non-separable high-order polynomial interactions with dynamic weights
        poly_interaction = 0.0
        for i in range(self.dim - 1):
            weight = 0.5 * (1 + np.cos(0.5 * i))
            poly_interaction += weight * (x_norm[i]**3 + x_norm[i+1]**3)
        f4 = 0.25 * np.sum(poly_interaction)
        
        # Multi-scale fractal noise with varying amplitudes and frequencies
        f5 = 0.2 * np.sum(np.sin(25 * x_norm) + 0.5 * np.sin(75 * x_norm) + 0.25 * np.sin(225 * x_norm))
        
        # Cross-dimension coupling with dynamic exponential weights
        cross_term = 0.0
        for i in range(self.dim - 1):
            weight = np.exp(-0.3 * (i + 1)) * (1 + 0.2 * np.sin(0.5 * i))
            cross_term += weight * np.sin(25 * x_norm[i]) * np.cos(25 * x_norm[i+1])
        f6 = 0.15 * np.sum(cross_term)
        
        # Degenerate saddle points with piecewise cubic functions and adaptive scaling
        f7 = 0.15 * np.sum(np.where(x_norm > 0, x_norm**3, -x_norm**3) * (1 + 0.1 * np.abs(x_norm)))
        
        # Add controlled noise for robustness testing with dynamic amplitude
        noise_amp = 0.08 * (1 + 0.2 * np.sin(np.sum(x_norm)))
        noise = noise_amp * np.random.standard_normal(self.dim)
        f8 = 0.08 * np.sum(noise**2)
        
        # Add a global repulsion field to create degenerate optima
        repulsion = 0.1 * np.sum(1 / (1 + np.exp(-5 * x_norm)) - 0.5)
        
        return f1 + f2 + f3 + f4 + f5 + f6 + f7 + f8 + repulsion