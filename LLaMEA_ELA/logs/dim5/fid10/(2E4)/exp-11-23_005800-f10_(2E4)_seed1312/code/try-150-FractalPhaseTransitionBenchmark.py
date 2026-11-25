import numpy as np

class FractalPhaseTransitionBenchmark:
    def __init__(self, dim):
        self.dim = dim
        self.time = 0.0
        self.fractal_dimension = 1.8
        self.phase_transition_freq = 2.1
        self.self_similarity = 0.6
        self.transition_strength = 3.0
        self.geometry_modulation = np.random.uniform(0.3, 1.8, dim)
        self.phase_offsets = np.random.uniform(0, 4*np.pi, dim)
        self.frequency_spectrum = np.random.uniform(0.5, 2.5, dim)
        self.coupling_strength = np.random.uniform(0.1, 0.5, (dim, dim))
        self.resonance_frequency = np.random.uniform(0.1, 0.8, dim)
        
    def f(self, x):
        x = np.clip(x, -5.0, 5.0)
        self.time += 0.03
        
        # Hyperbolic tangent based phase transitions
        tanh_sum = 0.0
        for i in range(self.dim):
            freq = self.frequency_spectrum[i]
            phase = self.phase_offsets[i] + self.time * freq * 0.7
            
            # Hyperbolic tangent components with varying steepness
            x_i = x[i]
            tanh_sum += np.tanh(freq * x_i + phase) * np.sin(freq * x_i + phase)
            
            # Add higher-order hyperbolic terms
            tanh_sum += 0.3 * np.tanh(2 * freq * x_i + phase) * np.cos(2 * freq * x_i + phase)
            
        # Dynamic coupling between dimensions with stochastic resonance
        coupling_term = 0.0
        for i in range(self.dim):
            for j in range(self.dim):
                if i != j:
                    coupling_term += self.coupling_strength[i][j] * np.sin(x[i] - x[j] + self.time * 0.5)
        
        # Stochastic resonance effect with time-varying frequency
        resonance_effect = 0.0
        for i in range(self.dim):
            freq = self.resonance_frequency[i]
            resonance_effect += np.sin(freq * self.time + x[i]) * np.cos(freq * self.time + x[i])
        
        # Phase transition dynamics creating varying curvature with hyperbolic scaling
        r = np.linalg.norm(x)
        transition_term = self.transition_strength * np.tanh(self.phase_transition_freq * r + self.time)
        
        # Self-similar geometric patterns with multi-scale modulation
        geometry_pattern = 0.0
        for i in range(self.dim):
            mod = self.geometry_modulation[i]
            geometry_pattern += (mod * np.tanh(x[i] * self.fractal_dimension) * 
                               np.sin(x[i] * self.fractal_dimension))
            
        # Dynamic phase modulation with fractal coupling
        phase_modulation = 1.0 + 0.4 * np.tanh(self.time * 3.0) * np.sin(self.time * 2.0)
        
        # Combine all terms with dynamic scaling and stochastic noise
        result = phase_modulation * (tanh_sum**2 + coupling_term * transition_term + geometry_pattern * resonance_effect)
        
        # Add chaotic noise for increased complexity
        noise = np.random.normal(0, 0.03) * np.tanh(self.time * 5.0)
        
        return result + noise