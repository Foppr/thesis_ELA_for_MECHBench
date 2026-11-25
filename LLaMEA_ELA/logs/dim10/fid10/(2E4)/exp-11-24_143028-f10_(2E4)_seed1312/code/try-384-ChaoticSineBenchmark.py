import numpy as np

class ChaoticSineBenchmark:
    def __init__(self, dim):
        self.dim = dim
        # Chaotic parameters for sine map
        self.sine_params = np.random.uniform(0.5, 2.0, dim)
        self.bifurcation_points = np.random.uniform(1.0, 4.0, dim)
        self.damping_factors = np.random.uniform(0.7, 1.3, dim)
        # Self-similar basin parameters
        self.basin_centers = np.random.uniform(-4.0, 4.0, dim)
        self.basin_radii = np.random.uniform(0.3, 1.5, dim)
        # Time-varying chaotic dynamics
        self.time_phase = np.random.uniform(0, 2*np.pi, dim)
        self.frequency_modulation = np.random.uniform(0.2, 0.8, dim)
        # Adaptive coupling coefficients
        self.coupling_strength = np.random.uniform(0.1, 0.5, dim)
        
    def f(self, x):
        # Ensure x is within bounds [-5, 5]
        x = np.clip(x, -5.0, 5.0)
        
        # Normalize to [0, 1] for sine map computation
        normalized_x = (x + 5.0) / 10.0
        
        # Compute chaotic sine map values with time-varying parameters
        sine_values = np.zeros(self.dim)
        for i in range(self.dim):
            # Dynamic parameter based on current position and time
            dynamic_param = self.sine_params[i] * (1.0 + 0.3 * np.cos(self.time_phase[i] + x[i]))
            
            # Sine map iteration with bifurcation point
            sine_value = normalized_x[i]
            for _ in range(15):  # Iterate to reach chaotic regime
                sine_value = np.sin(dynamic_param * np.pi * sine_value)
            
            # Apply damping factor
            sine_values[i] = sine_value * self.damping_factors[i]
        
        # Add time-varying modulation
        time_modulation = np.zeros(self.dim)
        for i in range(self.dim):
            time_modulation[i] = np.cos(self.frequency_modulation[i] * (x[i] + self.time_phase[i]))
        
        # Combine chaotic components with self-similar basins
        fitness = 0.0
        for i in range(self.dim):
            # Basin attraction term (self-similar structure)
            basin_attraction = np.exp(-((sine_values[i] - self.basin_centers[i])**2) / (2 * self.basin_radii[i]**2))
            
            # Chaotic energy term with higher-order nonlinearity
            chaotic_energy = sine_values[i]**2 + 0.3 * sine_values[i]**6 + 0.1 * sine_values[i]**8
            
            # Cross-dimensional coupling with adaptive strength
            coupling_term = 0.0
            for j in range(self.dim):
                if i != j:
                    coupling_factor = np.exp(-((sine_values[i] - sine_values[j])**2) / (0.3 + 0.2 * np.abs(sine_values[i])))
                    coupling_term += coupling_factor * time_modulation[j] * self.coupling_strength[i]
            
            # Combine all terms
            fitness += chaotic_energy + basin_attraction + coupling_term
        
        # Add global scaling and noise
        fitness = fitness / self.dim
        noise = np.random.uniform(-0.02, 0.02)
        return fitness + noise