import numpy as np

class ChaoticNeuralBenchmark:
    def __init__(self, dim):
        self.dim = dim
        # Initialize chaotic neural network parameters
        self.weights = np.random.uniform(-2.0, 2.0, (dim, dim))
        self.biases = np.random.uniform(-1.0, 1.0, dim)
        self.time_varying_params = np.random.uniform(0.1, 1.0, dim)
        self.attractor_states = np.random.uniform(-3.0, 3.0, (dim, 5))
        self.recurrence_strength = np.random.uniform(0.5, 2.0, dim)
        # Add new parameters for improved landscape complexity
        self.frequency_modulation = np.random.uniform(0.5, 5.0, dim)
        self.amplitude_modulation = np.random.uniform(0.1, 3.0, dim)
        self.phase_shift = np.random.uniform(0, 4*np.pi, dim)
        # Quantum-inspired parameters - Modified coefficients
        self.quantum_coeff = np.random.uniform(0.2, 1.5, dim)  # Increased range
        self.fractal_exponent = np.random.uniform(1.8, 4.5, dim)  # Increased range
        self.harmonic_order = np.random.randint(3, 15, dim)
        # Additional chaotic coupling parameters
        self.coupling_strength = np.random.uniform(0.01, 1.0, (dim, dim))
        self.coupling_phase = np.random.uniform(0, 4*np.pi, (dim, dim))
        # New enhanced parameters for better landscape control
        self.interference_modulation = np.random.uniform(1.2, 3.5, dim)  # Increased range
        self.stochastic_amplitude = np.random.uniform(0.15, 1.2, dim)  # Increased range
        self.energy_damping = np.random.uniform(0.8, 0.999, dim)
        # Additional high-order chaotic parameters
        self.chaos_order = np.random.randint(5, 20, dim)
        self.fractal_scale = np.random.uniform(0.1, 2.0, dim)
        self.quantum_phase = np.random.uniform(0, 3*np.pi, dim)
        self.stochastic_frequency = np.random.uniform(0.5, 3.0, dim)
        # Enhanced parameters for better fitness performance
        self.nonlinearity_strength = np.random.uniform(1.2, 5.5, dim)  # Increased range
        self.resonance_frequency = np.random.uniform(0.1, 2.0, dim)
        self.coupling_decay = np.random.uniform(0.01, 0.5, (dim, dim))
        self.modulation_depth = np.random.uniform(0.6, 2.5, dim)  # Increased range
        # Additional chaotic complexity parameters
        self.ergodic_coeff = np.random.uniform(0.02, 0.35, dim)  # Increased range
        self.dissipation_rate = np.random.uniform(0.001, 0.05, dim)
        self.spectral_density = np.random.uniform(0.1, 2.0, dim)
        self.coupling_magnitude = np.random.uniform(0.5, 3.0, (dim, dim))
        self.frequency_shift = np.random.uniform(-1.0, 1.0, dim)
        self.harmonic_amplitude = np.random.uniform(0.15, 2.5, dim)  # Increased range
        self.fractal_density = np.random.uniform(0.6, 3.5, dim)  # Increased range
        self.quantum_entropy = np.random.uniform(0.01, 0.25, dim)  # Increased range
        self.stochastic_decay = np.random.uniform(0.9, 0.999, dim)
        # High-order coupling and interference terms
        self.high_order_coupling = np.random.uniform(0.01, 0.5, (dim, dim, dim))
        self.interference_frequency = np.random.uniform(1.2, 5.5, (dim, dim))  # Increased range
        self.fractal_multiplier = np.random.uniform(0.6, 2.8, dim)  # Increased range
        # Enhanced spectral and ergodic parameters
        self.spectral_modulation = np.random.uniform(0.6, 2.2, dim)  # Increased range
        self.ergodic_shift = np.random.uniform(-0.15, 0.15, dim)  # Increased range
        self.fractal_coupling = np.random.uniform(0.15, 1.2, (dim, dim))  # Increased range
        self.harmonic_mixing = np.random.uniform(0.15, 0.6, dim)  # Increased range
        self.stochastic_phase = np.random.uniform(0, 2*np.pi, dim)
        self.energy_gradient = np.random.uniform(0.01, 0.25, dim)  # Increased range
        # Additional multi-scale fractal terms
        self.multi_scale_exponent = np.random.uniform(1.2, 3.2, dim)  # Increased range
        self.scale_factor = np.random.uniform(0.15, 1.0, dim)  # Increased range
        self.fractal_roughness = np.random.uniform(0.6, 2.2, dim)  # Increased range
        # Enhanced coupling with additional phase and amplitude terms
        self.phase_coupling = np.random.uniform(0.15, 2.2, (dim, dim))  # Increased range
        self.amplitude_coupling = np.random.uniform(0.01, 0.6, (dim, dim))  # Increased range
        self.coupling_frequency = np.random.uniform(0.5, 3.5, (dim, dim))  # Increased range
        # New mutation: Increased complexity with additional fractal and quantum terms
        self.fractal_dimensionality = np.random.uniform(1.2, 3.8, dim)  # Increased range
        self.quantum_mixing = np.random.uniform(0.08, 0.6, dim)  # Increased range
        self.multi_fractal_exponent = np.random.uniform(0.6, 2.8, dim)  # Increased range
        self.stochastic_coupling = np.random.uniform(0.15, 1.8, (dim, dim))  # Increased range
        self.coupling_oscillation = np.random.uniform(0.5, 3.5, (dim, dim))  # Increased range
        self.harmonic_resonance = np.random.uniform(0.25, 2.0, dim)  # Increased range
        self.ergodic_mixing = np.random.uniform(0.08, 0.45, dim)  # Increased range
        self.multi_scale_coupling = np.random.uniform(0.15, 2.2, (dim, dim))  # Increased range
        self.fractal_frequency = np.random.uniform(0.15, 4.5, dim)  # Increased range
        self.quantum_harmonic = np.random.uniform(0.6, 3.5, dim)  # Increased range
        self.stochastic_oscillation = np.random.uniform(0.01, 0.35, dim)  # Increased range
        self.multi_resonance_order = np.random.randint(2, 12, dim)  # Increased range
        self.fractal_damping = np.random.uniform(0.9, 0.996, dim)  # Increased range
        
    def f(self, x):
        # Scale input to [-5, 5] domain
        x = np.clip(x, -5.0, 5.0)
        
        # Initialize chaotic neural dynamics
        state = np.zeros(self.dim)
        energy = 0.0
        
        # Simulate chaotic dynamics over time steps with enhanced complexity
        for t in range(300):
            # Update neural states with recurrent connections and time-varying parameters
            new_state = np.tanh(np.dot(self.weights, state) + self.biases)
            
            # Apply time-varying modulation with frequency and amplitude
            for i in range(self.dim):
                new_state[i] *= (1.0 + self.amplitude_modulation[i] * 
                               np.sin(self.frequency_modulation[i] * t + self.phase_shift[i]))
            
            # Add recurrent feedback with dynamic strength and energy damping
            state = (1.0 - self.recurrence_strength) * state + self.recurrence_strength * new_state
            state *= self.energy_damping
            
            # Accumulate energy based on state deviation from attractors
            if t > 150:  # Only accumulate after longer transient period
                for i in range(self.dim):
                    # Calculate distance to nearest attractor state
                    distances = [np.linalg.norm(state[i] - attractor) for attractor in self.attractor_states[i]]
                    min_distance = min(distances)
                    energy += min_distance**2
        
        # Add basin of attraction terms with modified sigmoidal functions and quantum interference
        basin_terms = 0.0
        for i in range(self.dim):
            # Create multiple local minima using modified sigmoidal basin functions
            basin_term = 0.0
            for j in range(5):
                center = self.attractor_states[i, j]
                width = np.random.uniform(0.5, 3.0)
                # Modified sigmoid with exponential scaling and quantum interference
                sigmoid_component = 1.0 / (1.0 + np.exp(-width * (x[i] - center)))
                quantum_component = np.sin(self.quantum_coeff[i] * (x[i] - center)) * \
                                  np.exp(-0.5 * ((x[i] - center) / (width * 0.5))**2)
                basin_term += sigmoid_component * quantum_component
            basin_terms += basin_term
            
        # Add coupling between dimensions with chaotic interaction and fractal harmonic terms
        coupling_terms = 0.0
        for i in range(self.dim):
            for j in range(i+1, self.dim):
                # Chaotic coupling based on distance and time-varying parameters
                dist = np.abs(x[i] - x[j])
                # Enhanced coupling with phase modulation and fractal scaling
                coupling = np.sin(dist * self.time_varying_params[i]) * \
                          np.cos(dist * self.time_varying_params[j]) * \
                          np.exp(-0.1 * dist) * \
                          (1.0 + 0.2 * np.sin(self.fractal_exponent[i] * dist)) * \
                          (1.0 + 0.2 * np.cos(self.fractal_exponent[j] * dist))
                coupling_terms += coupling
                
        # Add chaotic modulation with exponential decay and additional harmonic terms
        chaos_modulation = 0.0
        for i in range(self.dim):
            # Create chaotic behavior using logistic map-like dynamics with harmonic components
            base_term = np.sin(x[i])**2 + np.cos(x[i])**2
            harmonic_term = 0.0
            for k in range(1, self.harmonic_order[i]+1):
                harmonic_term += (1.0/k) * np.sin(k * x[i]) * np.cos(k * x[i])
            chaos_modulation += base_term + 0.6 * harmonic_term
            
        # Add quantum-inspired fractal potential terms with enhanced interference
        fractal_terms = 0.0
        for i in range(self.dim):
            # Fractal potential with multiple scaling factors and stochastic modulation
            fractal_potential = 0.0
            for k in range(1, 12):
                scale = 1.0 / (k**self.fractal_exponent[i])
                fractal_potential += scale * np.sin(scale * x[i]) * np.cos(scale * x[i])
            # Add stochastic modulation to increase complexity
            fractal_terms += fractal_potential * (1.0 + self.stochastic_amplitude[i] * np.random.uniform(-1, 1))
            
        # Combine all components with adaptive weights and enhanced quantum interference
        total = 0.2 * energy/150.0 + 0.35 * basin_terms + 0.25 * coupling_terms + 0.15 * chaos_modulation + 0.05 * fractal_terms
        
        # Add quantum interference term to enhance landscape complexity
        quantum_interference = 0.0
        for i in range(self.dim):
            for j in range(i+1, self.dim):
                interference = np.sin(self.quantum_coeff[i] * (x[i] - x[j])) * \
                              np.cos(self.quantum_coeff[j] * (x[i] - x[j]))
                quantum_interference += interference
        
        total += 0.05 * quantum_interference
        
        # Add high-order fractal and stochastic components for increased complexity
        high_order_terms = 0.0
        for i in range(self.dim):
            # Add higher order polynomial terms with enhanced nonlinearity
            poly_term = 0.0
            for k in range(1, self.chaos_order[i] + 1):
                poly_term += (x[i]**k) / (k * self.fractal_scale[i])
            high_order_terms += poly_term
            
        total += 0.03 * high_order_terms
        
        # Add enhanced multimodal components for better optimization challenge
        multimodal_terms = 0.0
        for i in range(self.dim):
            # Enhanced multimodal terms with resonance and modulation
            modulated_term = 0.0
            for k in range(1, 8):
                freq = self.resonance_frequency[i] * k
                amp = self.modulation_depth[i] / (k**2)
                modulated_term += amp * np.sin(freq * x[i]) * np.cos(freq * x[i])
            multimodal_terms += modulated_term
            
        total += 0.05 * multimodal_terms
        
        # Add high-order coupling terms for additional complexity
        high_order_coupling = 0.0
        for i in range(self.dim):
            for j in range(self.dim):
                for k in range(self.dim):
                    if i != j and j != k:
                        coupling_val = self.high_order_coupling[i, j, k] * np.sin(x[i] + x[j] - x[k])
                        high_order_coupling += coupling_val
                        
        total += 0.02 * high_order_coupling
        
        # Add spectral density and fractal interference terms
        spectral_terms = 0.0
        for i in range(self.dim):
            spectral_term = 0.0
            for k in range(1, 10):
                spectral_term += (self.spectral_density[i] / k) * np.sin(k * x[i]) * np.cos(k * x[i])
            spectral_terms += spectral_term
            
        total += 0.02 * spectral_terms
        
        # Add chaotic ergodic and dissipation components
        ergodic_terms = 0.0
        for i in range(self.dim):
            ergodic_term = self.ergodic_coeff[i] * np.exp(-self.dissipation_rate[i] * x[i]**2)
            ergodic_terms += ergodic_term
            
        total += 0.01 * ergodic_terms
        
        # Add enhanced multi-scale fractal terms
        multi_scale_terms = 0.0
        for i in range(self.dim):
            scale_term = 0.0
            for k in range(1, 6):
                scale_factor = self.scale_factor[i] * (k**self.multi_scale_exponent[i])
                scale_term += np.sin(scale_factor * x[i]) * np.cos(scale_factor * x[i])
            multi_scale_terms += scale_term
            
        total += 0.02 * multi_scale_terms
        
        # Add enhanced fractal coupling terms
        fractal_coupling_terms = 0.0
        for i in range(self.dim):
            for j in range(i+1, self.dim):
                coupling_val = self.fractal_coupling[i, j] * np.sin(self.fractal_density[i] * (x[i] - x[j]))
                fractal_coupling_terms += coupling_val
                
        total += 0.03 * fractal_coupling_terms
        
        # Add enhanced harmonic mixing terms
        harmonic_mixing_terms = 0.0
        for i in range(self.dim):
            mixing_term = 0.0
            for k in range(1, 6):
                mixing_term += self.harmonic_mixing[i] * np.sin(k * x[i]) * np.cos(k * x[i])
            harmonic_mixing_terms += mixing_term
            
        total += 0.02 * harmonic_mixing_terms
        
        # Add enhanced phase coupling terms
        phase_coupling_terms = 0.0
        for i in range(self.dim):
            for j in range(i+1, self.dim):
                phase_val = self.phase_coupling[i, j] * np.sin(x[i] + x[j] + self.stochastic_phase[i])
                phase_coupling_terms += phase_val
                
        total += 0.01 * phase_coupling_terms
        
        # Add enhanced amplitude coupling terms
        amplitude_coupling_terms = 0.0
        for i in range(self.dim):
            for j in range(i+1, self.dim):
                amp_val = self.amplitude_coupling[i, j] * np.sin(x[i] * x[j])
                amplitude_coupling_terms += amp_val
                
        total += 0.01 * amplitude_coupling_terms
        
        # Add new mutation terms to increase landscape complexity
        # Multi-fractal coupling with enhanced quantum mixing
        multi_fractal_coupling = 0.0
        for i in range(self.dim):
            for j in range(i+1, self.dim):
                multi_term = (self.stochastic_coupling[i, j] * 
                            np.sin(self.multi_fractal_exponent[i] * x[i]) * 
                            np.cos(self.multi_fractal_exponent[j] * x[j]))
                multi_fractal_coupling += multi_term
                
        total += 0.03 * multi_fractal_coupling
        
        # Quantum harmonic resonance with fractal frequency modulation
        quantum_harmonic_terms = 0.0
        for i in range(self.dim):
            freq_mod = self.fractal_frequency[i] * np.sin(x[i])
            quantum_harmonic_terms += (self.quantum_harmonic[i] * 
                                     np.sin(freq_mod * x[i]) * 
                                     np.cos(freq_mod * x[i]))
            
        total += 0.02 * quantum_harmonic_terms
        
        # Enhanced stochastic oscillation terms
        stochastic_oscillation_terms = 0.0
        for i in range(self.dim):
            stochastic_oscillation_terms += self.stochastic_oscillation[i] * np.sin(x[i]**2)
            
        total += 0.01 * stochastic_oscillation_terms
        
        # Multi-resonance harmonic terms
        multi_resonance_terms = 0.0
        for i in range(self.dim):
            resonance_term = 0.0
            for k in range(1, self.multi_resonance_order[i] + 1):
                resonance_term += np.sin(k * x[i]) * np.cos(k * x[i])
            multi_resonance_terms += resonance_term
            
        total += 0.02 * multi_resonance_terms
        
        # Fractal damping and energy gradient terms
        fractal_damping_terms = 0.0
        for i in range(self.dim):
            fractal_damping_terms += self.fractal_damping[i] * np.exp(-x[i]**2)
            
        total += 0.01 * fractal_damping_terms
        
        # Multi-scale coupling with enhanced ergodic mixing
        multi_scale_ergodic = 0.0
        for i in range(self.dim):
            for j in range(i+1, self.dim):
                multi_scale_ergodic += (self.multi_scale_coupling[i, j] * 
                                      np.sin(self.ergodic_mixing[i] * x[i]) * 
                                      np.cos(self.ergodic_mixing[j] * x[j]))
                
        total += 0.02 * multi_scale_ergodic
        
        return total