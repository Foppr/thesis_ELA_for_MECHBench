import numpy as np

class MultimodalBenchmark:
    def __init__(self, dim):
        self.dim = dim
        
    def f(self, x):
        # Scale input to [-1, 1] range
        x_scaled = x / 5.0
        
        # Polynomial chaos expansion terms with varying degrees
        poly_terms = np.sum((x_scaled**2 + 0.1) * (x_scaled**4 + 0.2 * x_scaled**2 + 0.05))
        
        # Radial basis functions with dynamic scaling based on dimension
        rbfs = np.sum(np.exp(-0.5 * np.sum((x_scaled[:, np.newaxis] - np.linspace(-1, 1, self.dim))**2, axis=0) / (0.3 + 0.1 * np.sqrt(self.dim))))
        
        # Sine-cosine coupling with dynamic frequency modulation
        freq_mod = 3.0 + 0.5 * np.sin(np.pi * self.dim / 10.0)
        trig_coupling = np.sum(np.sin(freq_mod * x_scaled) * np.cos(freq_mod * x_scaled**3))
        
        # Multi-scale exponential interactions with varying decay rates
        exp_interaction = np.sum(np.exp(-2.0 * np.abs(x_scaled)) * (1.0 + 0.5 * np.sin(4.0 * x_scaled)))
        
        # Chaotic modulation using logistic map dynamics
        chaotic = np.sum(np.sin(10.0 * np.sin(x_scaled) * np.cos(x_scaled)) * np.exp(-0.5 * x_scaled**2))
        
        # Combined function with diverse curvature and multiple local minima
        return 2.0 * poly_terms + 1.5 * rbfs + 0.8 * trig_coupling + 0.4 * exp_interaction + 0.3 * chaotic