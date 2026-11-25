import numpy as np

class NestedTrigonometricOscillationBenchmark:
    def __init__(self, dim):
        self.dim = dim
        # Initialize parameters for nested oscillatory components
        self.frequency_layers = np.random.uniform(1.0, 10.0, (dim, 6))
        self.amplitude_layers = np.random.uniform(0.5, 3.0, (dim, 6))
        self.phase_shifts = np.random.uniform(0, 2*np.pi, (dim, 6))
        self.interference_weights = np.random.uniform(-1.0, 1.0, (dim, 5))
        self.spatial_modulation = np.random.uniform(0.1, 2.0, dim)
        self.harmonic_mixing = np.random.uniform(0.1, 3.0, (dim, 4))
        
    def f(self, x):
        x = np.array(x)
        
        # Nested trigonometric oscillation with multiple layers
        nested_term = 0.0
        for i in range(self.dim):
            layer_sum = 0.0
            for j in range(6):
                freq = self.frequency_layers[i, j]
                amp = self.amplitude_layers[i, j]
                phase = self.phase_shifts[i, j]
                layer_sum += amp * np.sin(freq * x[i] + phase) + \
                            amp * np.cos(freq * x[i] * 0.7 + phase) + \
                            amp * np.sin(freq * x[i] * 1.3 + phase) * np.exp(-0.1 * x[i]**2)
            nested_term += layer_sum
        
        # Spatially varying harmonic interference
        interference_term = 0.0
        for i in range(self.dim):
            spatial_factor = self.spatial_modulation[i]
            for j in range(5):
                weight = self.interference_weights[i, j]
                interference_term += weight * np.sin(x[i] * spatial_factor * (j+1)) * \
                                   np.cos(x[i] * spatial_factor * (j+1) * 0.5)
        
        # Adaptive harmonic mixing with dynamic weights
        mixing_term = 0.0
        for i in range(self.dim):
            mix_weights = self.harmonic_mixing[i]
            mixing_term += mix_weights[0] * np.sin(x[i] * mix_weights[1]) + \
                          mix_weights[2] * np.cos(x[i] * mix_weights[3]) * np.exp(-0.05 * x[i]**2)
        
        # Combine all components with adaptive scaling
        total = 0.40 * nested_term + 0.35 * interference_term + 0.25 * mixing_term
        
        # Add spatially varying global modulation
        global_mod = np.prod(1.0 + 0.2 * np.sin(x * 0.5) * np.cos(x * 0.3))
        
        return total * global_mod + 0.05 * np.sum(x**2)