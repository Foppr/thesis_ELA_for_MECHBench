import numpy as np

class ChaoticTentBenchmark:
    def __init__(self, dim):
        self.dim = dim
        # Chaotic parameters for logistic map
        self.logistic_r = np.random.uniform(3.5, 4.0, dim)
        self.coupling_strength = np.random.uniform(0.5, 2.5, dim)
        self.adaptive_scaling = np.random.uniform(1.0, 2.0, dim)
        # Dynamic basin parameters
        self.basin_centers = np.random.uniform(-4.0, 4.0, dim)
        self.basin_radii = np.random.uniform(0.3, 1.8, dim)
        # Time-varying chaotic dynamics
        self.time_phase = np.random.uniform(0, 2*np.pi, dim)
        self.frequency_modulation = np.random.uniform(0.2, 0.8, dim)
        # Enhanced nonlinear terms and noise
        self.nonlinear_exponents = np.random.uniform(3.0, 7.0, dim)
        self.noise_level = np.random.uniform(0.005, 0.02, dim)
        
    def f(self, x):
        # Ensure x is within bounds [-5, 5]
        x = np.clip(x, -5.0, 5.0)
        
        # Normalize to [0, 1] for logistic map computation
        normalized_x = (x + 5.0) / 10.0
        
        # Compute chaotic logistic map values with time-varying parameters
        logistic_values = np.zeros(self.dim)
        for i in range(self.dim):
            # Dynamic parameter based on current position and time
            dynamic_r = self.logistic_r[i] * (1.0 + 0.2 * np.sin(self.time_phase[i] + x[i]))
            
            # Logistic map iteration with bifurcation point
            log_value = normalized_x[i]
            for _ in range(20):  # Iterate to reach chaotic regime
                log_value = dynamic_r * log_value * (1.0 - log_value)
            
            # Apply adaptive scaling factor
            logistic_values[i] = log_value * self.adaptive_scaling[i]
        
        # Add time-varying modulation
        time_modulation = np.zeros(self.dim)
        for i in range(self.dim):
            time_modulation[i] = np.sin(self.frequency_modulation[i] * (x[i] + self.time_phase[i]))
        
        # Combine chaotic components with dynamic basins and enhanced energy terms
        fitness = 0.0
        for i in range(self.dim):
            # Basin attraction term with modified exponential decay
            basin_attraction = np.exp(-((logistic_values[i] - self.basin_centers[i])**2) / (2 * self.basin_radii[i]**2))
            
            # Chaotic energy term with higher-order nonlinearities and altered scaling
            chaotic_energy = logistic_values[i]**self.nonlinear_exponents[i] + 0.3 * logistic_values[i]**(self.nonlinear_exponents[i]+1) + 0.05 * logistic_values[i]**(self.nonlinear_exponents[i]+2)
            
            # Enhanced cross-dimensional coupling with modified strength and time modulation
            coupling_term = 0.0
            for j in range(self.dim):
                if i != j:
                    coupling_factor = np.exp(-((logistic_values[i] - logistic_values[j])**2) / (0.3 * self.coupling_strength[i]))
                    coupling_term += coupling_factor * time_modulation[j] * self.adaptive_scaling[i]
            
            # Combine all terms with noise injection
            fitness += chaotic_energy + basin_attraction + coupling_term
        
        # Add global scaling and noise
        fitness = fitness / self.dim
        noise = np.random.normal(0, self.noise_level.mean())
        return fitness + noise