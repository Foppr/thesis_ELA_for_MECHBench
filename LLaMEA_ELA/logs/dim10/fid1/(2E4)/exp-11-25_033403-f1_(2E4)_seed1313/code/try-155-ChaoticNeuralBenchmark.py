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
        
    def f(self, x):
        # Scale input to [-5, 5] domain
        x = np.clip(x, -5.0, 5.0)
        
        # Chaotic neural network dynamics
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
            
            # Time-varying parameter modulation
            time_mod = np.sin(self.time_varying_params[i] * x[i])
            
            # Combine all chaotic components
            chaotic_component = (
                recurrent_sum + 
                self.biases[i] + 
                attractor_influence * time_mod +
                self.recurrence_strength[i] * np.sin(x[i])
            )
            
            chaotic_term += chaotic_component**2
            
        # Multi-scale chaotic structure with superposition
        multiscale_term = 0.0
        scales = [1.0, 0.5, 2.0, 0.25]
        for scale in scales:
            scale_sum = 0.0
            for i in range(self.dim):
                # Chaotic sine-wave modulation with varying frequencies
                scale_sum += np.sin(scale * x[i] + np.cos(scale * x[i]))
            multiscale_term += scale_sum / len(scales)
            
        # Boundary chaos with exponential weighting
        boundary_chaos = 0.0
        for i in range(self.dim):
            # Exponential decay at boundaries to create hard constraints
            boundary_penalty = np.exp(-0.5 * ((x[i] - 5.0)**2 + (x[i] + 5.0)**2))
            boundary_chaos += boundary_penalty
            
        # Non-separability through coupling of dimensions
        coupling_term = 0.0
        for i in range(self.dim):
            for j in range(i+1, self.dim):
                # Create non-separable interactions between dimensions
                coupling_term += np.sin(x[i] + x[j]) * np.cos(x[i] - x[j])
                
        # Adaptive difficulty modulation based on input position
        difficulty_mod = 0.0
        for i in range(self.dim):
            # Varying difficulty based on distance from center
            difficulty_mod += (1.0 + 0.5 * np.sin(2.0 * x[i])) * np.abs(x[i])
            
        # Combine all components with varying weights
        total = 0.4 * chaotic_term + 0.3 * multiscale_term + 0.2 * boundary_chaos + 0.1 * coupling_term + 0.05 * difficulty_mod
        
        return total