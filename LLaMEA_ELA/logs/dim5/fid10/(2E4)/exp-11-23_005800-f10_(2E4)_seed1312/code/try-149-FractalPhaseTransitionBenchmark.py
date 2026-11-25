import numpy as np

class FractalPhaseTransitionBenchmark:
    def __init__(self, dim):
        self.dim = dim
        self.time = 0.0
        self.fractal_dimension = 1.5
        self.phase_transition_freq = 1.2
        self.self_similarity = 0.7
        self.transition_strength = 2.0
        self.geometry_modulation = np.random.uniform(0.5, 1.5, dim)
        self.phase_offsets = np.random.uniform(0, 2*np.pi, dim)
        self.frequency_spectrum = np.random.uniform(0.8, 2.0, dim)
        
    def f(self, x):
        x = np.clip(x, -5.0, 5.0)
        self.time += 0.02
        
        # Fractal geometric structure with self-similarity
        fractal_sum = 0.0
        for i in range(self.dim):
            freq = self.frequency_spectrum[i]
            phase = self.phase_offsets[i] + self.time * freq * 0.5
            
            # Multi-scale harmonic components with fractal scaling
            x_i = x[i]
            fractal_sum += (np.sin(freq * x_i + phase) * 
                           np.cos(freq * x_i + phase) * 
                           np.sin(2 * freq * x_i + phase))
            
            # Add fractal higher-order terms
            fractal_sum += 0.5 * np.sin(3 * freq * x_i + phase) * np.cos(3 * freq * x_i + phase)
            
        # Phase transition dynamics creating varying curvature
        r = np.linalg.norm(x)
        transition_term = self.transition_strength * np.sin(self.phase_transition_freq * r + self.time)
        
        # Self-similar geometric patterns with multi-scale modulation
        geometry_pattern = 0.0
        for i in range(self.dim):
            mod = self.geometry_modulation[i]
            geometry_pattern += (mod * np.sin(x[i] * self.fractal_dimension) * 
                               np.cos(x[i] * self.fractal_dimension))
            
        # Dynamic phase modulation with fractal coupling
        phase_modulation = 1.0 + 0.3 * np.sin(self.time * 2.0) * np.cos(self.time * 1.5)
        
        # Combine all terms with dynamic scaling and improved normalization
        result = phase_modulation * (fractal_sum**2 + transition_term * geometry_pattern)
        
        # Add improved fractal noise with better statistical properties for robust benchmarking
        noise = np.random.normal(0, 0.01) * np.sin(self.time * 3.0 + np.sum(x))
        
        # Apply a sigmoid transformation to reduce extreme values and improve conditioning
        result = 1.0 / (1.0 + np.exp(-result)) - 0.5
        
        return result + noise