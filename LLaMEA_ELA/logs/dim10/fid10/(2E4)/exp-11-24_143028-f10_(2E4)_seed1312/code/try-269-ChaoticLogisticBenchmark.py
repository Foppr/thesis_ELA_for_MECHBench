import numpy as np

class ChaoticLogisticBenchmark:
    def __init__(self, dim):
        self.dim = dim
        # Initialize chaotic parameters for each dimension with higher variability
        self.r_values = np.random.uniform(3.8, 4.0, dim)
        self.delay_lengths = np.random.randint(1, 5, dim)
        self.noise_levels = np.random.uniform(0.02, 0.15, dim)
        # Adaptive coupling matrix with varying strengths
        self.coupling_matrix = np.random.uniform(-0.8, 0.8, (dim, dim))
        np.fill_diagonal(self.coupling_matrix, 0.0)
        # Frequency modulation parameters
        self.freq_modulation = np.random.uniform(0.5, 2.0, dim)
        # Initialize logistic map states
        self.states = np.random.uniform(0.1, 0.9, dim)
        # Memory for delayed values
        self.memory = [np.random.uniform(0.1, 0.9, dim) for _ in range(5)]
        
    def f(self, x):
        # Ensure x is within bounds [-5, 5]
        x = np.clip(x, -5.0, 5.0)
        
        # Normalize inputs to [0, 1] for logistic map
        normalized_x = (x + 5.0) / 10.0
        
        # Update chaotic states using delayed logistic maps with frequency modulation
        new_states = np.zeros(self.dim)
        for i in range(self.dim):
            # Base delayed logistic map contribution
            base_contribution = self.r_values[i] * normalized_x[i] * (1.0 - normalized_x[i])
            
            # Delayed feedback contribution
            delay_idx = self.delay_lengths[i] % len(self.memory)
            delayed_value = self.memory[delay_idx][i]
            delayed_contribution = 0.3 * delayed_value * (1.0 - delayed_value)
            
            # Coupling from other dimensions with adaptive strengths
            coupling_contribution = 0.0
            for j in range(self.dim):
                if i != j:
                    coupling_contribution += self.coupling_matrix[i, j] * normalized_x[j]
            
            # Add noise and compute new state
            new_states[i] = base_contribution + delayed_contribution + coupling_contribution + \
                           self.noise_levels[i] * np.random.uniform(-1, 1)
        
        # Update memory with current states
        self.memory.pop(0)
        self.memory.append(new_states.copy())
        
        # Compute fitness with enhanced multimodality through frequency modulation
        fitness = 0.0
        for i in range(self.dim):
            # Enhanced multimodal term with frequency modulation
            mod_term = np.sin(self.freq_modulation[i] * 2.0 * np.pi * new_states[i]) + \
                      0.3 * np.cos(self.freq_modulation[i] * 3.0 * np.pi * new_states[i]) + \
                      0.1 * np.sin(self.freq_modulation[i] * 5.0 * np.pi * new_states[i])
            fitness += (new_states[i] - mod_term)**2
            
        # Add sharp cross-dimensional interaction terms
        cross_term = 0.0
        for i in range(self.dim):
            for j in range(i+1, self.dim):
                # Sharp interaction with exponential decay
                distance = np.abs(normalized_x[i] - normalized_x[j])
                cross_term += (distance**3) * np.exp(-0.2 * (i - j)**2)
        
        return fitness + 0.15 * cross_term