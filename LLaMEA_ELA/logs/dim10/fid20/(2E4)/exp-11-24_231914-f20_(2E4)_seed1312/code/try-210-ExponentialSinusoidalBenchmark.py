import numpy as np

class ExponentialSinusoidalBenchmark:
    def __init__(self, dim):
        self.dim = dim
        # Initialize chaotic sinusoidal parameters with quantum-like randomness
        self.chaotic_freq = np.random.uniform(1.0, 25.0, size=dim)
        self.chaotic_amp = np.random.uniform(0.1, 4.0, size=dim)
        self.quantum_phase = np.random.uniform(0, 2*np.pi, size=dim)
        # Fractal ruggedness parameters with self-similar structure
        self.fractal_depth = np.random.randint(3, 12, size=dim)
        self.fractal_scale = np.random.uniform(0.02, 1.5, size=dim)
        # Enhanced cubic coupling with non-linear interaction weights (modified)
        self.cubic_weights = np.random.uniform(-1.5, 1.5, size=(dim, dim))  # Reduced range
        # Multi-scale exponential decay with quantum tunneling effects
        self.decay_rates = np.random.uniform(0.01, 5.0, size=dim)
        self.tunneling_prob = np.random.uniform(0.001, 0.4, size=dim)
        # Dynamic harmonic interference with time-delayed feedback
        self.delay_freq = np.random.uniform(0.5, 12.0, size=dim)
        self.feedback_strength = np.random.uniform(0.03, 0.7, size=dim)
        # Novel dynamic coupling parameters (modified)
        self.dynamic_coupling = np.random.uniform(-2.5, 2.5, size=dim)  # Reduced range
        self.harmonic_modulation = np.random.uniform(0.3, 3.0, size=dim)
        self.stochastic_resonance = np.random.uniform(0.05, 1.0, size=dim)
        # Additional parameters for improved fitness score (modified)
        self.amplitude_modulation = np.random.uniform(0.3, 2.5, size=dim)
        self.frequency_modulation = np.random.uniform(0.05, 3.5, size=dim)
        # New enhanced complexity parameters (modified)
        self.interaction_strength = np.random.uniform(1.0, 3.0, size=dim)  # Reduced range
        self.resonance_frequency = np.random.uniform(0.2, 2.0, size=dim)
        self.fractal_intensity = np.random.uniform(0.8, 2.5, size=dim)
        self.coupling_decay = np.random.uniform(0.1, 0.9, size=dim)
        # New parameters for improved landscape characteristics (modified)
        self.nonlinear_damping = np.random.uniform(0.1, 1.5, size=dim)  # Reduced range
        self.wave_interaction = np.random.uniform(0.5, 2.5, size=dim)
        self.resonance_amplitude = np.random.uniform(0.5, 2.0, size=dim)  # Reduced range
        
    def f(self, x):
        # Scale input to [-5, 5]
        x = np.clip(x, -5.0, 5.0)
        
        # Chaotic sinusoidal component with quantum phase modulation and amplitude modulation
        chaotic_component = 0.0
        for i in range(self.dim):
            phase = self.quantum_phase[i] + np.sin(x[i]) * np.cos(x[(i+1)%self.dim])
            amplitude = self.chaotic_amp[i] * (1 + 0.4 * np.sin(self.amplitude_modulation[i] * x[i]))
            chaotic_component += (np.sin(self.chaotic_freq[i] * x[i] + phase) * 
                                amplitude * np.exp(-0.3 * x[i]**2))
            
        # Fractal-based ruggedness with multi-scale interference
        fractal_ruggedness = 0.0
        for i in range(self.dim):
            base_fractal = 0.0
            for depth in range(1, self.fractal_depth[i]+1):
                scale = self.fractal_scale[i] * (0.3**depth)
                freq = self.chaotic_freq[i] * (3.0**depth)
                base_fractal += np.sin(freq * x[i]) * scale
            fractal_ruggedness += base_fractal * np.cos(x[i]**2) * self.chaotic_amp[i] * self.fractal_intensity[i]
            
        # Quantum-like exponential decay with tunneling probability and frequency modulation
        quantum_decay = 0.0
        for i in range(self.dim):
            tunnel_prob = self.tunneling_prob[i] * np.exp(-0.2 * x[i]**2)
            freq_mod = self.frequency_modulation[i] * (1 + 0.3 * np.cos(x[i]))
            quantum_decay += (np.exp(-self.decay_rates[i] * np.abs(x[i])) + 
                            tunnel_prob * np.sin(freq_mod * x[i])) * self.chaotic_amp[i]
            
        # Multi-scale cubic coupling with dynamic interaction and phase shifting
        cubic_coupling = 0.0
        for i in range(self.dim):
            for j in range(self.dim):
                if i != j:
                    interaction = (x[i]**3) * (x[j]**2) + (x[i]**2) * (x[j]**3)
                    phase_shift = self.phase_shift[i] + self.phase_shift[j]
                    cubic_coupling += self.cubic_weights[i, j] * interaction * np.cos(phase_shift)
                    
        # Time-delayed harmonic feedback with chaotic interference and dynamic coupling
        delayed_harmonic = 0.0
        for i in range(self.dim):
            delay_term = np.sin(self.delay_freq[i] * x[(i-1)%self.dim]) * self.feedback_strength[i]
            dynamic_term = self.dynamic_coupling[i] * np.cos(x[i])
            delayed_harmonic += (np.sin(self.chaotic_freq[i] * x[i] + delay_term) + 
                               0.4 * np.cos(2 * self.chaotic_freq[i] * x[i] + delay_term) + 
                               dynamic_term) * self.chaotic_amp[i]
        
        # Novel dynamic coupling mechanism with harmonic modulation
        dynamic_coupling = 0.0
        for i in range(self.dim):
            harmonic = np.sin(self.harmonic_modulation[i] * x[i]) * np.cos(self.harmonic_modulation[i] * x[i])
            dynamic_coupling += (self.dynamic_coupling[i] * 
                               harmonic * 
                               np.exp(-0.2 * x[i]**2))
        
        # Stochastic resonance enhancement with phase modulation
        stochastic_effect = 0.0
        for i in range(self.dim):
            phase_mod = self.phase_shift[i] + 0.15 * np.sin(x[i])
            stochastic_effect += (self.stochastic_resonance[i] * 
                                np.sin(x[i] * (1 + 0.15 * np.random.rand()) + phase_mod) * 
                                np.cos(2 * x[i] + phase_mod))
        
        # Enhanced interaction terms for increased complexity
        enhanced_interaction = 0.0
        for i in range(self.dim):
            enhanced_interaction += (self.interaction_strength[i] * 
                                  np.sin(self.resonance_frequency[i] * x[i]) * 
                                  np.cos(self.resonance_frequency[i] * x[i])**2)
        
        # New nonlinear damping and wave interaction terms to improve landscape characteristics
        damping_term = 0.0
        wave_interaction_term = 0.0
        for i in range(self.dim):
            damping_term += self.nonlinear_damping[i] * np.sin(x[i]**3) * np.exp(-x[i]**2/10)
            wave_interaction_term += self.wave_interaction[i] * np.sin(x[i]) * np.cos(x[i]**2) * self.resonance_amplitude[i]
        
        # Combined fitness with enhanced non-linearity and complexity
        return (2.0 * chaotic_component + 
                1.8 * fractal_ruggedness + 
                1.6 * quantum_decay + 
                2.2 * cubic_coupling + 
                1.6 * delayed_harmonic + 
                1.0 * dynamic_coupling + 
                0.8 * stochastic_effect + 
                0.7 * enhanced_interaction +
                0.5 * damping_term +
                0.4 * wave_interaction_term)