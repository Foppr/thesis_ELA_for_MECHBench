import numpy as np

class ChaoticGradientBenchmark:
    def __init__(self, dim):
        self.dim = dim
        self.global_min = np.zeros(dim)
        # Precompute hyperchaotic parameters with increased complexity and randomness
        self.hyperchaos_params = 8.0 + 3.0 * np.sin(np.arange(dim) * 1.1 + np.random.rand() * 2.0)
        self.fractal_dim = 1.7 + 0.6 * np.cos(np.arange(dim) * 0.9 + np.random.rand() * 1.5)
        # Add new chaotic modulation parameters with higher variance
        self.chaos_mod = 1.0 + 0.5 * np.random.rand(dim)
        # Introduce enhanced fractal dimensionality and coupling strength with increased variation
        self.fractal_coupling_strength = 4.0 + 3.0 * np.sin(np.arange(dim) * 0.7 + np.random.rand() * 1.2)
        self.saddle_strength_factor = 4.0 + 2.5 * np.cos(np.arange(dim) * 0.4 + np.random.rand() * 1.8)
        
    def f(self, x):
        if len(x) != self.dim:
            if len(x) < self.dim:
                x = np.pad(x, (0, self.dim - len(x)), mode='constant', constant_values=0.0)
            else:
                x = x[:self.dim]
        
        # Clip to bounds
        x = np.clip(x, -5.0, 5.0)
        
        # Enhanced hyperbolic basin term with fractal conditioning and chaotic modulation
        basin_term = 0.15 * np.sum(np.abs(x)**(2.0 + 0.4 * np.sin(self.fractal_dim)))
        
        # Hyperchaotic multimodal term with enhanced fractal potentials and cross-dimensional coupling
        multimodal_term = 0.0
        
        for i in range(self.dim):
            # Fractal harmonic potential with hyperchaotic modulation, chaos modulation and enhanced nonlinearity
            freq = self.hyperchaos_params[i] + 1.0 * np.sin(x[i] * 0.6 + i * 0.5)
            amp = 2.5 + 1.5 * np.cos(x[i] * 0.4 + i * 0.3)
            
            # Fractal phase shift with chaos modulation and enhanced temporal variation
            phase = 1.0 * np.sin(i * 0.7 + np.sum(x) * 0.25 + x[i] * 0.2 + self.chaos_mod[i] + np.sin(np.sum(x) * 0.3))
            
            # Create enhanced fractal potential with hyperchaotic frequency and amplitude
            potential = amp * np.sin(freq * x[i] + phase)**5
            
            # Add enhanced cross-dimensional coupling with fractal scaling and increased coupling strength
            coupling = 0.0
            for j in range(self.dim):
                if i != j:
                    # Enhanced fractal coupling strength based on dimension indices, variable values and chaotic modulation
                    coupling_strength = self.fractal_coupling_strength[i] * (2.0 + 1.5 * np.sin(i * 0.4 + j * 0.3 + x[i] * 0.2 + x[j] * 0.25 + self.chaos_mod[i] * 0.5))
                    # Enhanced fractal coupling function with higher order polynomial
                    coupling += coupling_strength * np.cos(x[i] - x[j])**5
            
            multimodal_term += potential + coupling
        
        # Enhanced hyper-fractal conditioning term with time-varying scaling and increased ruggedness
        condition_term = 0.0
        for i in range(self.dim):
            # Enhanced fractal scaling factor influenced by hyperchaotic parameters, current position and chaotic modulation
            scale_factor = 2.0 + 1.5 * np.sin(i * 0.5 + x[i] * 0.6 + self.hyperchaos_params[i] * 0.3 + self.chaos_mod[i])
            # Enhanced fractal power term with increased exponent for more ruggedness
            condition_term += scale_factor * (i + 1)**(2.5 + 0.4 * np.cos(x[i])) * x[i]**9
        
        # Enhanced hyper-saddle point term with fractal modulation and increased complexity
        saddle_term = 0.0
        for i in range(0, self.dim, 5):
            if i + 4 < self.dim:
                # Create enhanced hyper-saddle points with fractal positions and chaotic influence
                saddle_x = 3.0 * np.sin(i * 0.6 + x[i] * 0.4 + self.chaos_mod[i])
                saddle_y = 3.0 * np.cos(i * 0.7 + x[i+1] * 0.4 + self.chaos_mod[i+1])
                saddle_z = 3.0 * np.sin((i+1) * 0.5 + x[i+2] * 0.4 + self.chaos_mod[i+2])
                saddle_w = 3.0 * np.cos((i+2) * 0.6 + x[i+3] * 0.4 + self.chaos_mod[i+3])
                saddle_v = 3.0 * np.sin((i+3) * 0.5 + x[i+4] * 0.4 + self.chaos_mod[i+4])
                
                # Enhanced fractal modulation of saddle strength with chaotic variation
                strength = self.saddle_strength_factor[i] * (3.0 + 2.0 * np.sin(x[i] * 0.8 + x[i+1] * 0.7 + x[i+2] * 0.6 + x[i+3] * 0.5 + x[i+4] * 0.4 + i * 0.3 + self.chaos_mod[i]))
                
                dist = np.sqrt((x[i] - saddle_x)**2 + (x[i+1] - saddle_y)**2 + (x[i+2] - saddle_z)**2 + (x[i+3] - saddle_w)**2 + (x[i+4] - saddle_v)**2)
                # Enhanced fractal distance function with higher order scaling
                saddle_term += strength * np.exp(-dist**(2.5) / 0.3)
        
        # Add enhanced fractal noise term for extreme ruggedness and chaotic variation
        noise_term = 0.0
        for i in range(self.dim):
            noise = 0.4 * np.sin(x[i] * 8.0 + i * 3.0 + self.chaos_mod[i]) * np.cos(x[i] * 5.0 + self.chaos_mod[i+1 if i+1 < self.dim else 0])
            noise_term += noise
        
        # Add a new chaotic basin term with higher dimensionality coupling and increased nonlinearity
        chaos_basin = 0.08 * np.sum(np.sin(x)**4 * np.cos(x)**3)
        
        # Introduce improved conditioning and reduced bias in the final function with enhanced weighting
        return 1.0 * basin_term + 2.0 * condition_term + 1.5 * multimodal_term - 1.2 * saddle_term + 0.9 * noise_term + 0.5 * chaos_basin