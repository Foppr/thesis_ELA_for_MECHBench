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
        self.frequency_modulation = np.random.uniform(0.5, 10.0, dim)
        self.amplitude_modulation = np.random.uniform(0.1, 5.0, dim)
        self.phase_shift = np.random.uniform(0, 8*np.pi, dim)
        # Quantum-inspired parameters
        self.quantum_coeff = np.random.uniform(0.1, 2.0, dim)
        self.fractal_exponent = np.random.uniform(1.5, 6.0, dim)
        self.harmonic_order = np.random.randint(3, 25, dim)
        # Additional chaotic coupling parameters
        self.coupling_strength = np.random.uniform(0.01, 2.0, (dim, dim))
        self.coupling_phase = np.random.uniform(0, 8*np.pi, (dim, dim))
        # New enhanced parameters for better landscape control
        self.interference_modulation = np.random.uniform(1.0, 5.0, dim)
        self.stochastic_amplitude = np.random.uniform(0.1, 2.0, dim)
        self.energy_damping = np.random.uniform(0.7, 0.9999, dim)
        # Additional high-order chaotic parameters
        self.chaos_order = np.random.randint(5, 30, dim)
        self.fractal_scale = np.random.uniform(0.05, 3.0, dim)
        self.quantum_phase = np.random.uniform(0, 6*np.pi, dim)
        self.stochastic_frequency = np.random.uniform(0.2, 5.0, dim)
        # Enhanced parameters for better fitness performance
        self.nonlinearity_strength = np.random.uniform(1.0, 8.0, dim)
        self.resonance_frequency = np.random.uniform(0.05, 3.0, dim)
        self.coupling_decay = np.random.uniform(0.005, 0.7, (dim, dim))
        self.modulation_depth = np.random.uniform(0.3, 3.0, dim)
        # Additional high-dimensional coupling parameters
        self.cross_coupling = np.random.uniform(-1.0, 1.0, (dim, dim, dim))
        self.spatial_freq = np.random.uniform(0.1, 4.0, dim)
        self.damping_factor = np.random.uniform(0.5, 0.99999, dim)
        # New multi-scale fractal parameters
        self.multi_fractal_exponent = np.random.uniform(0.5, 8.0, (dim, 3))
        self.scale_weights = np.random.uniform(0.1, 2.0, (dim, 3))
        
    def f(self, x):
        # Scale input to [-5, 5] domain
        x = np.clip(x, -5.0, 5.0)
        
        # Initialize chaotic neural dynamics
        state = np.zeros(self.dim)
        energy = 0.0
        
        # Simulate chaotic dynamics over time steps
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
            for k in range(1, 15):
                scale = 1.0 / (k**self.fractal_exponent[i])
                fractal_potential += scale * np.sin(scale * x[i]) * np.cos(scale * x[i])
            # Add stochastic modulation to increase complexity
            fractal_terms += fractal_potential * (1.0 + self.stochastic_amplitude[i] * np.random.uniform(-1, 1))
            
        # Combine all components with adaptive weights and enhanced quantum interference
        total = 0.15 * energy/150.0 + 0.30 * basin_terms + 0.20 * coupling_terms + 0.18 * chaos_modulation + 0.07 * fractal_terms
        
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
            for k in range(1, 10):
                freq = self.resonance_frequency[i] * k
                amp = self.modulation_depth[i] / (k**2)
                modulated_term += amp * np.sin(freq * x[i]) * np.cos(freq * x[i])
            multimodal_terms += modulated_term
            
        total += 0.05 * multimodal_terms
        
        # Add multi-scale fractal terms for increased complexity
        multi_fractal = 0.0
        for i in range(self.dim):
            fractal_component = 0.0
            for j in range(3):
                scale = self.scale_weights[i, j]
                exponent = self.multi_fractal_exponent[i, j]
                fractal_component += scale * np.sin(x[i] / (1.0 + exponent)) * np.cos(x[i] / (1.0 + exponent))
            multi_fractal += fractal_component
            
        total += 0.02 * multi_fractal
        
        # Add cross-dimensional coupling terms for enhanced complexity
        cross_terms = 0.0
        for i in range(self.dim):
            for j in range(self.dim):
                if i != j:
                    cross_term = 0.0
                    for k in range(self.dim):
                        cross_term += self.cross_coupling[i, j, k] * np.sin(x[k])
                    cross_terms += cross_term * np.cos(x[i]) * np.sin(x[j])
        total += 0.03 * cross_terms
        
        # Add improved fitness scaling and normalization
        return total * (1.0 + 0.1 * np.random.uniform(-1, 1))