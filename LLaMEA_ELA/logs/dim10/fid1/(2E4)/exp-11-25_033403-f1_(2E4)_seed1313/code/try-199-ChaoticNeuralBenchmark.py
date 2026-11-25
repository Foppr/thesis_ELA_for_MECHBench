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
        self.frequency_modulation = np.random.uniform(0.5, 2.0, dim)
        self.amplitude_modulation = np.random.uniform(0.1, 1.0, dim)
        self.phase_shift = np.random.uniform(0, 2*np.pi, dim)
        # Quantum-inspired parameters
        self.quantum_coeff = np.random.uniform(0.15, 0.45, dim)  # Slightly reduced range
        self.fractal_exponent = np.random.uniform(1.1, 2.5, dim)
        self.harmonic_order = np.random.randint(3, 8, dim)
        # Additional chaotic coupling parameters
        self.coupling_strength = np.random.uniform(0.01, 0.5, (dim, dim))
        self.coupling_phase = np.random.uniform(0, 2*np.pi, (dim, dim))
        # New enhanced parameters for better landscape control
        self.interference_modulation = np.random.uniform(0.8, 1.5, dim)
        self.stochastic_amplitude = np.random.uniform(0.05, 0.3, dim)
        self.energy_damping = np.random.uniform(0.9, 0.99, dim)
        # Mutated parameters for enhanced complexity
        self.harmonic_coupling_factor = np.random.uniform(0.6, 1.4, (dim, dim))  # Changed range
        self.stochastic_resonance_strength = np.random.uniform(0.02, 0.15, dim)
        self.fractal_modulation = np.random.uniform(0.3, 0.7, dim)
        
    def f(self, x):
        # Scale input to [-5, 5] domain
        x = np.clip(x, -5.0, 5.0)
        
        # Initialize chaotic neural dynamics
        state = np.zeros(self.dim)
        energy = 0.0
        
        # Simulate chaotic dynamics over time steps
        for t in range(150):
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
            if t > 75:  # Only accumulate after longer transient period
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
                width = np.random.uniform(0.5, 2.0)
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
                          (1.0 + 0.1 * np.sin(self.fractal_exponent[i] * dist)) * \
                          (1.0 + 0.1 * np.cos(self.fractal_exponent[j] * dist))
                # Mutated coupling with harmonic factors and stochastic resonance
                coupling *= self.harmonic_coupling_factor[i, j]
                coupling += self.stochastic_resonance_strength[i] * np.random.uniform(-0.5, 0.5)
                coupling_terms += coupling
                
        # Add chaotic modulation with exponential decay and additional harmonic terms
        chaos_modulation = 0.0
        for i in range(self.dim):
            # Create chaotic behavior using logistic map-like dynamics with harmonic components
            base_term = np.sin(x[i])**2 + np.cos(x[i])**2
            harmonic_term = 0.0
            for k in range(1, self.harmonic_order[i]+1):
                harmonic_term += (1.0/k) * np.sin(k * x[i]) * np.cos(k * x[i])
            chaos_modulation += base_term + 0.3 * harmonic_term
            
        # Add quantum-inspired fractal potential terms with enhanced interference
        fractal_terms = 0.0
        for i in range(self.dim):
            # Fractal potential with multiple scaling factors and stochastic modulation
            fractal_potential = 0.0
            for k in range(1, 6):
                scale = 1.0 / (k**self.fractal_exponent[i])
                fractal_potential += scale * np.sin(scale * x[i]) * np.cos(scale * x[i])
            # Add stochastic modulation to increase complexity and mutated fractal modulation
            fractal_terms += fractal_potential * (1.0 + self.stochastic_amplitude[i] * np.random.uniform(-1, 1)) * \
                            (1.0 + self.fractal_modulation[i] * np.sin(x[i]))
            
        # Combine all components with adaptive weights and enhanced quantum interference
        total = 0.25 * energy/75.0 + 0.3 * basin_terms + 0.2 * coupling_terms + 0.15 * chaos_modulation + 0.1 * fractal_terms
        
        # Add quantum interference term to enhance landscape complexity
        quantum_interference = 0.0
        for i in range(self.dim):
            for j in range(i+1, self.dim):
                interference = np.sin(self.quantum_coeff[i] * (x[i] - x[j])) * \
                              np.cos(self.quantum_coeff[j] * (x[i] - x[j]))
                quantum_interference += interference
        
        total += 0.05 * quantum_interference
        
        return total