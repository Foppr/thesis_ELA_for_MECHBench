import numpy as np

class ChaoticTentBenchmark:
    def __init__(self, dim):
        self.dim = dim
        # Chaotic parameters for sine map
        self.sine_params = np.random.uniform(0.1, 0.9, dim)
        self.bifurcation_points = np.random.uniform(1.5, 3.5, dim)
        self.damping_factors = np.random.uniform(0.8, 1.2, dim)
        # Dynamic basin parameters
        self.basin_centers = np.random.uniform(-3.0, 3.0, dim)
        self.basin_radii = np.random.uniform(0.5, 2.0, dim)
        # Time-varying chaotic dynamics
        self.time_phase = np.random.uniform(0, 2*np.pi, dim)
        self.frequency_modulation = np.random.uniform(0.1, 0.5, dim)
        # Enhanced coupling and scaling parameters (mutated)
        self.coupling_strength = np.random.uniform(0.3, 1.8, dim)  # Reduced range
        self.adaptive_scaling = np.random.uniform(0.9, 1.6, dim)   # Slight shift
        # New: Higher-order polynomial chaos and gradient modulation
        self.poly_degree = np.random.randint(3, 7, dim)
        self.gradient_modulation = np.random.uniform(0.5, 1.5, dim)
        
    def f(self, x):
        # Ensure x is within bounds [-5, 5]
        x = np.clip(x, -5.0, 5.0)
        
        # Normalize to [0, 1] for sine map computation
        normalized_x = (x + 5.0) / 10.0
        
        # Compute chaotic sine map values with time-varying parameters
        sine_values = np.zeros(self.dim)
        for i in range(self.dim):
            # Dynamic parameter based on current position and time
            dynamic_param = self.sine_params[i] * (1.0 + 0.3 * np.sin(self.time_phase[i] + x[i]))
            
            # Sine map iteration with bifurcation point
            sine_value = normalized_x[i]
            for _ in range(15):  # Iterate to reach chaotic regime
                sine_value = np.sin(np.pi * dynamic_param * sine_value)
            
            # Apply damping factor
            sine_values[i] = sine_value * self.damping_factors[i]
        
        # Add time-varying modulation
        time_modulation = np.zeros(self.dim)
        for i in range(self.dim):
            time_modulation[i] = np.sin(self.frequency_modulation[i] * (x[i] + self.time_phase[i]))
        
        # Combine chaotic components with dynamic basins
        fitness = 0.0
        for i in range(self.dim):
            # Basin attraction term (mutated)
            basin_attraction = np.exp(-((sine_values[i] - self.basin_centers[i])**2) / (2 * self.basin_radii[i]**2))
            
            # Chaotic energy term with altered nonlinearity (mutated)
            chaotic_energy = sine_values[i]**2 + 0.4 * sine_values[i]**4 + 0.15 * sine_values[i]**6
            
            # Add higher-order polynomial chaos component
            poly_chaos = np.sum([sine_values[i]**(self.poly_degree[i] + j) for j in range(3)])
            
            # Enhanced cross-dimensional coupling with adaptive scaling (mutated)
            coupling_term = 0.0
            for j in range(self.dim):
                if i != j:
                    coupling_factor = np.exp(-((sine_values[i] - sine_values[j])**2) / (0.4 * self.coupling_strength[i]))
                    coupling_term += coupling_factor * time_modulation[j] * self.adaptive_scaling[i]
            
            # Gradient modulation for conditioning
            grad_mod = self.gradient_modulation[i] * np.abs(x[i])
            
            # Combine all terms
            fitness += chaotic_energy + basin_attraction + coupling_term + poly_chaos + grad_mod
        
        # Add global scaling and noise (mutated)
        fitness = fitness / self.dim
        noise = np.random.uniform(-0.01, 0.01)
        return fitness + noise