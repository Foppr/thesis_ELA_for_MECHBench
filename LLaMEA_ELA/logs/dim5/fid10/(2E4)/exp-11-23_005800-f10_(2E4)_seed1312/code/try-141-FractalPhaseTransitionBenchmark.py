import numpy as np

class FractalPhaseTransitionBenchmark:
    def __init__(self, dim):
        self.dim = dim
        self.fractal_dimension = 1.5
        self.phase_frequency = 2.0
        self.transition_strength = 2.0
        self.self_similarity = 0.6
        self.base_amplitude = 1.0
        self.noise_level = 0.02
        self.phase_offsets = np.random.uniform(0, 2*np.pi, dim)
        self.scale_factors = np.random.uniform(0.5, 2.0, dim)
        
    def f(self, x):
        x = np.clip(x, -5.0, 5.0)
        
        # Fractal geometric structure with self-similarity
        fractal_sum = 0.0
        for i in range(self.dim):
            x_i = x[i]
            scale = self.scale_factors[i]
            
            # Multi-scale harmonic components with fractal scaling
            for k in range(1, 6):
                freq = self.phase_frequency * (scale ** k)
                phase = self.phase_offsets[i] + np.pi * k / 4.0
                fractal_sum += (self.base_amplitude / (k ** self.fractal_dimension)) * np.sin(freq * x_i + phase)
                
        # Phase transition regions with dynamic curvature
        transition_term = 0.0
        for i in range(self.dim):
            x_i = x[i]
            # Dynamic phase transition based on position
            phase_transition = np.sin(x_i * self.transition_strength)
            transition_term += phase_transition * (x_i ** 2) * np.cos(x_i)
            
        # Self-similar pattern with varying amplitude
        self_similarity_term = 0.0
        for i in range(self.dim):
            x_i = x[i]
            # Nested harmonic patterns with diminishing amplitude
            nested_sum = 0.0
            for k in range(1, 8):
                nested_sum += (self.self_similarity ** k) * np.cos((x_i / (2**k)) * (k + 1))
            self_similarity_term += nested_sum
            
        # Combined fractal landscape with dynamic scaling
        result = fractal_sum**2 + transition_term + self_similarity_term
        
        # Add dynamic noise for increased complexity
        noise = np.random.normal(0, self.noise_level) * np.sin(np.sum(x)**2)
        
        return result + noise