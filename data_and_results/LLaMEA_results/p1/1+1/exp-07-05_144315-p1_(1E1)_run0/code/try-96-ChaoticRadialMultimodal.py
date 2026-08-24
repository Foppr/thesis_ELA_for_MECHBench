import numpy as np

class ChaoticRadialMultimodal:
    def __init__(self, dim):
        self.dim = dim
        
    def f(self, x):
        # Ensure x is within bounds
        x = np.clip(x, -5.0, 5.0)
        
        # Radial component with chaotic modulation
        r = np.sqrt(np.sum(x**2))
        radial = r * np.exp(-0.1 * r) * (1.0 + 0.3 * np.sin(10 * r))
        
        # Multiple Gaussian peaks with chaotic centers
        peaks = 0.0
        for i in range(12):
            center = np.random.rand(self.dim) * 10 - 5  # Random center in [-5, 5]
            peaks += 0.5 * np.exp(-0.5 * np.sum((x - center)**2)) * np.sin(2 * np.pi * np.sum(x - center))
        
        # Cross-dimensional interaction terms
        cross = 0.0
        for i in range(self.dim):
            for j in range(i+1, self.dim):
                cross += np.sin(3 * x[i]) * np.cos(5 * x[j]) * np.exp(-0.05 * (x[i]**2 + x[j]**2))
        
        # Sine wave components with varying frequencies and amplitudes
        sine_terms = 0.0
        for i in range(1, 6):
            sine_terms += (1.0 / i) * np.sin(i * np.sum(x)) * np.cos(i * r)
        
        # Polynomial and exponential interactions
        poly_exp = 0.0
        for i in range(self.dim):
            poly_exp += x[i]**3 * np.exp(-0.02 * x[i]**2) + x[i]**4 * np.exp(-0.01 * x[i]**2)
        
        # Chaotic modulation with logistic map
        chaotic = 0.0
        for i in range(self.dim):
            chaotic += np.sin(20 * x[i]) * np.cos(15 * x[i]) * np.exp(-0.03 * x[i]**2)
        
        # Hyperbolic tangent and exponential interaction
        tanh_exp = 0.0
        for i in range(self.dim):
            tanh_exp += np.tanh(x[i]) * np.exp(-0.05 * x[i]**2)
        
        # Fractional power and sinusoidal combination
        frac_sin = 0.0
        for i in range(self.dim):
            frac_sin += (np.abs(x[i])**1.7) * np.sin(4 * x[i])
        
        # Final combination with adjusted weights
        return radial + 0.7 * peaks + 0.5 * cross + 0.6 * sine_terms + 0.4 * poly_exp + 0.3 * chaotic + 0.25 * tanh_exp + 0.3 * frac_sin