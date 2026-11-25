import numpy as np

class ChaoticTentBenchmark:
    def __init__(self, dim):
        self.dim = dim
        # Hyperchaotic parameters for sine map with increased complexity
        self.sine_params = np.random.uniform(0.05, 1.2, dim)
        self.bifurcation_points = np.random.uniform(2.0, 4.0, dim)
        self.damping_factors = np.random.uniform(0.5, 1.5, dim)
        # Enhanced dynamic basin parameters
        self.basin_centers = np.random.uniform(-4.0, 4.0, dim)
        self.basin_radii = np.random.uniform(0.3, 2.5, dim)
        self.basin_strengths = np.random.uniform(0.8, 2.0, dim)
        # Time-varying chaotic dynamics with higher frequency
        self.time_phase = np.random.uniform(0, 4*np.pi, dim)
        self.frequency_modulation = np.random.uniform(0.2, 1.0, dim)
        # Ultra-enhanced coupling and scaling parameters (mutated)
        self.coupling_strength = np.random.uniform(0.5, 2.5, dim)
        self.adaptive_scaling = np.random.uniform(0.7, 2.0, dim)
        self.hyperchaos_factor = np.random.uniform(1.5, 3.0, dim)
        
    def f(self, x):
        # Ensure x is within bounds [-5, 5]
        x = np.clip(x, -5.0, 5.0)
        
        # Normalize to [0, 1] for sine map computation
        normalized_x = (x + 5.0) / 10.0
        
        # Compute hyperchaotic sine map values with time-varying parameters
        sine_values = np.zeros(self.dim)
        for i in range(self.dim):
            # Dynamic parameter based on current position and time with hyperchaos
            dynamic_param = self.sine_params[i] * (1.0 + 0.5 * np.sin(self.time_phase[i] + x[i]))
            
            # Sine map iteration with bifurcation point and multiple iterations
            sine_value = normalized_x[i]
            for _ in range(25):  # More iterations to reach hyperchaotic regime
                sine_value = np.sin(np.pi * dynamic_param * sine_value)
                sine_value = np.sin(np.pi * self.bifurcation_points[i] * sine_value)  # Additional nonlinearity
            
            # Apply damping factor and hyperchaos factor
            sine_values[i] = sine_value * self.damping_factors[i] * self.hyperchaos_factor[i]
        
        # Add time-varying modulation with higher frequency
        time_modulation = np.zeros(self.dim)
        for i in range(self.dim):
            time_modulation[i] = np.sin(self.frequency_modulation[i] * (x[i] + self.time_phase[i]))
        
        # Combine chaotic components with dynamic basins and enhanced coupling
        fitness = 0.0
        for i in range(self.dim):
            # Basin attraction term with increased strength
            basin_attraction = self.basin_strengths[i] * np.exp(-((sine_values[i] - self.basin_centers[i])**2) / (2 * self.basin_radii[i]**2))
            
            # Chaotic energy term with higher-order nonlinearities
            chaotic_energy = sine_values[i]**2 + 0.5 * sine_values[i]**4 + 0.25 * sine_values[i]**6 + 0.1 * sine_values[i]**8
            
            # Enhanced cross-dimensional coupling with adaptive scaling and hyperchaos
            coupling_term = 0.0
            for j in range(self.dim):
                if i != j:
                    coupling_factor = np.exp(-((sine_values[i] - sine_values[j])**2) / (0.3 * self.coupling_strength[i]))
                    coupling_term += coupling_factor * time_modulation[j] * self.adaptive_scaling[i] * self.hyperchaos_factor[i]
            
            # Combine all terms
            fitness += chaotic_energy + basin_attraction + coupling_term
        
        # Add global scaling and noise with higher variance (mutated)
        fitness = fitness / self.dim
        noise = np.random.uniform(-0.05, 0.05)
        return fitness + noise