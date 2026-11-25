import numpy as np

class AdaptiveSineCosineBenchmark:
    def __init__(self, dim):
        self.dim = dim
        # Initialize parameters for adaptive sine-cosine waves
        self.amplitude_params = np.random.uniform(0.5, 2.0, dim)
        self.frequency_params = np.random.uniform(1.0, 5.0, dim)
        self.phase_params = np.random.uniform(0, 2*np.pi, dim)
        self.damping_params = np.random.uniform(0.1, 0.8, dim)
        self.harmonic_weights = np.random.uniform(0.3, 1.5, dim)
        self.cross_coupling_strengths = np.random.uniform(0.5, 2.0, (dim, dim))
        self.modulation_indices = np.random.uniform(0.5, 3.0, dim)
        self.resonance_frequencies = np.random.uniform(0.1, 2.0, dim)
        self.nonlinear_exponents = np.random.uniform(1.5, 4.0, dim)
        self.adaptive_scaling = np.random.uniform(0.5, 2.5, dim)
        
    def f(self, x):
        # Normalize input to [-1, 1] range
        x_norm = x / 5.0
        
        # Base sine-cosine wave components
        wave_sum = 0.0
        for i in range(self.dim):
            # Adaptive frequency modulation
            freq = self.frequency_params[i] * (1 + 0.3 * np.sin(x_norm[i] * 2))
            # Sine-cosine wave with damping and phase shift
            wave_component = (self.amplitude_params[i] * 
                            np.sin(freq * x_norm[i] + self.phase_params[i]) * 
                            np.cos(freq * x_norm[i] + self.phase_params[i]) * 
                            np.exp(-self.damping_params[i] * np.abs(x_norm[i])))
            wave_sum += wave_component * self.harmonic_weights[i]
        
        # Cross-dimensional coupling with harmonic resonance
        coupling_terms = 0.0
        for i in range(self.dim):
            for j in range(self.dim):
                if i != j:
                    coupling_strength = self.cross_coupling_strengths[i, j]
                    coupling_terms += (coupling_strength * 
                                     np.sin(x_norm[i] * x_norm[j]) * 
                                     np.cos(x_norm[i] * x_norm[j]) * 
                                     np.exp(-0.5 * (x_norm[i] - x_norm[j])**2))
        
        # Harmonic resonance components
        resonance_terms = 0.0
        for i in range(self.dim):
            resonance_terms += (np.sin(self.resonance_frequencies[i] * x_norm[i]) * 
                              np.cos(self.resonance_frequencies[i] * x_norm[i]) * 
                              np.exp(-0.1 * np.abs(x_norm[i])))
        
        # Nonlinear distortion and adaptive scaling
        nonlinear_terms = 0.0
        for i in range(self.dim):
            nonlinear_terms += (np.sin(x_norm[i]**self.nonlinear_exponents[i]) * 
                              np.cos(x_norm[i]**self.nonlinear_exponents[i]) * 
                              self.adaptive_scaling[i])
        
        # Modulation and final combination
        modulation_factor = 1.0 + 0.2 * np.sin(np.sum(x_norm) * 0.5)
        return (modulation_factor * (wave_sum + coupling_terms + resonance_terms + nonlinear_terms) +
                0.5 * np.sum(x_norm**2))