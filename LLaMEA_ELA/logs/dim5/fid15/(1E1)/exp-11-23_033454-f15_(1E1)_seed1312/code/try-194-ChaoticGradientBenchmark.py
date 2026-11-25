import numpy as np

class ChaoticGradientBenchmark:
    def __init__(self, dim):
        self.dim = dim
        self.global_min = np.zeros(dim)
        # Increased complexity in hyperchaotic parameters
        self.hyperchaos_params = 8.0 + 3.0 * np.sin(np.arange(dim) * 1.1)
        self.fractal_dim = 2.0 + 0.6 * np.cos(np.arange(dim) * 0.9)
        # Enhanced chaos modulation with larger variation
        self.chaos_mod = 1.0 + 0.5 * np.random.rand(dim)
        # Significantly increased fractal coupling strength and variation
        self.fractal_coupling_strength = 5.0 + 3.0 * np.sin(np.arange(dim) * 0.7)
        self.saddle_strength_factor = 4.0 + 2.5 * np.cos(np.arange(dim) * 0.4)
        
    def f(self, x):
        if len(x) != self.dim:
            if len(x) < self.dim:
                x = np.pad(x, (0, self.dim - len(x)), mode='constant', constant_values=0.0)
            else:
                x = x[:self.dim]
        
        # Clip to bounds
        x = np.clip(x, -5.0, 5.0)
        
        # Enhanced hyperbolic basin term with increased fractal conditioning
        basin_term = 0.15 * np.sum(np.abs(x)**(2.5 + 0.4 * np.sin(self.fractal_dim)))
        
        # Hyperchaotic multimodal term with even more complex fractal potentials
        multimodal_term = 0.0
        
        for i in range(self.dim):
            # More complex fractal harmonic potential with hyperchaotic modulation and chaos modulation
            freq = self.hyperchaos_params[i] + 1.0 * np.sin(x[i] * 0.7 + i * 0.5)
            amp = 2.5 + 1.5 * np.cos(x[i] * 0.4 + i * 0.3)
            
            # More complex fractal phase shift with chaos modulation
            phase = 1.2 * np.sin(i * 0.8 + np.sum(x) * 0.3 + x[i] * 0.2 + self.chaos_mod[i])
            
            # Create even more complex fractal potential with hyperchaotic frequency and amplitude
            potential = amp * np.sin(freq * x[i] + phase)**5
            
            # Enhanced cross-dimensional coupling with much higher strength
            coupling = 0.0
            for j in range(self.dim):
                if i != j:
                    # Even more enhanced fractal coupling strength based on dimension indices and variable values
                    coupling_strength = self.fractal_coupling_strength[i] * (2.0 + 1.5 * np.sin(i * 0.4 + j * 0.3 + x[i] * 0.2 + x[j] * 0.25))
                    # More complex fractal coupling function
                    coupling += coupling_strength * np.cos(x[i] - x[j])**5
            
            multimodal_term += potential + coupling
        
        # Extremely enhanced hyper-fractal conditioning term with time-varying scaling
        condition_term = 0.0
        for i in range(self.dim):
            # Even more complex fractal scaling factor influenced by hyperchaotic parameters and current position
            scale_factor = 2.0 + 1.5 * np.sin(i * 0.5 + x[i] * 0.6 + self.hyperchaos_params[i] * 0.3)
            # Even more rugged fractal power term (increased exponent from 8 to 10)
            condition_term += scale_factor * (i + 1)**(2.5 + 0.4 * np.cos(x[i])) * x[i]**10
        
        # Extremely enhanced hyper-saddle point term with complex fractal modulation
        saddle_term = 0.0
        for i in range(0, self.dim, 3):
            if i + 2 < self.dim:
                # Create extremely complex hyper-saddle points with fractal positions
                saddle_x = 3.0 * np.sin(i * 0.6 + x[i] * 0.4)
                saddle_y = 3.0 * np.cos(i * 0.7 + x[i+1] * 0.4)
                saddle_z = 3.0 * np.sin((i+1) * 0.5 + x[i+2] * 0.4)
                
                # Even more complex fractal modulation of saddle strength
                strength = self.saddle_strength_factor[i] * (3.0 + 2.0 * np.sin(x[i] * 0.8 + x[i+1] * 0.7 + x[i+2] * 0.6 + i * 0.3))
                
                dist = np.sqrt((x[i] - saddle_x)**2 + (x[i+1] - saddle_y)**2 + (x[i+2] - saddle_z)**2)
                # Extremely complex fractal distance function
                saddle_term += strength * np.exp(-dist**(3.0) / 0.3)
        
        # Extremely rugged fractal noise term for maximum ruggedness
        noise_term = 0.0
        for i in range(self.dim):
            noise = 0.5 * np.sin(x[i] * 8.0 + i * 3.0) * np.cos(x[i] * 6.0 + self.chaos_mod[i])
            noise_term += noise
        
        # Enhanced chaotic basin term with higher dimensionality coupling
        chaos_basin = 0.1 * np.sum(np.sin(x)**4 * np.cos(x)**3)
        
        # Introduce extremely improved conditioning and reduced bias in the final function
        return 1.2 * basin_term + 2.0 * condition_term + 1.8 * multimodal_term - 1.5 * saddle_term + 1.0 * noise_term + 0.6 * chaos_basin