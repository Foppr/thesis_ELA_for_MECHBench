import numpy as np

class FractalPhaseTransitionBenchmark:
    def __init__(self, dim):
        self.dim = dim
        self.time = 0.0
        self.fractal_dimension = 2.1
        self.phase_transition_freq = 1.8
        self.self_similarity = 0.85
        self.transition_strength = 3.2
        self.geometry_modulation = np.random.uniform(0.3, 1.7, dim)
        self.phase_offsets = np.random.uniform(0, 4*np.pi, dim)
        self.frequency_spectrum = np.random.uniform(0.5, 2.5, dim)
        self.resonance_frequency = np.random.uniform(0.1, 0.5, dim)
        self.stochastic_amplitude = 0.1
        self.multi_scale_factor = 1.5
        
    def f(self, x):
        x = np.clip(x, -5.0, 5.0)
        self.time += 0.03
        
        # Multi-scale fractal harmonic components with chaotic coupling
        fractal_sum = 0.0
        for i in range(self.dim):
            freq = self.frequency_spectrum[i]
            phase = self.phase_offsets[i] + self.time * freq * 0.7
            
            # Chaotic higher-order harmonics with multi-scale coupling
            x_i = x[i]
            fractal_sum += (np.sin(freq * x_i + phase) * 
                           np.cos(freq * x_i + phase) * 
                           np.sin(2 * freq * x_i + phase) *
                           np.cos(3 * freq * x_i + phase))
            
            # Add chaotic fractal terms with varying scales
            fractal_sum += 0.3 * np.sin(4 * freq * x_i + phase) * np.cos(4 * freq * x_i + phase)
            fractal_sum += 0.2 * np.sin(5 * freq * x_i + phase) * np.cos(5 * freq * x_i + phase)
            
        # Dynamic phase transition with chaotic modulation
        r = np.linalg.norm(x)
        transition_term = self.transition_strength * np.sin(self.phase_transition_freq * r + self.time)
        
        # Multi-scale geometric patterns with stochastic resonance
        geometry_pattern = 0.0
        for i in range(self.dim):
            mod = self.geometry_modulation[i]
            geo_freq = self.frequency_spectrum[i] * self.multi_scale_factor
            geometry_pattern += (mod * np.sin(x[i] * geo_freq) * 
                               np.cos(x[i] * geo_freq) *
                               np.sin(x[i] * geo_freq * 0.5))
            
        # Time-varying stochastic resonance effect
        resonance_effect = 0.0
        for i in range(self.dim):
            freq = self.resonance_frequency[i]
            resonance_effect += np.sin(freq * x[i] + self.time * freq) * np.cos(freq * x[i] + self.time * freq)
        
        # Dynamic scaling with chaotic modulation
        phase_modulation = 1.0 + 0.5 * np.sin(self.time * 3.0) * np.cos(self.time * 2.0) * np.sin(self.time * 1.5)
        
        # Combine all terms with chaotic coupling
        result = phase_modulation * (fractal_sum**2 + transition_term * geometry_pattern + resonance_effect * 0.5)
        
        # Add stochastic noise with chaotic amplitude modulation
        noise_amplitude = self.stochastic_amplitude * (1.0 + 0.3 * np.sin(self.time * 5.0))
        noise = np.random.normal(0, noise_amplitude) * np.sin(self.time * 6.0)
        
        # Add chaotic basin structure
        basin_term = 0.0
        for i in range(self.dim):
            basin_term += np.sin(x[i] * 2.0 + self.time * 0.5) * np.cos(x[i] * 1.5 + self.time * 0.3)
        
        return result + noise + 0.1 * basin_term