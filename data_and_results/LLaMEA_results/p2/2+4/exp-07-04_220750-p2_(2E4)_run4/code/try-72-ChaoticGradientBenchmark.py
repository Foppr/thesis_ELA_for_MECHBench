import numpy as np

class ChaoticGradientBenchmark:
    def __init__(self, dim):
        self.dim = dim
        self.global_min = 0.0
        self.bounds = type('Bounds', (), {'lb': np.full(dim, -5.0), 'ub': np.full(dim, 5.0)})()
    
    def f(self, x):
        # Normalize input to [-1, 1] range
        x_norm = x / 5.0
        
        # Hyperbolic tangent radial component with chaotic scaling
        r = np.sqrt(np.sum(x_norm**2))
        tanh_radial = np.sum(np.tanh(3 * x_norm) * (1 + 0.5 * np.sin(5 * r * np.pi)))
        
        # Coupled harmonic oscillators with exponential decay
        harmonic_sum = 0.0
        for i in range(self.dim):
            for j in range(i+1, self.dim):
                coupling = np.sin(x_norm[i] * x_norm[j] * 2 * np.pi) * np.exp(-0.1 * (x_norm[i]**2 + x_norm[j]**2))
                harmonic_sum += coupling
        
        # Exponentially decaying sinusoidal terms with varying frequencies
        decay_sine = 0.0
        for i in range(self.dim):
            freq = 2**(i % 4 + 1)
            decay_sine += np.exp(-0.3 * r**2) * np.sin(freq * x_norm[i] * np.pi)
        
        # Chaotic gradient component using logistic map modulation
        logistic_mod = 0.0
        for i in range(self.dim):
            logistic_input = 3.8 * (x_norm[i] + 0.1) % 1.0
            logistic_mod += np.sin(logistic_input * 10 * np.pi) * np.cos(x_norm[i] * 5 * np.pi)
        
        # Cross-dimensional exponential coupling with hyperbolic tangent
        cross_exp = 0.0
        for i in range(self.dim):
            for j in range(i+1, self.dim):
                cross_exp += np.tanh(x_norm[i] * x_norm[j]) * np.exp(-0.2 * (x_norm[i]**2 + x_norm[j]**2))
        
        # Additional multimodal component with polynomial interactions
        poly_interaction = 0.0
        for i in range(self.dim):
            for j in range(i+1, self.dim):
                poly_interaction += (x_norm[i]**3 + x_norm[j]**3) * np.sin(3 * x_norm[i] * x_norm[j])
        
        # Enhanced trigonometric coupling with adaptive oscillation
        trig_coupling = 0.0
        for i in range(self.dim):
            trig_coupling += np.sin(2 * x_norm[i] * np.pi) * np.cos(2 * x_norm[i] * np.pi) * np.exp(-0.1 * x_norm[i]**2)
        
        # Additional chaotic component with fractional Brownian motion-like behavior
        fbm_component = 0.0
        for i in range(self.dim):
            fbm_component += np.sin(x_norm[i] * np.pi * 3) * np.cos(x_norm[i] * np.pi * 2) * np.exp(-0.15 * r**2)
        
        # Combined fitness with adaptive weighting
        return tanh_radial + 0.3 * harmonic_sum + 0.2 * decay_sine + 0.15 * logistic_mod + 0.25 * cross_exp + 0.2 * poly_interaction + 0.1 * trig_coupling + 0.15 * fbm_component