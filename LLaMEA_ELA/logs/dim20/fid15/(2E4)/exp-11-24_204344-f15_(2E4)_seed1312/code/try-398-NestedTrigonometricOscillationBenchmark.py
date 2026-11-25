import numpy as np

class NestedTrigonometricOscillationBenchmark:
    def __init__(self, dim):
        self.dim = dim
        # Initialize parameters for nested oscillatory components
        self.frequency_scales = np.random.uniform(0.5, 3.0, dim)
        self.amplitude_scales = np.random.uniform(1.0, 4.0, dim)
        self.phase_offsets = np.random.uniform(0, 2*np.pi, dim)
        self.harmonic_weights = np.random.uniform(0.1, 2.0, (dim, 5))
        self.interference_patterns = np.random.uniform(-1.0, 1.0, (dim, dim))
        self.spatial_modulation = np.random.uniform(0.5, 2.0, dim)
        
    def f(self, x):
        x = np.array(x)
        result = 0.0
        
        # Nested trigonometric oscillations with varying frequencies and amplitudes
        for i in range(self.dim):
            freq = self.frequency_scales[i]
            amp = self.amplitude_scales[i]
            phase = self.phase_offsets[i]
            
            # Multiple harmonic components with adaptive weights
            harmonic_sum = 0.0
            for j in range(5):
                weight = self.harmonic_weights[i, j]
                harmonic_sum += weight * np.sin(freq * (x[i] + phase) * (j + 1))
            
            # Spatial interference pattern modulation
            interference = 0.0
            for k in range(self.dim):
                if i != k:
                    interference += self.interference_patterns[i, k] * np.cos(x[k] * 0.5)
            
            # Combined component with spatial modulation
            result += amp * harmonic_sum * (1.0 + 0.3 * interference) * self.spatial_modulation[i]
        
        # Add coupling terms between dimensions with nonlinear interaction
        coupling_term = 0.0
        for i in range(self.dim):
            for j in range(i+1, self.dim):
                # Nonlinear coupling with distance-based modulation
                dist = np.abs(x[i] - x[j])
                coupling_factor = np.exp(-dist * 0.5) * np.sin(dist * 2.0)
                coupling_term += coupling_factor * (x[i]**2 + x[j]**2)
        
        result += 0.1 * coupling_term
        
        # Add global scaling and noise component
        global_scale = np.sum(np.abs(x)) * 0.1
        noise_component = np.sum(np.random.randn(self.dim) * 0.01)
        
        return result + global_scale + noise_component