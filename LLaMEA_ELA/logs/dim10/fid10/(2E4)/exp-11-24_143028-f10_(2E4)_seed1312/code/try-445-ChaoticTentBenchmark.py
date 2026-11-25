import numpy as np

class ChaoticTentBenchmark:
    def __init__(self, dim):
        self.dim = dim
        # Chaotic parameters for logistic map
        self.logistic_r = np.random.uniform(3.5, 4.0, dim)
        self.noise_level = np.random.uniform(0.01, 0.1, dim)
        self.damping_factors = np.random.uniform(0.7, 1.3, dim)
        # Basin parameters with enhanced fractal structure
        self.basin_centers = np.random.uniform(-4.0, 4.0, dim)
        self.basin_radii = np.random.uniform(0.3, 1.8, dim)
        self.fractal_exponent = np.random.uniform(1.2, 2.0, dim)
        # Quantum interference patterns
        self.interference_amplitude = np.random.uniform(0.2, 0.8, dim)
        self.interference_phase = np.random.uniform(0, 2*np.pi, dim)
        # Time-varying dynamics
        self.time_freq = np.random.uniform(0.5, 1.5, dim)
        self.time_offset = np.random.uniform(0, 2*np.pi, dim)
        # Coupling and chaos modulation
        self.coupling_strength = np.random.uniform(0.4, 2.0, dim)
        self.modulation_depth = np.random.uniform(0.3, 1.0, dim)
        # Polynomial chaos expansion
        self.poly_order = np.random.randint(4, 9, dim)
        self.poly_coeff = np.random.uniform(-0.5, 0.5, (dim, 4))
        # Enhanced gradient modulation
        self.gradient_factor = np.random.uniform(0.6, 1.8, dim)
        
    def f(self, x):
        # Ensure x is within bounds [-5, 5]
        x = np.clip(x, -5.0, 5.0)
        
        # Normalize to [0, 1] for logistic map computation
        normalized_x = (x + 5.0) / 10.0
        
        # Compute chaotic logistic map values with time-varying parameters
        logistic_values = np.zeros(self.dim)
        for i in range(self.dim):
            # Dynamic parameter based on current position and time
            dynamic_r = self.logistic_r[i] * (1.0 + 0.2 * np.sin(self.time_freq[i] * x[i] + self.time_offset[i]))
            
            # Logistic map iteration with chaos
            log_value = normalized_x[i]
            for _ in range(20):  # Iterate to reach chaotic regime
                log_value = dynamic_r * log_value * (1.0 - log_value)
            
            # Apply damping factor
            logistic_values[i] = log_value * self.damping_factors[i]
        
        # Add quantum interference pattern
        quantum_pattern = np.zeros(self.dim)
        for i in range(self.dim):
            quantum_pattern[i] = self.interference_amplitude[i] * np.sin(self.interference_phase[i] + logistic_values[i])
        
        # Basin attraction term with fractal scaling
        basin_attraction = np.zeros(self.dim)
        for i in range(self.dim):
            dist = (logistic_values[i] - self.basin_centers[i])**2
            basin_attraction[i] = np.exp(-dist / (2 * self.basin_radii[i]**2)) * (1.0 + 0.3 * np.sin(logistic_values[i] * self.fractal_exponent[i]))
        
        # Polynomial chaos expansion term
        poly_chaos = np.zeros(self.dim)
        for i in range(self.dim):
            poly_chaos[i] = np.sum([self.poly_coeff[i, j] * (logistic_values[i]**(j+1)) for j in range(4)])
        
        # Coupling and modulation terms
        coupling_term = np.zeros(self.dim)
        for i in range(self.dim):
            for j in range(self.dim):
                if i != j:
                    coupling_factor = np.exp(-((logistic_values[i] - logistic_values[j])**2) / (0.5 * self.coupling_strength[i]))
                    coupling_term[i] += coupling_factor * self.modulation_depth[i]
        
        # Gradient modulation for conditioning
        grad_mod = np.zeros(self.dim)
        for i in range(self.dim):
            grad_mod[i] = self.gradient_factor[i] * np.abs(x[i])
        
        # Combine all terms with global scaling
        fitness = 0.0
        for i in range(self.dim):
            term = (logistic_values[i]**2 + 0.3 * logistic_values[i]**4 + 
                   basin_attraction[i] + coupling_term[i] + poly_chaos[i] + 
                   quantum_pattern[i] + grad_mod[i])
            fitness += term
        
        # Add noise and return
        noise = np.sum([np.random.uniform(-self.noise_level[i], self.noise_level[i]) for i in range(self.dim)])
        return fitness / self.dim + noise