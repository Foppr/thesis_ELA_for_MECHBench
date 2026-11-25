import numpy as np

class ChaoticTentBenchmark:
    def __init__(self, dim):
        self.dim = dim
        # Enhanced chaotic parameters for sine map
        self.sine_params = np.random.uniform(0.8, 1.2, dim)
        self.bifurcation_points = np.random.uniform(2.5, 3.9, dim)
        self.damping_factors = np.random.uniform(0.7, 1.3, dim)
        # Dynamic basin parameters with enhanced complexity
        self.basin_centers = np.random.uniform(-4.0, 4.0, dim)
        self.basin_radii = np.random.uniform(0.3, 2.5, dim)
        # Time-varying chaotic dynamics with enhanced modulation
        self.time_phase = np.random.uniform(0, 2*np.pi, dim)
        self.frequency_modulation = np.random.uniform(0.2, 0.8, dim)
        # Enhanced coupling and scaling parameters
        self.coupling_strength = np.random.uniform(1.0, 3.0, dim)
        self.adaptive_scaling = np.random.uniform(0.5, 2.0, dim)
        # Additional chaotic attractor parameters for increased complexity
        self.attractor_params = np.random.uniform(0.1, 0.9, dim)
        
    def f(self, x):
        # Ensure x is within bounds [-5, 5]
        x = np.clip(x, -5.0, 5.0)
        
        # Normalize to [0, 1] for sine map computation
        normalized_x = (x + 5.0) / 10.0
        
        # Compute chaotic sine map values with enhanced nonlinearity
        sine_values = np.zeros(self.dim)
        for i in range(self.dim):
            # Enhanced dynamic parameter with multiple modulation sources
            dynamic_param = self.sine_params[i] * (1.0 + 0.2 * np.sin(self.time_phase[i] + x[i]) + 
                                                   0.1 * np.cos(2 * self.time_phase[i] + x[i]))
            
            # Sine map iteration with enhanced bifurcation behavior
            sine_value = normalized_x[i]
            for _ in range(20):  # Increased iterations for stronger chaos
                sine_value = np.sin(np.pi * dynamic_param * sine_value)
                # Additional chaotic modulation
                sine_value += 0.05 * np.sin(3 * np.pi * sine_value)
            
            # Apply damping factor and attractor influence
            sine_values[i] = sine_value * self.damping_factors[i]
        
        # Add enhanced time-varying modulation
        time_modulation = np.zeros(self.dim)
        for i in range(self.dim):
            time_modulation[i] = np.sin(self.frequency_modulation[i] * (x[i] + self.time_phase[i])) * \
                                np.cos(0.5 * self.frequency_modulation[i] * (x[i] + self.time_phase[i]))
        
        # Combine chaotic components with enhanced basin attraction
        fitness = 0.0
        for i in range(self.dim):
            # Enhanced basin attraction term with multi-modal structure
            basin_attraction = np.exp(-((sine_values[i] - self.basin_centers[i])**2) / (2 * self.basin_radii[i]**2))
            
            # Chaotic energy term with higher-order polynomial for increased complexity
            chaotic_energy = sine_values[i]**2 + 0.4 * sine_values[i]**4 + 0.15 * sine_values[i]**6 + \
                             0.05 * sine_values[i]**8
            
            # Enhanced cross-dimensional coupling with adaptive scaling
            coupling_term = 0.0
            for j in range(self.dim):
                if i != j:
                    # Enhanced coupling with distance-based weighting
                    distance = np.abs(sine_values[i] - sine_values[j])
                    coupling_factor = np.exp(-distance**2 / (0.2 * self.coupling_strength[i]))
                    coupling_term += coupling_factor * time_modulation[j] * self.adaptive_scaling[i]
            
            # Add attractor influence from other dimensions
            attractor_influence = 0.0
            for j in range(self.dim):
                if i != j:
                    attractor_influence += np.exp(-((sine_values[i] - sine_values[j])**2) / (0.5 * self.basin_radii[j]**2))
            
            # Combine all terms with improved balance
            fitness += chaotic_energy + basin_attraction + coupling_term + 0.3 * attractor_influence
        
        # Add global scaling and improved noise
        fitness = fitness / self.dim
        noise = np.random.uniform(-0.02, 0.02)
        return fitness + noise