import numpy as np

class MultimodalBenchmark:
    def __init__(self, dim):
        self.dim = dim
    
    def f(self, x):
        # Ensure x is within bounds [-5, 5]
        x = np.clip(x, -5.0, 5.0)
        
        # Fractal-like self-similar pattern with scaling factors
        fractal_term = 0.0
        for i in range(self.dim):
            scale = 1.0 + 0.5 * np.sin(2.0 * x[i]) * np.cos(3.0 * x[i])
            fractal_term += scale * np.sin(10.0 * x[i]) * np.cos(7.0 * x[i]) * np.exp(-0.1 * x[i]**2)
        
        # Multi-scale harmonic oscillations with adaptive frequencies
        harmonic_term = 0.0
        freqs = [1.0, 2.5, 4.0, 6.5, 8.0]
        for i in range(self.dim):
            for f in freqs:
                freq = f * (1.0 + 0.3 * np.sin(0.5 * x[i]))
                harmonic_term += np.sin(freq * x[i]) * np.cos(freq * x[i]) * np.exp(-0.05 * x[i]**2)
        
        # Adaptive noise injection with dimensionality-dependent intensity
        noise_term = 0.0
        for i in range(self.dim):
            noise_intensity = 0.1 * (1.0 + 0.2 * np.sin(1.5 * x[i]))
            noise_term += noise_intensity * np.random.normal(0, 1) * np.exp(-0.2 * x[i]**2)
        
        # Cross-dimensional coupling with geometric progression weights
        cross_term = 0.0
        for i in range(self.dim):
            for j in range(i+1, self.dim):
                weight = 0.5 * (1.0 + np.cos(0.3 * x[i] * x[j]))
                dist = np.sqrt((x[i] - x[j])**2 + 1e-6)
                cross_term += weight * np.sin(5.0 * dist) * np.exp(-0.1 * dist**2)
        
        # Non-smooth piecewise function with varying exponents
        piecewise_term = 0.0
        for i in range(self.dim):
            if np.abs(x[i]) < 2.0:
                piecewise_term += 0.3 * np.abs(x[i])**1.5 + 0.1 * np.sin(20.0 * x[i])
            else:
                piecewise_term += 0.4 * np.abs(x[i])**2.2 + 0.08 * np.cos(15.0 * x[i])
        
        # Multi-fractal energy landscape with variable dimensionality scaling
        fractal_energy = 0.0
        for i in range(self.dim):
            base = 1.0 + 0.4 * np.sin(0.7 * x[i])
            fractal_energy += base**3.0 * np.cos(2.0 * x[i]) * np.exp(-0.15 * x[i]**2)
        
        # Ridge structure with varying curvature
        ridge_term = 0.0
        for i in range(self.dim):
            ridge_term += 0.2 * np.sin(4.0 * x[i]) * np.cos(3.0 * x[i]) + 0.1 * np.sin(8.0 * x[i])
        
        return fractal_term + harmonic_term + noise_term + cross_term + piecewise_term + fractal_energy + ridge_term