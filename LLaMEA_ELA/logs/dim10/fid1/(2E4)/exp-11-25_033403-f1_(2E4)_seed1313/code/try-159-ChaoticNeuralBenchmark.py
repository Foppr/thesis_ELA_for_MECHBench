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
        
    def f(self, x):
        # Scale input to [-5, 5] domain
        x = np.clip(x, -5.0, 5.0)
        
        # Initialize chaotic neural dynamics
        state = np.zeros(self.dim)
        energy = 0.0
        
        # Simulate chaotic dynamics over time steps
        for t in range(100):
            # Update neural states with recurrent connections and time-varying parameters
            new_state = np.tanh(np.dot(self.weights, state) + self.biases)
            
            # Apply time-varying modulation
            for i in range(self.dim):
                new_state[i] *= (1.0 + 0.5 * np.sin(self.time_varying_params[i] * t))
            
            # Add recurrent feedback with dynamic strength
            state = (1.0 - self.recurrence_strength) * state + self.recurrence_strength * new_state
            
            # Accumulate energy based on state deviation from attractors
            if t > 50:  # Only accumulate after transient period
                for i in range(self.dim):
                    # Calculate distance to nearest attractor state
                    distances = [np.linalg.norm(state[i] - attractor) for attractor in self.attractor_states[i]]
                    min_distance = min(distances)
                    energy += min_distance**2
        
        # Add basin of attraction terms
        basin_terms = 0.0
        for i in range(self.dim):
            # Create multiple local minima using sigmoidal basin functions
            basin_term = 0.0
            for j in range(5):
                center = self.attractor_states[i, j]
                width = np.random.uniform(0.5, 2.0)
                basin_term += 1.0 / (1.0 + np.exp(-width * (x[i] - center)))
            basin_terms += basin_term
            
        # Add coupling between dimensions with chaotic interaction
        coupling_terms = 0.0
        for i in range(self.dim):
            for j in range(i+1, self.dim):
                # Chaotic coupling based on distance and time-varying parameters
                dist = np.abs(x[i] - x[j])
                coupling = np.sin(dist * self.time_varying_params[i]) * np.cos(dist * self.time_varying_params[j])
                coupling_terms += coupling
                
        # Add chaotic modulation with exponential decay
        chaos_modulation = 0.0
        for i in range(self.dim):
            # Create chaotic behavior using logistic map-like dynamics
            chaos_modulation += np.sin(x[i])**2 + np.cos(x[i])**2
            
        # Combine all components with adaptive weights
        total = 0.3 * energy/50.0 + 0.4 * basin_terms + 0.3 * coupling_terms + 0.2 * chaos_modulation
        
        return total