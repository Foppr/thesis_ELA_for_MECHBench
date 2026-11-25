import numpy as np

class ChaoticSineBenchmark:
    def __init__(self, dim):
        self.dim = dim
        # Chaotic parameters for logistic map
        self.logistic_params = np.random.uniform(3.5, 4.0, dim)
        self.bifurcation_points = np.random.uniform(2.0, 4.0, dim)
        self.damping_factors = np.random.uniform(0.7, 1.3, dim)
        # Dynamic basin parameters
        self.basin_centers = np.random.uniform(-4.0, 4.0, dim)
        self.basin_radii = np.random.uniform(0.3, 2.5, dim)
        # Time-varying chaotic dynamics
        self.time_phase = np.random.uniform(0, 2*np.pi, dim)
        self.frequency_modulation = np.random.uniform(0.05, 0.8, dim)
        # Self-similar fractal structure parameters
        self.fractal_dimensions = np.random.uniform(0.3, 1.7, dim)
        self.fractal_scaling = np.random.uniform(0.05, 0.95, dim)
        # Additional coupling and interaction terms
        self.coupling_strength = np.random.uniform(0.5, 2.0, dim)
        self.interaction_exponent = np.random.uniform(1.0, 3.0, dim)
        
    def f(self, x):
        # Ensure x is within bounds [-5, 5]
        x = np.clip(x, -5.0, 5.0)
        
        # Normalize to [0, 1] for logistic map computation
        normalized_x = (x + 5.0) / 10.0
        
        # Compute chaotic logistic map values with time-varying parameters
        logistic_values = np.zeros(self.dim)
        for i in range(self.dim):
            # Dynamic parameter based on current position and time
            dynamic_param = self.logistic_params[i] * (1.0 + 0.3 * np.sin(self.time_phase[i] + x[i]))
            
            # Logistic map iteration with bifurcation point
            logistic_value = normalized_x[i]
            for _ in range(15):  # Iterate to reach chaotic regime
                logistic_value = dynamic_param * logistic_value * (1.0 - logistic_value)
            
            # Apply damping factor
            logistic_values[i] = logistic_value * self.damping_factors[i]
        
        # Add time-varying modulation
        time_modulation = np.zeros(self.dim)
        for i in range(self.dim):
            time_modulation[i] = np.cos(self.frequency_modulation[i] * (x[i] + self.time_phase[i]))
        
        # Combine chaotic components with dynamic basins and fractal structure
        fitness = 0.0
        for i in range(self.dim):
            # Basin attraction term
            basin_attraction = np.exp(-((logistic_values[i] - self.basin_centers[i])**2) / (2 * self.basin_radii[i]**2))
            
            # Chaotic energy term with fractal scaling and enhanced complexity
            fractal_energy = logistic_values[i]**2 + 0.3 * logistic_values[i]**4 + \
                            self.fractal_scaling[i] * np.sin(self.fractal_dimensions[i] * np.pi * logistic_values[i]) + \
                            0.1 * logistic_values[i]**6
            
            # Cross-dimensional coupling with time modulation and fractal structure
            coupling_term = 0.0
            for j in range(self.dim):
                if i != j:
                    coupling_factor = self.coupling_strength[i] * np.exp(-((logistic_values[i] - logistic_values[j])**2) / (2 * self.interaction_exponent[i]))
                    coupling_term += coupling_factor * time_modulation[j]
            
            # Add interaction term with distance-based scaling
            distance_interaction = 0.0
            for j in range(self.dim):
                if i != j:
                    dist = np.abs(x[i] - x[j])
                    distance_interaction += (1.0 / (1.0 + dist)) * np.sin(self.fractal_dimensions[i] * np.pi * logistic_values[j])
            
            # Combine all terms
            fitness += fractal_energy + basin_attraction + coupling_term + 0.5 * distance_interaction
        
        # Add global scaling and noise
        fitness = fitness / self.dim
        noise = np.random.uniform(-0.02, 0.02)
        return fitness + noise