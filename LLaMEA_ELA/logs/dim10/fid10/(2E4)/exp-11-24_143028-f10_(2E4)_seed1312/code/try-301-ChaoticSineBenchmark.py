import numpy as np

class ChaoticSineBenchmark:
    def __init__(self, dim):
        self.dim = dim
        # Initialize chaotic sine map parameters with dimension-dependent frequencies
        self.frequencies = np.random.uniform(1.0, 8.0, dim)
        self.amplitudes = np.random.uniform(0.5, 2.0, dim)
        self.phase_shifts = np.random.uniform(0, 2*np.pi, dim)
        # Dynamic coupling matrix with adaptive strength based on dimension
        self.coupling_matrix = np.random.uniform(-0.5, 0.5, (dim, dim))
        np.fill_diagonal(self.coupling_matrix, 0.0)
        # Basin structure parameters that vary across dimensions for adaptive ruggedness
        self.basin_strengths = np.random.uniform(0.1, 1.5, dim)
        self.basin_widths = np.random.uniform(0.2, 1.0, dim)
        # Time-dependent modulation factors for dynamic landscape evolution
        self.modulation_factors = np.random.uniform(0.8, 1.5, dim)
        
    def f(self, x):
        # Ensure x is within bounds [-5, 5]
        x = np.clip(x, -5.0, 5.0)
        
        # Normalize inputs to [0, 2*pi] for sine map
        normalized_x = (x + 5.0) / 10.0 * 2.0 * np.pi
        
        # Compute chaotic sine map contributions with dynamic coupling
        sine_states = np.zeros(self.dim)
        for i in range(self.dim):
            # Base chaotic sine contribution with frequency modulation
            base_contribution = self.amplitudes[i] * np.sin(self.frequencies[i] * normalized_x[i] + self.phase_shifts[i])
            
            # Coupling from other dimensions with adaptive weights
            coupling_contribution = 0.0
            for j in range(self.dim):
                if i != j:
                    coupling_strength = self.coupling_matrix[i, j]
                    coupling_contribution += coupling_strength * np.sin(self.frequencies[j] * normalized_x[j] + self.phase_shifts[j])
            
            # Apply time-dependent modulation and basin structure
            modulation = self.modulation_factors[i] * (np.sin(0.5 * normalized_x[i]) + 1.0)
            basin_effect = self.basin_strengths[i] * np.exp(-0.5 * ((normalized_x[i] - np.pi) / self.basin_widths[i])**2)
            
            sine_states[i] = base_contribution + coupling_contribution + modulation * basin_effect
            
        # Compute fitness with multimodal structure and varying ruggedness
        fitness = 0.0
        for i in range(self.dim):
            # Multimodal component with multiple peaks and valleys
            multimodal_term = (np.sin(2.0 * sine_states[i]) + 
                              0.7 * np.sin(4.0 * sine_states[i]) +
                              0.5 * np.sin(6.0 * sine_states[i]) +
                              0.3 * np.sin(8.0 * sine_states[i]))
            
            # Adaptive ruggedness based on dimension
            ruggedness_factor = 1.0 + 0.5 * np.sin(i * np.pi / 4.0)
            fitness += ruggedness_factor * (sine_states[i] - multimodal_term)**2
            
        # Add cross-dimensional interaction terms with dynamic coupling weights
        cross_term = 0.0
        for i in range(self.dim):
            for j in range(i+1, self.dim):
                # Dynamic weight based on frequency difference and coupling strength
                weight = np.abs(self.frequencies[i] - self.frequencies[j]) * np.abs(self.coupling_matrix[i, j])
                # Interaction with sharp transition function
                transition = 1.0 / (1.0 + np.exp(-20.0 * (sine_states[i] - sine_states[j])**2))
                cross_term += weight * transition * (sine_states[i] - sine_states[j])**2
        
        # Global scaling and noise component for increased difficulty
        return fitness + 0.4 * cross_term + 0.1 * np.sum(np.abs(x)) + \
               0.05 * np.sum(np.sin(15.0 * x) * np.cos(7.0 * x))