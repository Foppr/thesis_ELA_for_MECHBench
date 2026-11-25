import numpy as np

class ChaoticHarmonicBifurcationBenchmark:
    def __init__(self, dim):
        self.dim = dim
        self.time = 0.0
        self.base_frequency = 2.5
        self.harmonic_amplitude = 1.8
        self.bifurcation_parameter = 4.0
        self.saddle_strength = 1.0
        self.noise_level = 0.02
        self.phase_offsets = np.random.uniform(0, 2*np.pi, dim)
        self.frequency_modulation = np.random.uniform(0.9, 1.6, dim)
        self.modulation_frequency = np.random.uniform(1.5, 3.0, dim)
        
    def f(self, x):
        x = np.clip(x, -5.0, 5.0)
        self.time += 0.01
        
        # Enhanced harmonic potential with multi-scale frequency modulation
        harmonic_sum = 0.0
        for i in range(self.dim):
            freq = self.base_frequency * self.frequency_modulation[i]
            phase = self.phase_offsets[i] + self.time * (i + 1) * 0.15
            x_i = x[i]
            
            # Base harmonic term with enhanced nonlinearity
            harmonic_sum += np.sin(freq * x_i + phase) * np.cos(freq * x_i + phase)
            
            # Higher-order harmonics with adaptive coupling
            harmonic_sum += 0.4 * np.sin(2 * freq * x_i + phase) * np.cos(2 * freq * x_i + phase)
            
            # Third harmonic for increased complexity
            harmonic_sum += 0.2 * np.sin(3 * freq * x_i + phase) * np.cos(3 * freq * x_i + phase)
            
        # Enhanced bifurcation potential with multi-modal wells
        r = np.linalg.norm(x)
        bifurcation_term = self.bifurcation_parameter * (r**2 - 1.0)**2
        
        # Modified saddle-node bifurcations with spatial variation
        saddle_term = 0.0
        for i in range(self.dim):
            # Spatially varying saddle strength
            local_saddle = self.saddle_strength * (1.0 + 0.3 * np.sin(x[i] * 2.0))
            saddle_term += local_saddle * np.sin(x[i]) * np.cos(x[i])
            
        # Advanced time-varying modulation with chaotic coupling
        time_modulation = 1.0 + 0.3 * np.sin(self.time * self.modulation_frequency[0]) * np.cos(self.time * self.modulation_frequency[1])
        
        # Additional chaotic modulation based on all dimensions
        chaotic_factor = 1.0 + 0.1 * np.sin(np.sum(x) * 0.5 + self.time * 2.0)
        
        # Combine all terms with dynamic scaling and enhanced complexity
        result = time_modulation * (harmonic_sum**2 + self.harmonic_amplitude * bifurcation_term + saddle_term) * chaotic_factor
        
        # Enhanced noise with multi-dimensional correlation
        noise = np.random.normal(0, self.noise_level) * np.sin(self.time * 7.0 + np.sum(x))
        
        return result + noise