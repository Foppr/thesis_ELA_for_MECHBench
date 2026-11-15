import numpy as np

class ChaoticGradientBenchmark:
    def __init__(self, dim):
        self.dim = dim
        self.global_min = 0.0
        self.bounds = type('Bounds', (), {'lb': np.full(dim, -5.0), 'ub': np.full(dim, 5.0)})()
    
    def f(self, x):
        # Normalize input to [-1, 1] range
        x_norm = x / 5.0
        
        # Enhanced hyperbolic tangent radial component with chaotic scaling
        r = np.sqrt(np.sum(x_norm**2))
        tanh_radial = np.sum(np.tanh(5 * x_norm) * (1 + 0.8 * np.sin(9 * r * np.pi)))
        
        # Coupled harmonic oscillators with exponential decay and chaotic modulation
        harmonic_sum = 0.0
        for i in range(self.dim):
            for j in range(i+1, self.dim):
                coupling = np.sin(x_norm[i] * x_norm[j] * 4 * np.pi) * np.exp(-0.2 * (x_norm[i]**2 + x_norm[j]**2))
                harmonic_sum += coupling
        
        # Exponentially decaying sinusoidal terms with varying frequencies and chaotic modulation
        decay_sine = 0.0
        for i in range(self.dim):
            freq = 4**(i % 6 + 1)
            decay_sine += np.exp(-0.5 * r**2) * np.sin(freq * x_norm[i] * np.pi) * np.cos(3 * x_norm[i] * np.pi)
        
        # Chaotic gradient component using logistic map modulation with enhanced nonlinearity
        logistic_mod = 0.0
        for i in range(self.dim):
            logistic_input = 4.0 * (x_norm[i] + 0.2) % 1.0
            logistic_mod += np.sin(logistic_input * 15 * np.pi) * np.cos(x_norm[i] * 7 * np.pi) * np.tanh(3 * x_norm[i])
        
        # Cross-dimensional exponential coupling with hyperbolic tangent and enhanced chaos
        cross_exp = 0.0
        for i in range(self.dim):
            for j in range(i+1, self.dim):
                cross_exp += np.tanh(x_norm[i] * x_norm[j]) * np.exp(-0.3 * (x_norm[i]**2 + x_norm[j]**2)) * np.sin(4 * x_norm[i] * x_norm[j])
        
        # Additional multimodal component with polynomial interactions and enhanced coupling
        poly_interaction = 0.0
        for i in range(self.dim):
            for j in range(i+1, self.dim):
                poly_interaction += (x_norm[i]**6 + x_norm[j]**6) * np.sin(5 * x_norm[i] * x_norm[j]) * np.cos(3 * x_norm[i] * x_norm[j])
        
        # Enhanced trigonometric coupling with adaptive oscillation and chaotic modulation
        trig_coupling = 0.0
        for i in range(self.dim):
            trig_coupling += np.sin(4 * x_norm[i] * np.pi) * np.cos(4 * x_norm[i] * np.pi) * np.exp(-0.2 * x_norm[i]**2) * np.tanh(4 * x_norm[i])
        
        # Additional chaotic cross-dimensional interaction with modified coupling strength
        cross_dim_interaction = 0.0
        for i in range(self.dim):
            for j in range(i+1, self.dim):
                cross_dim_interaction += np.sin(x_norm[i] * x_norm[j] * 6 * np.pi) * np.cos(x_norm[i] * x_norm[j] * 3 * np.pi) * np.exp(-0.4 * (x_norm[i]**2 + x_norm[j]**2))
        
        # Additional chaotic interaction with higher-order polynomial and frequency modulation
        high_order_interaction = 0.0
        for i in range(self.dim):
            for j in range(i+1, self.dim):
                high_order_interaction += (x_norm[i]**7 + x_norm[j]**7) * np.sin(6 * x_norm[i] * x_norm[j]) * np.cos(4 * x_norm[i] * x_norm[j]) * np.exp(-0.25 * (x_norm[i]**2 + x_norm[j]**2))
        
        # Combined fitness with adaptive weighting and enhanced chaotic components
        return tanh_radial + 0.5 * harmonic_sum + 0.3 * decay_sine + 0.25 * logistic_mod + 0.35 * cross_exp + 0.35 * poly_interaction + 0.2 * trig_coupling + 0.2 * cross_dim_interaction + 0.1 * high_order_interaction