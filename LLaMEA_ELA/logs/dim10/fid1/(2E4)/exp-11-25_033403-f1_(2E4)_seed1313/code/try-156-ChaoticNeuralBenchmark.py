import numpy as np

class ChaoticNeuralBenchmark:
    def __init__(self, dim):
        self.dim = dim
        # Initialize chaotic neural network parameters
        self.weights = np.random.uniform(-1.0, 1.0, (dim, dim))
        self.biases = np.random.uniform(-0.5, 0.5, dim)
        self.time_varying_params = np.random.uniform(0.1, 2.0, dim)
        self.attractor_states = np.random.uniform(-2.0, 2.0, (dim, 3))
        self.recurrence_strength = np.random.uniform(0.5, 1.5, dim)
        # Additional chaotic components for increased complexity
        self.frequency_modulators = np.random.uniform(0.5, 3.0, dim)
        self.amplitude_scalers = np.random.uniform(0.1, 2.0, dim)
        self.phase_shifts = np.random.uniform(0, 2*np.pi, dim)
        
    def f(self, x):
        # Scale input to [-5, 5] domain
        x = np.clip(x, -5.0, 5.0)
        
        # Chaotic neural network dynamics with enhanced complexity
        chaotic_term = 0.0
        for i in range(self.dim):
            # Recurrent connection with time-varying weights
            recurrent_sum = 0.0
            for j in range(self.dim):
                if i != j:
                    recurrent_sum += self.weights[i, j] * x[j]
            
            # Dynamic attractor state influence
            attractor_influence = 0.0
            for k in range(3):
                attractor_influence += np.exp(-0.5 * (x[i] - self.attractor_states[i, k])**2)
            
            # Time-varying parameter modulation with additional sine/cosine components
            time_mod = np.sin(self.time_varying_params[i] * x[i]) + 0.5 * np.cos(2.0 * self.time_varying_params[i] * x[i])
            
            # Enhanced chaotic component with frequency modulation and phase shifts
            freq_mod = self.frequency_modulators[i]
            amp_scaler = self.amplitude_scalers[i]
            phase_shift = self.phase_shifts[i]
            
            chaotic_component = (
                recurrent_sum + 
                self.biases[i] + 
                attractor_influence * time_mod +
                self.recurrence_strength[i] * np.sin(freq_mod * x[i] + phase_shift) *
                amp_scaler
            )
            
            chaotic_term += chaotic_component**2
            
        # Multi-scale chaotic structure with superposition and additional harmonic components
        multiscale_term = 0.0
        scales = [1.0, 0.5, 2.0, 0.25, 0.75, 1.5]
        for scale in scales:
            scale_sum = 0.0
            for i in range(self.dim):
                # Chaotic sine-wave modulation with varying frequencies and harmonic components
                harmonic_component = np.sin(scale * x[i] + np.cos(scale * x[i])) + \
                                    0.3 * np.sin(2.0 * scale * x[i]) + \
                                    0.2 * np.cos(3.0 * scale * x[i])
                scale_sum += harmonic_component
            multiscale_term += scale_sum / len(scales)
            
        # Boundary chaos with exponential weighting and additional penalty terms
        boundary_chaos = 0.0
        for i in range(self.dim):
            # Exponential decay at boundaries to create hard constraints
            boundary_penalty = np.exp(-0.5 * ((x[i] - 5.0)**2 + (x[i] + 5.0)**2))
            # Additional penalty based on distance from boundary
            distance_penalty = 1.0 / (1.0 + np.exp(-0.5 * (x[i] - 5.0))) + \
                              1.0 / (1.0 + np.exp(-0.5 * (x[i] + 5.0)))
            boundary_chaos += boundary_penalty + 0.1 * distance_penalty
            
        # Non-separability through coupling of dimensions with higher-order interactions
        coupling_term = 0.0
        for i in range(self.dim):
            for j in range(i+1, self.dim):
                # Create non-separable interactions between dimensions with cubic terms
                coupling_term += (np.sin(x[i] + x[j]) * np.cos(x[i] - x[j])) + \
                                0.3 * np.sin(x[i] * x[j]) + \
                                0.2 * (x[i]**3 + x[j]**3)
                
        # Adaptive difficulty modulation based on input position with additional polynomial terms
        difficulty_mod = 0.0
        for i in range(self.dim):
            # Varying difficulty based on distance from center with higher-order polynomials
            difficulty_mod += (1.0 + 0.5 * np.sin(2.0 * x[i])) * (np.abs(x[i]) + 0.1 * x[i]**2 + 0.05 * x[i]**3)
            
        # Additional chaotic harmonic terms to increase landscape complexity
        harmonic_term = 0.0
        for i in range(self.dim):
            harmonic_term += np.sin(3.0 * x[i]) + 0.7 * np.cos(4.0 * x[i]) + \
                            0.5 * np.sin(5.0 * x[i]) + 0.3 * np.cos(6.0 * x[i])
        
        # Combine all components with varying weights
        total = 0.3 * chaotic_term + 0.25 * multiscale_term + 0.2 * boundary_chaos + \
                0.15 * coupling_term + 0.05 * difficulty_mod + 0.05 * harmonic_term
        
        return total