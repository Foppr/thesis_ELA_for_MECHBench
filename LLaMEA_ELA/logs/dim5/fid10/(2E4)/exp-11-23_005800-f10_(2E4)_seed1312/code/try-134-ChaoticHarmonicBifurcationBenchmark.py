import numpy as np

class ChaoticHarmonicBifurcationBenchmark:
    def __init__(self, dim):
        self.dim = dim
        self.time = 0.0
        self.base_frequency = 2.0
        self.harmonic_amplitude = 1.5
        self.bifurcation_parameter = 3.8
        self.saddle_strength = 0.8
        self.noise_level = 0.01
        self.phase_offsets = np.random.uniform(0, 2*np.pi, dim)
        self.frequency_modulation = np.random.uniform(0.8, 1.5, dim)
        
    def f(self, x):
        x = np.clip(x, -5.0, 5.0)
        self.time += 0.01
        
        # Time-varying harmonic potential with bifurcation dynamics
        harmonic_sum = 0.0
        for i in range(self.dim):
            freq = self.base_frequency * self.frequency_modulation[i]
            phase = self.phase_offsets[i] + self.time * (i + 1) * 0.1
            x_i = x[i]
            
            # Base harmonic term
            harmonic_sum += np.sin(freq * x_i + phase) * np.cos(freq * x_i + phase)
            
            # Add higher-order harmonics with time-varying coupling
            harmonic_sum += 0.3 * np.sin(2 * freq * x_i + phase) * np.cos(2 * freq * x_i + phase)
            
        # Bifurcation-driven potential wells with varying depth
        r = np.linalg.norm(x)
        bifurcation_term = self.bifurcation_parameter * (r**2 - 1.0)**2
        
        # Saddle-node bifurcations creating intermittent chaotic regions
        saddle_term = 0.0
        for i in range(self.dim):
            saddle_term += self.saddle_strength * np.sin(x[i]) * np.cos(x[i])
            
        # Time-varying harmonic modulation with chaotic coupling
        time_modulation = 1.0 + 0.2 * np.sin(self.time * 3.0) * np.cos(self.time * 2.0)
        
        # Combine all terms with dynamic scaling
        result = time_modulation * (harmonic_sum**2 + self.harmonic_amplitude * bifurcation_term + saddle_term)
        
        # Add chaotic noise for increased complexity
        noise = np.random.normal(0, self.noise_level) * np.sin(self.time * 5.0)
        
        return result + noise