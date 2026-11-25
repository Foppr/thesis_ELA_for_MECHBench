import numpy as np

class MultimodalBenchmark:
    def __init__(self, dim):
        self.dim = dim
        
    def f(self, x):
        # Normalize input to [-1, 1] range
        x_norm = x / 5.0
        
        # Base quadratic term
        f1 = np.sum(x_norm**2)
        
        # Chaotic sine-cosine wave structure with dynamic frequencies
        freqs = np.linspace(5, 25, self.dim)
        f2 = 0.4 * np.sum(np.sin(freqs * x_norm) * np.cos(freqs * x_norm))
        
        # Asymmetric quartic potentials with adaptive exponents
        exponents = np.linspace(3, 7, self.dim)
        f3 = 0.3 * np.sum(np.where(x_norm > 0, x_norm**exponents, -x_norm**exponents))
        
        # Non-separable high-order polynomial interactions with dynamic coupling
        poly_interaction = 0.0
        for i in range(self.dim - 1):
            poly_interaction += (x_norm[i]**5 + x_norm[i+1]**5) * np.exp(-0.15 * (i + 1))
        f4 = 0.25 * np.sum(poly_interaction)
        
        # Multi-scale fractal noise with varying amplitudes and frequencies
        f5 = 0.2 * np.sum(np.sin(30 * x_norm) + np.sin(90 * x_norm) + np.sin(270 * x_norm))
        
        # Cross-dimension coupling with dynamic exponential weights and phase shifts
        cross_term = 0.0
        for i in range(self.dim - 1):
            phase_shift = np.sin(0.5 * i)
            cross_term += np.exp(-0.25 * (i + 1)) * np.sin(40 * x_norm[i] + phase_shift) * np.cos(40 * x_norm[i+1] + phase_shift)
        f6 = 0.15 * np.sum(cross_term)
        
        # Degenerate saddle points with piecewise cubic functions and dynamic scaling
        f7 = 0.15 * np.sum(np.where(x_norm > 0, x_norm**3, -x_norm**3))
        
        # Dynamic repulsion field creating multiple degenerate optima
        repulsion_field = 0.0
        for i in range(self.dim):
            repulsion_field += np.exp(-0.3 * (x_norm[i]**2)) * np.sin(15 * x_norm[i])
        f8 = 0.2 * np.sum(repulsion_field)
        
        # Adaptive noise scaling based on dimensionality and fitness landscape
        noise_scale = 0.1 / (1.0 + np.exp(-0.5 * np.sum(x_norm**2)))
        noise = noise_scale * np.random.standard_normal(self.dim)
        f9 = 0.08 * np.sum(noise**2)
        
        # Additional high-frequency chaotic component
        f10 = 0.1 * np.sum(np.sin(100 * x_norm) * np.cos(100 * x_norm))
        
        return f1 + f2 + f3 + f4 + f5 + f6 + f7 + f8 + f9 + f10