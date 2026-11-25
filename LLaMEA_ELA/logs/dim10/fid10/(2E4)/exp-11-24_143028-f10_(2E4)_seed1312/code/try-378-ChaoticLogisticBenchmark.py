import numpy as np

class ChaoticLogisticBenchmark:
    def __init__(self, dim):
        self.dim = dim
        # Initialize chaotic parameters for each dimension
        self.r_parameters = np.random.uniform(3.5, 4.0, dim)
        self.noise_levels = np.random.uniform(0.01, 0.1, dim)
        self.temporal_couplings = np.random.uniform(-0.2, 0.2, (dim, dim))
        # Add parameter perturbations for diversity
        self.perturbation_strength = np.random.uniform(0.1, 0.5, dim)
        
    def f(self, x):
        # Ensure x is within bounds [-5, 5]
        x = np.clip(x, -5.0, 5.0)
        
        # Normalize to [0, 1] for logistic map
        normalized_x = (x + 5.0) / 10.0
        
        # Initialize chaotic states
        chaotic_states = normalized_x.copy()
        
        # Iterate chaotic maps for multiple steps to reach attractor
        num_iterations = 50
        for _ in range(num_iterations):
            new_states = np.zeros(self.dim)
            for i in range(self.dim):
                # Logistic map with parameter perturbation
                r = self.r_parameters[i] + self.perturbation_strength[i] * np.sin(chaotic_states[i] * 10.0)
                # Apply temporal coupling from other dimensions
                coupling_term = 0.0
                for j in range(self.dim):
                    if i != j:
                        coupling_term += self.temporal_couplings[i, j] * chaotic_states[j]
                
                # Logistic map equation with noise and coupling
                new_state = r * chaotic_states[i] * (1.0 - chaotic_states[i]) + coupling_term
                # Add noise
                new_state += np.random.normal(0, self.noise_levels[i])
                new_states[i] = np.clip(new_state, 0.0, 1.0)
            chaotic_states = new_states
        
        # Compute fitness based on final chaotic states
        fitness = 0.0
        for i in range(self.dim):
            # Multiple basin terms with different scales
            basin1 = (chaotic_states[i] - 0.25)**2 + (chaotic_states[i] - 0.75)**2
            basin2 = (chaotic_states[i] - 0.5)**2 + (chaotic_states[i] - 0.3)**2
            basin3 = np.sin(10 * chaotic_states[i])**2
            
            # Combine basins with adaptive weights
            weight1 = 0.5 + 0.5 * np.sin(i)
            weight2 = 0.3 + 0.7 * np.cos(i)
            weight3 = 0.2 + 0.8 * np.tan(i)
            
            fitness += weight1 * basin1 + weight2 * basin2 + weight3 * basin3
        
        # Add cross-dimension interaction terms
        interaction_term = 0.0
        for i in range(self.dim):
            for j in range(i+1, self.dim):
                interaction_term += np.exp(-((chaotic_states[i] - chaotic_states[j])**2) / 0.1)
        
        fitness = fitness / self.dim + 0.5 * interaction_term
        
        # Add small noise for robustness
        noise = np.random.uniform(-0.01, 0.01)
        return fitness + noise