import numpy as np

class ChaoticSineBenchmark:
    def __init__(self, dim):
        self.dim = dim
        # Enhanced chaotic parameters with higher variability
        self.sine_params = np.random.uniform(0.05, 1.2, dim)
        self.bifurcation_points = np.random.uniform(1.0, 4.0, dim)
        self.damping_factors = np.random.uniform(0.5, 1.5, dim)
        # Complex fractal basin centers and radii
        self.basin_centers = np.random.uniform(-4.0, 4.0, dim)
        self.basin_radii = np.random.uniform(0.2, 3.0, dim)
        # Time-varying chaotic dynamics with frequency modulation
        self.time_phase = np.random.uniform(0, 4*np.pi, dim)
        self.frequency_modulation = np.random.uniform(0.05, 1.0, dim)
        # Fractal structure with multi-scale scaling factors
        self.fractal_dimensions = np.random.uniform(0.3, 2.0, dim)
        self.fractal_scaling = np.random.uniform(0.05, 1.5, dim)
        # Stronger coupling and nonlinearity for increased complexity
        self.coupling_strength = np.random.uniform(1.0, 3.0, dim)
        self.nonlinearity_factor = np.random.uniform(0.2, 1.0, dim)
        # Additional spectral components for frequency domain challenge
        self.spectral_factors = np.random.uniform(0.1, 2.0, dim)
        self.frequency_shifts = np.random.uniform(-0.5, 0.5, dim)
        
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
            
            # Sine map iteration with bifurcation point and higher iterations
            sine_value = normalized_x[i]
            for _ in range(20):  # More iterations for stronger chaos
                sine_value = np.sin(np.pi * dynamic_param * sine_value)
            
            # Apply damping factor
            sine_values[i] = sine_value * self.damping_factors[i]
        
        # Add time-varying modulation with spectral components
        time_modulation = np.zeros(self.dim)
        for i in range(self.dim):
            time_modulation[i] = np.sin(self.frequency_modulation[i] * (x[i] + self.time_phase[i])) + \
                                self.spectral_factors[i] * np.cos(self.frequency_shifts[i] * x[i])
        
        # Combine chaotic components with dynamic basins and fractal structure
        fitness = 0.0
        for i in range(self.dim):
            # Basin attraction term with fractal scaling
            basin_attraction = np.exp(-((sine_values[i] - self.basin_centers[i])**2) / (2 * self.basin_radii[i]**2))
            
            # Chaotic energy term with enhanced fractal structure and spectral components
            fractal_energy = sine_values[i]**2 + 0.3 * sine_values[i]**4 + \
                            self.fractal_scaling[i] * np.sin(self.fractal_dimensions[i] * np.pi * sine_values[i]) + \
                            self.nonlinearity_factor[i] * sine_values[i]**6 + \
                            0.1 * np.sin(5 * sine_values[i]) * np.cos(3 * x[i])
            
            # Cross-dimensional coupling with time modulation and fractal structure
            coupling_term = 0.0
            for j in range(self.dim):
                if i != j:
                    coupling_factor = np.exp(-((sine_values[i] - sine_values[j])**2) / (0.3 * self.coupling_strength[i]))
                    coupling_term += coupling_factor * time_modulation[j]
            
            # Add a new term for better conditioning and increased complexity
            interaction_term = 0.15 * np.sum(np.abs(sine_values[i] - sine_values))
            
            # Add spectral interference term
            spectral_interference = 0.05 * np.sin(self.spectral_factors[i] * x[i]) * np.cos(self.frequency_shifts[i] * x[i])
            
            # Combine all terms
            fitness += fractal_energy + basin_attraction + coupling_term + interaction_term + spectral_interference
        
        # Add global scaling and noise
        fitness = fitness / self.dim
        noise = np.random.uniform(-0.02, 0.02)
        return fitness + noise