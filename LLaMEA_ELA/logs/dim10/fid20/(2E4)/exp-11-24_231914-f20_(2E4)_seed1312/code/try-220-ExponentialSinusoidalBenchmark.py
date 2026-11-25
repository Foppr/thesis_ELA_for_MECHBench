import numpy as np

class ExponentialSinusoidalBenchmark:
    def __init__(self, dim):
        self.dim = dim
        # Initialize chaotic sinusoidal parameters with quantum-like randomness
        self.chaotic_freq = np.random.uniform(1.0, 30.0, size=dim)
        self.chaotic_amp = np.random.uniform(0.1, 5.0, size=dim)
        self.quantum_phase = np.random.uniform(0, 2*np.pi, size=dim)
        # Fractal ruggedness parameters with self-similar structure
        self.fractal_depth = np.random.randint(3, 15, size=dim)
        self.fractal_scale = np.random.uniform(0.01, 2.0, size=dim)
        # Enhanced cubic coupling with non-linear interaction weights
        self.cubic_weights = np.random.uniform(-3.0, 3.0, size=(dim, dim))
        # Multi-scale exponential decay with quantum tunneling effects
        self.decay_rates = np.random.uniform(0.01, 6.0, size=dim)
        self.tunneling_prob = np.random.uniform(0.0005, 0.5, size=dim)
        # Dynamic harmonic interference with time-delayed feedback
        self.delay_freq = np.random.uniform(0.3, 15.0, size=dim)
        self.feedback_strength = np.random.uniform(0.02, 0.8, size=dim)
        # Novel dynamic coupling parameters
        self.dynamic_coupling = np.random.uniform(-4.0, 4.0, size=dim)
        self.harmonic_modulation = np.random.uniform(0.2, 4.0, size=dim)
        self.stochastic_resonance = np.random.uniform(0.03, 1.2, size=dim)
        # Additional parameters for improved fitness score
        self.amplitude_modulation = np.random.uniform(0.2, 3.0, size=dim)
        self.frequency_modulation = np.random.uniform(0.03, 4.0, size=dim)
        self.phase_shift = np.random.uniform(-np.pi, np.pi, size=dim)
        # New enhanced complexity parameters
        self.interaction_strength = np.random.uniform(1.2, 4.0, size=dim)
        self.resonance_frequency = np.random.uniform(0.1, 2.5, size=dim)
        self.fractal_intensity = np.random.uniform(0.6, 3.0, size=dim)
        self.coupling_decay = np.random.uniform(0.05, 0.95, size=dim)
        # New parameters for improved landscape characteristics
        self.nonlinear_damping = np.random.uniform(0.05, 2.5, size=dim)
        self.wave_interaction = np.random.uniform(0.3, 3.5, size=dim)
        self.resonance_amplitude = np.random.uniform(0.3, 3.0, size=dim)
        # Additional chaotic components for increased multimodality
        self.chaotic_mutation = np.random.uniform(-1.5, 1.5, size=dim)
        self.modulation_depth = np.random.uniform(0.3, 3.5, size=dim)
        self.frequency_jitter = np.random.uniform(0.05, 2.5, size=dim)
        # New coupling mechanisms for increased complexity
        self.cross_coupling = np.random.uniform(-2.0, 2.0, size=(dim, dim))
        self.resonance_shift = np.random.uniform(-0.7, 0.7, size=dim)
        # Additional high-order interaction terms
        self.high_order_weights = np.random.uniform(-0.5, 0.5, size=(dim, dim, dim))
        self.gaussian_kernel = np.random.uniform(0.1, 1.0, size=dim)
        self.spectral_mixing = np.random.uniform(0.2, 1.8, size=dim)
        
    def f(self, x):
        # Scale input to [-5, 5]
        x = np.clip(x, -5.0, 5.0)
        
        # Chaotic sinusoidal component with quantum phase modulation and amplitude modulation
        chaotic_component = 0.0
        for i in range(self.dim):
            phase = self.quantum_phase[i] + np.sin(x[i]) * np.cos(x[(i+1)%self.dim])
            amplitude = self.chaotic_amp[i] * (1 + 0.5 * np.sin(self.amplitude_modulation[i] * x[i]))
            chaotic_component += (np.sin(self.chaotic_freq[i] * x[i] + phase) * 
                                amplitude * np.exp(-0.2 * x[i]**2))
            
        # Fractal-based ruggedness with multi-scale interference
        fractal_ruggedness = 0.0
        for i in range(self.dim):
            base_fractal = 0.0
            for depth in range(1, self.fractal_depth[i]+1):
                scale = self.fractal_scale[i] * (0.25**depth)
                freq = self.chaotic_freq[i] * (2.5**depth)
                base_fractal += np.sin(freq * x[i]) * scale
            fractal_ruggedness += base_fractal * np.cos(x[i]**2) * self.chaotic_amp[i] * self.fractal_intensity[i]
            
        # Quantum-like exponential decay with tunneling probability and frequency modulation
        quantum_decay = 0.0
        for i in range(self.dim):
            tunnel_prob = self.tunneling_prob[i] * np.exp(-0.15 * x[i]**2)
            freq_mod = self.frequency_modulation[i] * (1 + 0.4 * np.cos(x[i]))
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
                               0.5 * np.cos(2 * self.chaotic_freq[i] * x[i] + delay_term) + 
                               dynamic_term) * self.chaotic_amp[i]
        
        # Novel dynamic coupling mechanism with harmonic modulation
        dynamic_coupling = 0.0
        for i in range(self.dim):
            harmonic = np.sin(self.harmonic_modulation[i] * x[i]) * np.cos(self.harmonic_modulation[i] * x[i])
            dynamic_coupling += (self.dynamic_coupling[i] * 
                               harmonic * 
                               np.exp(-0.15 * x[i]**2))
        
        # Stochastic resonance enhancement with phase modulation
        stochastic_effect = 0.0
        for i in range(self.dim):
            phase_mod = self.phase_shift[i] + 0.2 * np.sin(x[i])
            stochastic_effect += (self.stochastic_resonance[i] * 
                                np.sin(x[i] * (1 + 0.2 * np.random.rand()) + phase_mod) * 
                                np.cos(3 * x[i] + phase_mod))
        
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
            damping_term += self.nonlinear_damping[i] * np.sin(x[i]**3) * np.exp(-x[i]**2/8)
            wave_interaction_term += self.wave_interaction[i] * np.sin(x[i]) * np.cos(x[i]**2) * self.resonance_amplitude[i]
        
        # Additional chaotic components for increased multimodality
        chaos_mutation = 0.0
        for i in range(self.dim):
            chaos_mutation += (self.chaotic_mutation[i] * 
                             np.sin(self.frequency_jitter[i] * x[i]) * 
                             np.cos(self.modulation_depth[i] * x[i]**2))
        
        # Cross-dimensional coupling for enhanced complexity
        cross_coupling_term = 0.0
        for i in range(self.dim):
            for j in range(self.dim):
                if i != j:
                    cross_coupling_term += (self.cross_coupling[i, j] * 
                                         np.sin(x[i]) * np.cos(x[j]) * 
                                         np.exp(-0.1 * (x[i] - x[j])**2))
        
        # Resonance shift for additional complexity
        resonance_shift_term = 0.0
        for i in range(self.dim):
            resonance_shift_term += self.resonance_shift[i] * np.sin(x[i]) * np.cos(3 * x[i])
        
        # High-order interaction terms for increased complexity
        high_order_term = 0.0
        for i in range(self.dim):
            for j in range(self.dim):
                for k in range(self.dim):
                    if i != j and j != k and i != k:
                        high_order_term += self.high_order_weights[i, j, k] * x[i] * x[j] * x[k]
        
        # Gaussian kernel smoothing for landscape regularization
        gaussian_term = 0.0
        for i in range(self.dim):
            gaussian_term += self.gaussian_kernel[i] * np.exp(-0.5 * (x[i]/2.0)**2)
        
        # Spectral mixing for frequency domain complexity
        spectral_term = 0.0
        for i in range(self.dim):
            spectral_term += self.spectral_mixing[i] * np.sin(3 * x[i]) * np.cos(2 * x[i])
        
        # Combined fitness with enhanced non-linearity and complexity
        return (2.5 * chaotic_component + 
                2.0 * fractal_ruggedness + 
                1.8 * quantum_decay + 
                2.5 * cubic_coupling + 
                1.8 * delayed_harmonic + 
                1.2 * dynamic_coupling + 
                0.9 * stochastic_effect + 
                0.8 * enhanced_interaction +
                0.6 * damping_term +
                0.5 * wave_interaction_term +
                0.4 * chaos_mutation +
                0.3 * cross_coupling_term +
                0.2 * resonance_shift_term +
                0.1 * high_order_term +
                0.05 * gaussian_term +
                0.05 * spectral_term)