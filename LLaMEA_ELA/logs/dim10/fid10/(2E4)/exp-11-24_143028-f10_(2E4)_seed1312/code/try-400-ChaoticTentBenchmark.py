import numpy as np

class ChaoticTentBenchmark:
    def __init__(self, dim):
        self.dim = dim
        # Chaotic parameters for logistic map
        self.logistic_params = np.random.uniform(3.5, 4.0, dim)
        self.bifurcation_memory = np.random.uniform(0.1, 0.9, dim)
        self.damping_factors = np.random.uniform(0.8, 1.2, dim)
        # Dynamic basin parameters
        self.basin_centers = np.random.uniform(-3.0, 3.0, dim)
        self.basin_radii = np.random.uniform(0.5, 2.0, dim)
        # Time-varying chaotic dynamics with memory
        self.time_phase = np.random.uniform(0, 2*np.pi, dim)
        self.frequency_modulation = np.random.uniform(0.1, 0.5, dim)
        self.memory_decay = np.random.uniform(0.01, 0.1, dim)
        # Enhanced coupling and scaling parameters
        self.coupling_strength = np.random.uniform(0.5, 2.0, dim)
        self.adaptive_scaling = np.random.uniform(0.8, 1.5, dim)
        # Memory effects for chaotic dynamics
        self.memory_history = np.zeros((10, dim))
        
    def f(self, x):
        # Ensure x is within bounds [-5, 5]
        x = np.clip(x, -5.0, 5.0)
        
        # Normalize to [0, 1] for logistic map computation
        normalized_x = (x + 5.0) / 10.0
        
        # Compute chaotic logistic map values with memory-dependent parameters
        logistic_values = np.zeros(self.dim)
        for i in range(self.dim):
            # Memory-dependent parameter based on historical values
            memory_effect = np.mean(self.memory_history[:, i]) if len(self.memory_history) > 0 else 0.0
            dynamic_param = self.logistic_params[i] * (1.0 + self.bifurcation_memory[i] * memory_effect)
            
            # Logistic map iteration with bifurcation point
            logistic_value = normalized_x[i]
            for _ in range(20):  # Iterate to reach chaotic regime
                logistic_value = dynamic_param * logistic_value * (1.0 - logistic_value)
            
            # Apply damping factor
            logistic_values[i] = logistic_value * self.damping_factors[i]
        
        # Update memory history
        self.memory_history = np.roll(self.memory_history, 1, axis=0)
        self.memory_history[0] = logistic_values
        
        # Add time-varying modulation
        time_modulation = np.zeros(self.dim)
        for i in range(self.dim):
            time_modulation[i] = np.sin(self.frequency_modulation[i] * (x[i] + self.time_phase[i]))
        
        # Combine chaotic components with dynamic basins
        fitness = 0.0
        for i in range(self.dim):
            # Basin attraction term
            basin_attraction = np.exp(-((logistic_values[i] - self.basin_centers[i])**2) / (2 * self.basin_radii[i]**2))
            
            # Chaotic energy term with enhanced nonlinearity
            chaotic_energy = logistic_values[i]**2 + 0.3 * logistic_values[i]**4 + 0.1 * logistic_values[i]**6
            
            # Enhanced cross-dimensional coupling with adaptive scaling
            coupling_term = 0.0
            for j in range(self.dim):
                if i != j:
                    coupling_factor = np.exp(-((logistic_values[i] - logistic_values[j])**2) / (0.3 * self.coupling_strength[i]))
                    coupling_term += coupling_factor * time_modulation[j] * self.adaptive_scaling[i]
            
            # Combine all terms
            fitness += chaotic_energy + basin_attraction + coupling_term
        
        # Add global scaling and noise
        fitness = fitness / self.dim
        noise = np.random.uniform(-0.01, 0.01)
        return fitness + noise