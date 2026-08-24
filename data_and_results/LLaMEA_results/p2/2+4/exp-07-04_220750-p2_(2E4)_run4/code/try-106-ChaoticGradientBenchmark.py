import numpy as np

class ChaoticGradientBenchmark:
    def __init__(self, dim):
        self.dim = dim
        self.global_min = 0.0
        self.bounds = type('Bounds', (), {'lb': np.full(dim, -5.0), 'ub': np.full(dim, 5.0)})()
    
    def f(self, x):
        # Normalize input to [-1, 1] range
        x_norm = x / 5.0
        
        # Enhanced radial component with chaotic modulation and polynomial scaling
        r = np.sqrt(np.sum(x_norm**2))
        radial_component = np.sum(np.tanh(3 * x_norm) * (1 + 0.5 * np.sin(5 * r * np.pi) * np.cos(3 * r * np.pi)))
        
        # Coupled oscillators with adaptive frequencies and chaotic coupling
        harmonic_sum = 0.0
        for i in range(self.dim):
            for j in range(i+1, self.dim):
                freq_i = 2**(i % 4 + 1)
                freq_j = 2**(j % 4 + 1)
                coupling = np.sin(x_norm[i] * x_norm[j] * freq_i * np.pi) * np.cos(x_norm[i] * x_norm[j] * freq_j * np.pi)
                coupling *= np.exp(-0.2 * (x_norm[i]**2 + x_norm[j]**2))
                harmonic_sum += coupling
        
        # Exponentially decaying sinusoidal terms with chaotic modulation and varying amplitudes
        decay_sine = 0.0
        for i in range(self.dim):
            freq = 4**(i % 6 + 1)
            amp = 1.0 + 0.3 * np.sin(7 * i * np.pi)
            decay_sine += amp * np.exp(-0.3 * r**2) * np.sin(freq * x_norm[i] * np.pi) * np.cos(3 * x_norm[i] * np.pi)
        
        # Chaotic gradient component using tent map with enhanced nonlinearity
        tent_mod = 0.0
        for i in range(self.dim):
            tent_input = 2.5 * (x_norm[i] + 0.2) % 1.0
            tent_mod += np.sin(tent_input * 10 * np.pi) * np.cos(x_norm[i] * 5 * np.pi) * np.tanh(3 * x_norm[i])
        
        # Cross-dimensional exponential coupling with enhanced chaotic interaction
        cross_exp = 0.0
        for i in range(self.dim):
            for j in range(i+1, self.dim):
                cross_exp += np.tanh(x_norm[i] * x_norm[j]) * np.exp(-0.3 * (x_norm[i]**2 + x_norm[j]**2)) * np.sin(4 * x_norm[i] * x_norm[j])
        
        # Polynomial interaction with chaotic modulation and enhanced coupling
        poly_interaction = 0.0
        for i in range(self.dim):
            for j in range(i+1, self.dim):
                poly_interaction += (x_norm[i]**4 + x_norm[j]**4) * np.sin(3 * x_norm[i] * x_norm[j]) * np.cos(x_norm[i] * x_norm[j])
        
        # Enhanced trigonometric coupling with adaptive oscillation and chaotic modulation
        trig_coupling = 0.0
        for i in range(self.dim):
            trig_coupling += np.sin(4 * x_norm[i] * np.pi) * np.cos(4 * x_norm[i] * np.pi) * np.exp(-0.2 * x_norm[i]**2) * np.tanh(4 * x_norm[i])
        
        # Additional cross-dimensional interaction with modified coupling strength and chaotic modulation
        cross_dim_interaction = 0.0
        for i in range(self.dim):
            for j in range(i+1, self.dim):
                cross_dim_interaction += np.sin(x_norm[i] * x_norm[j] * 6 * np.pi) * np.cos(x_norm[i] * x_norm[j] * 3 * np.pi) * np.exp(-0.4 * (x_norm[i]**2 + x_norm[j]**2))
        
        # Combined fitness with adjusted weighting and enhanced chaotic components
        return radial_component + 0.35 * harmonic_sum + 0.2 * decay_sine + 0.25 * tent_mod + 0.35 * cross_exp + 0.25 * poly_interaction + 0.2 * trig_coupling + 0.2 * cross_dim_interaction