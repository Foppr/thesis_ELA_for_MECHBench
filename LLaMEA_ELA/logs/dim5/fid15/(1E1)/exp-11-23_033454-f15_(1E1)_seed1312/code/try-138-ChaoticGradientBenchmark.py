import numpy as np

class ChaoticGradientBenchmark:
    def __init__(self, dim):
        self.dim = dim
        self.global_min = np.zeros(dim)
        # Enhanced hyperchaotic parameters with increased complexity
        self.hyperchaos_params = 6.5 + 2.5 * np.sin(np.arange(dim) * 0.85)
        self.fractal_dim = 1.4 + 0.5 * np.cos(np.arange(dim) * 0.75)
        # Add new chaotic modulation parameters with higher variance
        self.chaos_mod = 0.9 + 0.4 * np.random.rand(dim)
        # Introduce enhanced fractal dimensionality and coupling strength
        self.fractal_coupling_strength = 2.2 + 1.8 * np.sin(np.arange(dim) * 0.55)
        self.saddle_strength_factor = 2.7 + 1.4 * np.cos(np.arange(dim) * 0.35)
        
    def f(self, x):
        if len(x) != self.dim:
            if len(x) < self.dim:
                x = np.pad(x, (0, self.dim - len(x)), mode='constant', constant_values=0.0)
            else:
                x = x[:self.dim]
        
        # Clip to bounds
        x = np.clip(x, -5.0, 5.0)
        
        # Enhanced hyperbolic basin term with fractal conditioning
        basin_term = 0.12 * np.sum(np.abs(x)**(2.1 + 0.35 * np.sin(self.fractal_dim)))
        
        # Hyperchaotic multimodal term with enhanced fractal potentials
        multimodal_term = 0.0
        
        for i in range(self.dim):
            # Fractal harmonic potential with hyperchaotic modulation and chaos modulation
            freq = self.hyperchaos_params[i] + 0.8 * np.sin(x[i] * 0.55 + i * 0.45)
            amp = 2.2 + 1.3 * np.cos(x[i] * 0.35 + i * 0.25)
            
            # Fractal phase shift with chaos modulation
            phase = 0.9 * np.sin(i * 0.65 + np.sum(x) * 0.25 + x[i] * 0.18 + self.chaos_mod[i])
            
            # Create enhanced fractal potential with hyperchaotic frequency and amplitude
            potential = amp * np.sin(freq * x[i] + phase)**4.5
            
            # Add enhanced cross-dimensional coupling with fractal scaling (significantly increased coupling strength)
            coupling = 0.0
            for j in range(self.dim):
                if i != j:
                    # Enhanced fractal coupling strength based on dimension indices and variable values
                    coupling_strength = self.fractal_coupling_strength[i] * (1.3 + 0.9 * np.sin(i * 0.35 + j * 0.28 + x[i] * 0.18 + x[j] * 0.25))
                    # Enhanced fractal coupling function
                    coupling += coupling_strength * np.cos(x[i] - x[j])**4.5
            
            multimodal_term += potential + coupling
        
        # Enhanced hyper-fractal conditioning term with time-varying scaling
        condition_term = 0.0
        for i in range(self.dim):
            # Enhanced fractal scaling factor influenced by hyperchaotic parameters and current position
            scale_factor = 1.6 + 1.1 * np.sin(i * 0.45 + x[i] * 0.55 + self.hyperchaos_params[i] * 0.25)
            # Enhanced fractal power term (increased exponent from 6 to 8 for more ruggedness)
            condition_term += scale_factor * (i + 1)**(2.1 + 0.35 * np.cos(x[i])) * x[i]**8.5
        
        # Enhanced hyper-saddle point term with fractal modulation
        saddle_term = 0.0
        for i in range(0, self.dim, 4):
            if i + 3 < self.dim:
                # Create enhanced hyper-saddle points with fractal positions
                saddle_x = 2.6 * np.sin(i * 0.55 + x[i] * 0.35)
                saddle_y = 2.6 * np.cos(i * 0.65 + x[i+1] * 0.35)
                saddle_z = 2.6 * np.sin((i+1) * 0.45 + x[i+2] * 0.35)
                saddle_w = 2.6 * np.cos((i+2) * 0.55 + x[i+3] * 0.35)
                
                # Enhanced fractal modulation of saddle strength
                strength = self.saddle_strength_factor[i] * (1.9 + 1.1 * np.sin(x[i] * 0.75 + x[i+1] * 0.65 + x[i+2] * 0.55 + x[i+3] * 0.45 + i * 0.25))
                
                dist = np.sqrt((x[i] - saddle_x)**2 + (x[i+1] - saddle_y)**2 + (x[i+2] - saddle_z)**2 + (x[i+3] - saddle_w)**2)
                # Enhanced fractal distance function
                saddle_term += strength * np.exp(-dist**(2.1) / 0.28)
        
        # Add enhanced fractal noise term for extreme ruggedness
        noise_term = 0.0
        for i in range(self.dim):
            noise = 0.35 * np.sin(x[i] * 6.5 + i * 2.7) * np.cos(x[i] * 4.5 + self.chaos_mod[i])
            noise_term += noise
        
        # Add a new chaotic basin term with higher dimensionality coupling
        chaos_basin = 0.06 * np.sum(np.sin(x)**3.5 * np.cos(x)**2.5)
        
        # Introduce improved conditioning and reduced bias in the final function
        return 0.85 * basin_term + 1.25 * condition_term + 0.95 * multimodal_term - 0.75 * saddle_term + 0.65 * noise_term + 0.45 * chaos_basin