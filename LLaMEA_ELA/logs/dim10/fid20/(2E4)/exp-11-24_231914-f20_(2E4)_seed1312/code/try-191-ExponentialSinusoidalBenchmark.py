import numpy as np

class ExponentialSinusoidalBenchmark:
    def __init__(self, dim):
        self.dim = dim
        # Initialize chaotic sinusoidal parameters with quantum-like randomness
        self.chaotic_freq = np.random.uniform(2.0, 25.0, size=dim)
        self.chaotic_amp = np.random.uniform(0.1, 4.0, size=dim)
        self.quantum_phase = np.random.uniform(0, 2*np.pi, size=dim)
        # Fractal ruggedness parameters with self-similar structure
        self.fractal_depth = np.random.randint(3, 12, size=dim)
        self.fractal_scale = np.random.uniform(0.02, 1.5, size=dim)
        # Enhanced cubic coupling with non-linear interaction weights
        self.cubic_weights = np.random.uniform(-2.0, 2.0, size=(dim, dim))
        # Multi-scale exponential decay with quantum tunneling effects
        self.decay_rates = np.random.uniform(0.01, 5.0, size=dim)
        self.tunneling_prob = np.random.uniform(0.001, 0.4, size=dim)
        # Dynamic harmonic interference with time-delayed feedback
        self.delay_freq = np.random.uniform(0.5, 12.0, size=dim)
        self.feedback_strength = np.random.uniform(0.03, 0.7, size=dim)
        # Novel dynamic coupling parameters
        self.dynamic_coupling = np.random.uniform(-3.0, 3.0, size=dim)
        self.harmonic_modulation = np.random.uniform(0.3, 3.0, size=dim)
        self.stochastic_resonance = np.random.uniform(0.05, 1.0, size=dim)
        # Additional parameters to improve landscape quality
        self.nonlinearity_factor = np.random.uniform(0.3, 2.5, size=dim)
        self.frequency_modulation = np.random.uniform(0.05, 2.0, size=dim)
        self.amplitude_scaling = np.random.uniform(0.6, 1.8, size=dim)
        # New hyper-chaotic parameters for increased complexity
        self.hyperchaos_freq = np.random.uniform(15.0, 40.0, size=dim)
        self.hyperchaos_amp = np.random.uniform(0.5, 5.0, size=dim)
        self.resonance_strength = np.random.uniform(0.2, 1.5, size=dim)
        # Multi-modal interaction weights
        self.modal_weights = np.random.uniform(-1.0, 1.0, size=(dim, dim, dim))
        # Memory-based temporal dynamics
        self.memory_decay = np.random.uniform(0.1, 0.9, size=dim)
        
    def f(self, x):
        # Scale input to [-5, 5]
        x = np.clip(x, -5.0, 5.0)
        
        # Chaotic sinusoidal component with quantum phase modulation
        chaotic_component = 0.0
        for i in range(self.dim):
            phase = self.quantum_phase[i] + np.sin(x[i]) * np.cos(x[(i+1)%self.dim])
            chaotic_component += (np.sin(self.chaotic_freq[i] * x[i] + phase) * 
                                self.chaotic_amp[i] * np.exp(-0.5 * x[i]**2))
            
        # Fractal-based ruggedness with multi-scale interference
        fractal_ruggedness = 0.0
        for i in range(self.dim):
            base_fractal = 0.0
            for depth in range(1, self.fractal_depth[i]+1):
                scale = self.fractal_scale[i] * (0.3**depth)
                freq = self.chaotic_freq[i] * (3.0**depth)
                base_fractal += np.sin(freq * x[i]) * scale
            fractal_ruggedness += base_fractal * np.cos(x[i]**2) * self.chaotic_amp[i]
            
        # Quantum-like exponential decay with tunneling probability
        quantum_decay = 0.0
        for i in range(self.dim):
            tunnel_prob = self.tunneling_prob[i] * np.exp(-0.15 * x[i]**2)
            quantum_decay += (np.exp(-self.decay_rates[i] * np.abs(x[i])) + 
                            tunnel_prob * np.sin(3 * x[i])) * self.chaotic_amp[i]
            
        # Multi-scale cubic coupling with dynamic interaction
        cubic_coupling = 0.0
        for i in range(self.dim):
            for j in range(self.dim):
                if i != j:
                    interaction = (x[i]**3) * (x[j]**2) + (x[i]**2) * (x[j]**3)
                    cubic_coupling += self.cubic_weights[i, j] * interaction
                    
        # Time-delayed harmonic feedback with chaotic interference
        delayed_harmonic = 0.0
        for i in range(self.dim):
            delay_term = np.sin(self.delay_freq[i] * x[(i-1)%self.dim]) * self.feedback_strength[i]
            delayed_harmonic += (np.sin(self.chaotic_freq[i] * x[i] + delay_term) + 
                               0.3 * np.cos(2 * self.chaotic_freq[i] * x[i] + delay_term)) * self.chaotic_amp[i]
        
        # Novel dynamic coupling mechanism
        dynamic_coupling = 0.0
        for i in range(self.dim):
            dynamic_coupling += (self.dynamic_coupling[i] * 
                               np.sin(self.harmonic_modulation[i] * x[i]) * 
                               np.exp(-0.3 * x[i]**2))
        
        # Stochastic resonance enhancement
        stochastic_effect = 0.0
        for i in range(self.dim):
            stochastic_effect += (self.stochastic_resonance[i] * 
                                np.sin(x[i] * (1 + 0.1 * np.random.rand())) * 
                                np.cos(2 * x[i]))
        
        # Additional nonlinearity and interaction terms to improve landscape quality
        additional_terms = 0.0
        for i in range(self.dim):
            # Add frequency modulation and amplitude scaling
            freq_mod = self.frequency_modulation[i] * np.sin(x[i])
            amp_scale = self.amplitude_scaling[i] * np.cos(x[i])
            additional_terms += (freq_mod * amp_scale + 
                               self.nonlinearity_factor[i] * np.sin(4 * x[i]) * np.cos(3 * x[i]))
        
        # Hyper-chaotic component for enhanced complexity
        hyperchaos_component = 0.0
        for i in range(self.dim):
            hyperchaos_component += (self.hyperchaos_amp[i] * 
                                   np.sin(self.hyperchaos_freq[i] * x[i]) * 
                                   np.cos(2 * self.hyperchaos_freq[i] * x[i]))
        
        # Resonance enhancement
        resonance_effect = 0.0
        for i in range(self.dim):
            resonance_effect += (self.resonance_strength[i] * 
                               np.sin(x[i]) * np.cos(3 * x[i]) * 
                               np.exp(-0.2 * x[i]**2))
        
        # Multi-modal interaction terms
        modal_interaction = 0.0
        for i in range(self.dim):
            for j in range(self.dim):
                for k in range(self.dim):
                    if i != j and j != k:
                        modal_interaction += (self.modal_weights[i, j, k] * 
                                            x[i] * x[j] * x[k])
        
        # Memory-based temporal dynamics
        memory_effect = 0.0
        for i in range(self.dim):
            memory_effect += (self.memory_decay[i] * np.sin(x[i]) * 
                            np.cos(2 * x[i]) * np.exp(-0.1 * x[i]**2))
        
        # Combined fitness with enhanced non-linearity and complexity
        return (2.0 * chaotic_component + 
                1.8 * fractal_ruggedness + 
                1.6 * quantum_decay + 
                2.5 * cubic_coupling + 
                1.7 * delayed_harmonic + 
                0.9 * dynamic_coupling + 
                0.7 * stochastic_effect + 
                0.6 * additional_terms +
                1.2 * hyperchaos_component +
                0.8 * resonance_effect +
                0.5 * modal_interaction +
                0.4 * memory_effect)