import numpy as np

class FractalPhaseTransitionBenchmark:
    def __init__(self, dim):
        self.dim = dim
        self.fractal_dimension = 1.5
        self.phase_transition_freq = 0.5
        self.hierarchical_depth = 3
        self.base_amplitude = 2.0
        self.transition_strength = 1.2
        self.scale_factor = 0.8
        self.phase_shifts = np.random.uniform(0, 2*np.pi, dim)
        self.frequency_scales = np.random.uniform(0.5, 2.0, dim)
        
    def f(self, x):
        x = np.clip(x, -5.0, 5.0)
        
        # Normalize input to [-1, 1] for fractal generation
        x_norm = x / 5.0
        
        # Hierarchical fractal potential with self-similarity
        fractal_sum = 0.0
        for depth in range(self.hierarchical_depth):
            scale = self.scale_factor ** depth
            freq = self.frequency_scales * (2 ** depth)
            
            # Generate fractal terms with phase shifts
            for i in range(self.dim):
                phase = self.phase_shifts[i] + depth * np.pi / 4
                term = np.sin(freq[i] * x_norm[i] + phase) * scale
                fractal_sum += term**2
                
        # Phase transition dynamics creating dynamic landscape
        transition_phase = np.sin(self.phase_transition_freq * np.sum(x_norm))
        transition_factor = 1.0 + self.transition_strength * (np.cos(transition_phase) - 0.5)
        
        # Multi-scale harmonic interactions
        harmonic_sum = 0.0
        for i in range(self.dim):
            for k in range(1, 4):
                harmonic_sum += np.sin(k * x[i] * self.frequency_scales[i]) * (1.0 / k)
                
        # Self-similar basin structure with nested minima
        basin_term = 0.0
        for i in range(self.dim):
            basin_term += (x[i]**2 + 0.1) * np.sin(5 * x[i])
            
        # Combine all components with dynamic scaling
        result = transition_factor * (self.base_amplitude * fractal_sum + harmonic_sum + basin_term)
        
        # Add fractional Brownian motion-like complexity
        fbm_noise = 0.0
        for i in range(self.dim):
            fbm_noise += np.sin(x[i] * 10.0) * np.cos(x[i] * 7.0) * (1.0 / (i + 1)**self.fractal_dimension)
            
        return result + 0.1 * fbm_noise