import numpy as np

class ChaoticGradientBenchmark:
    def __init__(self, dim):
        self.dim = dim
        self.global_min = 0.0
        self.bounds = type('Bounds', (), {'lb': np.full(dim, -5.0), 'ub': np.full(dim, 5.0)})()
    
    def f(self, x):
        # Normalize input to [-1, 1] range
        x_norm = x / 5.0
        
        # Enhanced hyperbolic tangent radial component with nested chaotic scaling
        r = np.sqrt(np.sum(x_norm**2))
        tanh_radial = np.sum(np.tanh(6 * x_norm) * (1 + 0.8 * np.sin(9 * r * np.pi) * np.cos(4 * r * np.pi)))
        
        # Dynamic coupled harmonic oscillators with time-varying frequencies and chaotic modulation
        harmonic_sum = 0.0
        for i in range(self.dim):
            for j in range(i+1, self.dim):
                freq_i = 2**(i % 4 + 1)
                freq_j = 2**(j % 4 + 1)
                coupling = np.sin(x_norm[i] * x_norm[j] * 4 * np.pi) * np.cos(freq_i * x_norm[i] * np.pi) * np.sin(freq_j * x_norm[j] * np.pi) * np.exp(-0.2 * (x_norm[i]**2 + x_norm[j]**2))
                harmonic_sum += coupling
        
        # Multi-scale exponentially decaying sinusoidal terms with nested frequency modulation
        decay_sine = 0.0
        for i in range(self.dim):
            freq = 4**(i % 6 + 1)
            decay_sine += np.exp(-0.5 * r**2) * np.sin(freq * x_norm[i] * np.pi) * np.cos(3 * x_norm[i] * np.pi) * np.tanh(2 * x_norm[i])
        
        # Chaotic gradient component using multiple logistic maps with varying parameters
        logistic_mod = 0.0
        for i in range(self.dim):
            logistic_input1 = 3.8 * (x_norm[i] + 0.2) % 1.0
            logistic_input2 = 3.95 * (x_norm[i] - 0.1) % 1.0
            logistic_mod += np.sin(logistic_input1 * 15 * np.pi) * np.cos(logistic_input2 * 10 * np.pi) * np.tanh(3 * x_norm[i])
        
        # Cross-dimensional exponential coupling with nested hyperbolic tangent and chaotic modulation
        cross_exp = 0.0
        for i in range(self.dim):
            for j in range(i+1, self.dim):
                cross_exp += np.tanh(x_norm[i] * x_norm[j]) * np.exp(-0.3 * (x_norm[i]**2 + x_norm[j]**2)) * np.sin(4 * x_norm[i] * x_norm[j]) * np.cos(2 * x_norm[i] * x_norm[j])
        
        # Nested polynomial interactions with chaotic coupling coefficients
        poly_interaction = 0.0
        for i in range(self.dim):
            for j in range(i+1, self.dim):
                coeff = 0.5 + 0.3 * np.sin(5 * x_norm[i] * x_norm[j])
                poly_interaction += (x_norm[i]**6 + x_norm[j]**6) * coeff * np.sin(5 * x_norm[i] * x_norm[j]) * np.cos(3 * x_norm[i] * x_norm[j])
        
        # Enhanced trigonometric coupling with dynamic oscillation and multi-scale modulation
        trig_coupling = 0.0
        for i in range(self.dim):
            trig_coupling += np.sin(4 * x_norm[i] * np.pi) * np.cos(4 * x_norm[i] * np.pi) * np.exp(-0.2 * x_norm[i]**2) * np.tanh(4 * x_norm[i])
        
        # Complex cross-dimensional interaction with adaptive coupling strength and chaotic modulation
        cross_dim_interaction = 0.0
        for i in range(self.dim):
            for j in range(i+1, self.dim):
                coupling_strength = 0.8 + 0.4 * np.sin(7 * x_norm[i] * x_norm[j])
                cross_dim_interaction += np.sin(x_norm[i] * x_norm[j] * 6 * np.pi) * np.cos(x_norm[i] * x_norm[j] * 3 * np.pi) * np.exp(-0.4 * (x_norm[i]**2 + x_norm[j]**2)) * coupling_strength
        
        # Additional chaotic nested component with multi-scale polynomial and sine interactions
        nested_component = 0.0
        for i in range(self.dim):
            for j in range(i+1, self.dim):
                nested_component += (x_norm[i]**3 + x_norm[j]**3) * np.sin(3 * x_norm[i] * x_norm[j]) * np.cos(4 * x_norm[i] * x_norm[j]) * np.exp(-0.3 * (x_norm[i]**2 + x_norm[j]**2))
        
        # Combined fitness with enhanced adaptive weighting and chaotic components
        return tanh_radial + 0.5 * harmonic_sum + 0.3 * decay_sine + 0.25 * logistic_mod + 0.35 * cross_exp + 0.35 * poly_interaction + 0.2 * trig_coupling + 0.2 * cross_dim_interaction + 0.15 * nested_component