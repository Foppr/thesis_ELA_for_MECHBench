import numpy as np

class ChaoticGradientBenchmark:
    def __init__(self, dim):
        self.dim = dim
        self.global_min = np.zeros(dim)
        # Enhanced hyperchaotic parameters with exponential scaling
        self.hyperchaos_params = 8.0 * np.exp(np.arange(dim) * 0.15)
        self.fractal_dim = 2.0 + 0.6 * np.sin(np.arange(dim) * 0.8)
        # Introduce dynamic chaos modulation with exponential variation
        self.chaos_mod = 1.2 * np.exp(np.random.rand(dim) * 2.0)
        # Increased fractal coupling strength with exponential growth
        self.fractal_coupling_strength = 5.0 * np.exp(np.arange(dim) * 0.2)
        # Enhanced saddle point strength with logarithmic scaling
        self.saddle_strength_factor = 4.0 + 2.5 * np.log(np.arange(1, dim+1) + 1)
        
    def f(self, x):
        if len(x) != self.dim:
            if len(x) < self.dim:
                x = np.pad(x, (0, self.dim - len(x)), mode='constant', constant_values=0.0)
            else:
                x = x[:self.dim]
        
        # Clip to bounds
        x = np.clip(x, -5.0, 5.0)
        
        # Exponentially increased basin term with fractal conditioning
        basin_term = 0.2 * np.sum(np.abs(x)**(3.0 + 0.5 * np.sin(self.fractal_dim)))
        
        # Hyperchaotic multimodal term with exponential coupling
        multimodal_term = 0.0
        
        for i in range(self.dim):
            # Exponentially varying frequency and amplitude
            freq = self.hyperchaos_params[i] * (1.5 + 0.8 * np.sin(x[i] * 0.6 + i * 0.3))
            amp = 3.0 + 2.0 * np.cos(x[i] * 0.4 + i * 0.1)
            
            # Fractal phase shift with exponential chaos modulation
            phase = 1.2 * np.sin(i * 0.7 + np.sum(x) * 0.3 + x[i] * 0.2 + self.chaos_mod[i])
            
            # Create enhanced fractal potential with exponential frequency and amplitude
            potential = amp * np.sin(freq * x[i] + phase)**5
            
            # Enhanced cross-dimensional coupling with exponential scaling
            coupling = 0.0
            for j in range(self.dim):
                if i != j:
                    # Exponential coupling strength based on dimension indices and variable values
                    coupling_strength = self.fractal_coupling_strength[i] * np.exp(0.5 * (i + j) * 0.1)
                    # Enhanced fractal coupling function with higher power
                    coupling += coupling_strength * np.cos(x[i] - x[j])**5
            
            multimodal_term += potential + coupling
        
        # Hyper-fractal conditioning term with exponential scaling
        condition_term = 0.0
        for i in range(self.dim):
            # Exponential fractal scaling factor influenced by hyperchaotic parameters
            scale_factor = 2.0 * np.exp(0.3 * i + x[i] * 0.6)
            # Increased exponent and exponential power term
            condition_term += scale_factor * (i + 1)**(3.0 + 0.4 * np.cos(x[i])) * x[i]**10
        
        # Enhanced hyper-saddle point term with exponential modulation
        saddle_term = 0.0
        for i in range(0, self.dim, 5):
            if i + 4 < self.dim:
                # Create enhanced hyper-saddle points with exponential positions
                saddle_x = 3.0 * np.sin(i * 0.6 + x[i] * 0.4)
                saddle_y = 3.0 * np.cos(i * 0.7 + x[i+1] * 0.4)
                saddle_z = 3.0 * np.sin((i+1) * 0.5 + x[i+2] * 0.4)
                saddle_w = 3.0 * np.cos((i+2) * 0.6 + x[i+3] * 0.4)
                saddle_v = 3.0 * np.sin((i+3) * 0.5 + x[i+4] * 0.4)
                
                # Exponential fractal modulation of saddle strength
                strength = self.saddle_strength_factor[i] * (3.0 + 2.0 * np.sin(x[i] * 0.8 + x[i+1] * 0.7 + x[i+2] * 0.6 + x[i+3] * 0.5 + x[i+4] * 0.4 + i * 0.3))
                
                dist = np.sqrt((x[i] - saddle_x)**2 + (x[i+1] - saddle_y)**2 + (x[i+2] - saddle_z)**2 + (x[i+3] - saddle_w)**2 + (x[i+4] - saddle_v)**2)
                # Exponential distance function
                saddle_term += strength * np.exp(-dist**(3.0) / 0.3)
        
        # Enhanced fractal noise term with exponential complexity
        noise_term = 0.0
        for i in range(self.dim):
            noise = 0.5 * np.sin(x[i] * 8.0 + i * 3.0) * np.cos(x[i] * 6.0 + self.chaos_mod[i])
            noise_term += noise
        
        # Enhanced chaotic basin term with exponential coupling
        chaos_basin = 0.1 * np.sum(np.sin(x)**4 * np.cos(x)**3)
        
        # Final function with increased complexity and ruggedness
        return 1.2 * basin_term + 2.0 * condition_term + 1.8 * multimodal_term - 1.5 * saddle_term + 1.0 * noise_term + 0.6 * chaos_basin