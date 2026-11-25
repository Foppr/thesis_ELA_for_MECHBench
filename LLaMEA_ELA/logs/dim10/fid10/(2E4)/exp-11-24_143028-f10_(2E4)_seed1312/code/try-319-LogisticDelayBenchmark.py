import numpy as np

class LogisticDelayBenchmark:
    def __init__(self, dim):
        self.dim = dim
        # Initialize logistic map parameters with chaotic behavior
        self.r_values = np.random.uniform(3.57, 4.0, dim)
        # Time-delay coupling strengths
        self.delay_couplings = np.random.uniform(-0.5, 0.5, dim)
        # Multi-scale harmonic modulation frequencies and amplitudes
        self.harm_freqs = np.random.uniform(1.0, 6.0, dim)
        self.harm_ampls = np.random.uniform(0.3, 1.2, dim)
        # Memory buffer for delayed feedback
        self.memory = np.zeros((dim, 5))  # Store last 5 steps
        self.memory_index = 0
        # Dimensional conditioning factors
        self.conditioning = np.random.uniform(0.5, 2.0, dim)
        
    def f(self, x):
        # Ensure x is within bounds [-5, 5]
        x = np.clip(x, -5.0, 5.0)
        
        # Normalize inputs to [0, 1] for logistic maps
        normalized_x = (x + 5.0) / 10.0
        
        # Update memory buffer
        self.memory[:, self.memory_index] = normalized_x
        self.memory_index = (self.memory_index + 1) % 5
        
        # Compute chaotic logistic map states with delayed feedback
        states = np.zeros(self.dim)
        for i in range(self.dim):
            # Base logistic map contribution
            base_state = self.r_values[i] * normalized_x[i] * (1.0 - normalized_x[i])
            
            # Add delayed coupling from other dimensions
            delay_coupling = 0.0
            if self.memory_index > 0:
                prev_idx = (self.memory_index - 1) % 5
                for j in range(self.dim):
                    if i != j:
                        delay_coupling += self.delay_couplings[j] * self.memory[j, prev_idx]
            
            # Combine base and delayed contributions
            states[i] = base_state + delay_coupling
            
        # Apply multi-scale harmonic modulations
        fitness = 0.0
        for i in range(self.dim):
            # Harmonic modulation with multiple frequencies
            harm_mod = (self.harm_ampls[i] * 
                       (np.sin(self.harm_freqs[i] * np.pi * states[i]) + 
                        0.5 * np.sin(2 * self.harm_freqs[i] * np.pi * states[i]) +
                        0.3 * np.sin(3 * self.harm_freqs[i] * np.pi * states[i])))
            
            # Add conditioning factor and compute fitness
            conditioned_state = states[i] * self.conditioning[i]
            fitness += (conditioned_state - harm_mod)**2
            
        # Add cross-dimensional interaction with exponential weighting
        cross_term = 0.0
        for i in range(self.dim):
            for j in range(i+1, self.dim):
                # Exponential distance weighting
                dist_weight = np.exp(-0.5 * (i - j)**2 / (0.3 * self.dim))
                cross_term += (normalized_x[i] - normalized_x[j])**2 * dist_weight
        
        # Add global complexity with polynomial and trigonometric components
        return fitness + 0.2 * cross_term + 0.1 * np.sum(np.sin(2 * x)) + 0.05 * np.sum(x**4)