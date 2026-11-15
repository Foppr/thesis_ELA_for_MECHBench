import numpy as np

class NestedSinusoidalBenchmark:
    def __init__(self, dim):
        self.dim = dim
        self.freq_base = 2.0 * np.pi
        self.amplitude = 10.0
        self.bias_factor = 0.5
        
    def f(self, x):
        x = np.clip(x, -5.0, 5.0)
        
        # Normalize input to [-1, 1] for consistent scaling
        x_norm = x / 5.0
        
        # Radial component with polynomial scaling
        r = np.sqrt(np.sum(x_norm**2))
        
        # Adaptive frequency modulation based on radial distance
        adaptive_freq = self.freq_base * (1.0 + 0.5 * r)
        
        # Nested sinusoidal terms with varying amplitudes and frequencies
        nested_sum = 0.0
        for i in range(self.dim):
            # Inner sinusoidal term with increasing frequency
            inner_term = np.sin(adaptive_freq * x_norm[i])
            # Outer sinusoidal term with higher frequency
            outer_term = np.sin(3.0 * adaptive_freq * x_norm[i])
            # Combine with amplitude scaling
            nested_sum += self.amplitude * (inner_term + 0.3 * outer_term)
        
        # Radial bias component with polynomial decay
        radial_bias = self.bias_factor * r**3 * np.cos(2.0 * adaptive_freq * r)
        
        # Cross-dimensional interaction terms
        interaction = 0.0
        for i in range(self.dim):
            for j in range(i+1, self.dim):
                interaction += np.sin(adaptive_freq * x_norm[i] * x_norm[j]) * np.cos(adaptive_freq * x_norm[i] * x_norm[j] * 0.5)
        
        # Additional high-frequency oscillation for increased complexity
        high_freq = 0.0
        for i in range(self.dim):
            high_freq += np.sin(15.0 * x_norm[i]) * np.cos(12.0 * x_norm[i])
        
        # Combine all components
        result = (nested_sum + radial_bias + 0.5 * interaction + 0.3 * high_freq) * (1.0 + 0.2 * r)
        
        return result