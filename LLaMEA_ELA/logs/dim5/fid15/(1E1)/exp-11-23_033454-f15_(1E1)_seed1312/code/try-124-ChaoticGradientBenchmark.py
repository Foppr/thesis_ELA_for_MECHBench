import numpy as np

class ChaoticGradientBenchmark:
    def __init__(self, dim):
        self.dim = dim
        self.global_min = np.zeros(dim)
        # Precompute hyperchaotic parameters for each dimension with increased complexity
        self.hyperchaos_params = 7.0 + 2.0 * np.sin(np.arange(dim) * 0.9)
        self.fractal_dim = 1.5 + 0.4 * np.cos(np.arange(dim) * 0.7)
        # Add new chaotic modulation parameters
        self.chaos_mod = 0.8 + 0.3 * np.random.rand(dim)
        
    def f(self, x):
        if len(x) != self.dim:
            if len(x) < self.dim:
                x = np.pad(x, (0, self.dim - len(x)), mode='constant', constant_values=0.0)
            else:
                x = x[:self.dim]
        
        # Clip to bounds
        x = np.clip(x, -5.0, 5.0)
        
        # Enhanced hyperbolic basin term with fractal conditioning
        basin_term = 0.1 * np.sum(np.abs(x)**(2.0 + 0.3 * np.sin(self.fractal_dim)))
        
        # Hyperchaotic multimodal term with enhanced fractal potentials
        multimodal_term = 0.0
        
        for i in range(self.dim):
            # Fractal harmonic potential with hyperchaotic modulation and chaos modulation
            freq = self.hyperchaos_params[i] + 0.7 * np.sin(x[i] * 0.5 + i * 0.4)
            amp = 2.0 + 1.2 * np.cos(x[i] * 0.3 + i * 0.2)
            
            # Fractal phase shift with chaos modulation
            phase = 0.8 * np.sin(i * 0.6 + np.sum(x) * 0.2 + x[i] * 0.15 + self.chaos_mod[i])
            
            # Create enhanced fractal potential with hyperchaotic frequency and amplitude
            potential = amp * np.sin(freq * x[i] + phase)**4
            
            # Add enhanced cross-dimensional coupling with fractal scaling (significantly increased coupling strength)
            coupling = 0.0
            for j in range(self.dim):
                if i != j:
                    # Enhanced fractal coupling strength based on dimension indices and variable values (increased from 0.6 to 1.2)
                    coupling_strength = 1.2 + 0.8 * np.sin(i * 0.3 + j * 0.25 + x[i] * 0.15 + x[j] * 0.22)
                    # Enhanced fractal coupling function
                    coupling += coupling_strength * np.cos(x[i] - x[j])**4
            
            multimodal_term += potential + coupling
        
        # Enhanced hyper-fractal conditioning term with time-varying scaling
        condition_term = 0.0
        for i in range(self.dim):
            # Enhanced fractal scaling factor influenced by hyperchaotic parameters and current position
            scale_factor = 1.5 + 1.0 * np.sin(i * 0.4 + x[i] * 0.5 + self.hyperchaos_params[i] * 0.2)
            # Enhanced fractal power term (increased exponent from 6 to 8 for more ruggedness)
            condition_term += scale_factor * (i + 1)**(2.0 + 0.3 * np.cos(x[i])) * x[i]**8
        
        # Enhanced hyper-saddle point term with fractal modulation
        saddle_term = 0.0
        for i in range(0, self.dim, 4):
            if i + 3 < self.dim:
                # Create enhanced hyper-saddle points with fractal positions
                saddle_x = 2.5 * np.sin(i * 0.5 + x[i] * 0.3)
                saddle_y = 2.5 * np.cos(i * 0.6 + x[i+1] * 0.3)
                saddle_z = 2.5 * np.sin((i+1) * 0.4 + x[i+2] * 0.3)
                saddle_w = 2.5 * np.cos((i+2) * 0.5 + x[i+3] * 0.3)
                
                # Enhanced fractal modulation of saddle strength (increased from 1.2 to 1.8)
                strength = 1.8 + 1.0 * np.sin(x[i] * 0.7 + x[i+1] * 0.6 + x[i+2] * 0.5 + x[i+3] * 0.4 + i * 0.2)
                
                dist = np.sqrt((x[i] - saddle_x)**2 + (x[i+1] - saddle_y)**2 + (x[i+2] - saddle_z)**2 + (x[i+3] - saddle_w)**2)
                # Enhanced fractal distance function
                saddle_term += strength * np.exp(-dist**(2.0) / 0.25)
        
        # Add enhanced fractal noise term for extreme ruggedness
        noise_term = 0.0
        for i in range(self.dim):
            noise = 0.3 * np.sin(x[i] * 6.0 + i * 2.5) * np.cos(x[i] * 4.0 + self.chaos_mod[i])
            noise_term += noise
        
        # Add a new chaotic basin term with higher dimensionality coupling
        chaos_basin = 0.05 * np.sum(np.sin(x)**3 * np.cos(x)**2)
        
        # Introduce improved conditioning and reduced bias in the final function
        return 0.8 * basin_term + 1.2 * condition_term + 0.9 * multimodal_term - 0.7 * saddle_term + 0.6 * noise_term + 0.4 * chaos_basin