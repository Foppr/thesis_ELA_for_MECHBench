import numpy as np

class ChaoticGradientBenchmark:
    def __init__(self, dim):
        self.dim = dim
        self.global_min = np.zeros(dim)
        # Enhanced hyperchaotic parameters with increased complexity
        self.hyperchaos_params = 6.5 + 2.5 * np.sin(np.arange(dim) * 0.95)
        self.fractal_dim = 1.4 + 0.5 * np.cos(np.arange(dim) * 0.75)
        # Increased variation in chaos modulation
        self.chaos_mod = 0.7 + 0.4 * np.random.rand(dim)
        # Enhanced fractal coupling with greater variation
        self.fractal_coupling_strength = 3.5 + 1.8 * np.sin(np.arange(dim) * 0.55)
        self.saddle_strength_factor = 2.8 + 2.0 * np.cos(np.arange(dim) * 0.35)
        
    def f(self, x):
        if len(x) != self.dim:
            if len(x) < self.dim:
                x = np.pad(x, (0, self.dim - len(x)), mode='constant', constant_values=0.0)
            else:
                x = x[:self.dim]
        
        # Clip to bounds
        x = np.clip(x, -5.0, 5.0)
        
        # Enhanced basin term with higher fractal conditioning
        basin_term = 0.12 * np.sum(np.abs(x)**(2.2 + 0.35 * np.sin(self.fractal_dim)))
        
        # Multimodal term with enhanced hyperchaotic potential functions
        multimodal_term = 0.0
        
        for i in range(self.dim):
            # Fractal harmonic potential with increased frequency modulation
            freq = self.hyperchaos_params[i] + 0.8 * np.sin(x[i] * 0.55 + i * 0.45)
            amp = 2.2 + 1.3 * np.cos(x[i] * 0.35 + i * 0.25)
            
            # Fractal phase shift with enhanced chaos modulation
            phase = 0.9 * np.sin(i * 0.65 + np.sum(x) * 0.25 + x[i] * 0.18 + self.chaos_mod[i])
            
            # Enhanced fractal potential function with higher order harmonics
            potential = amp * np.sin(freq * x[i] + phase)**5
            
            # Enhanced cross-dimensional coupling with increased strength and complexity
            coupling = 0.0
            for j in range(self.dim):
                if i != j:
                    coupling_strength = self.fractal_coupling_strength[i] * (1.6 + 1.2 * np.sin(i * 0.35 + j * 0.3 + x[i] * 0.18 + x[j] * 0.25))
                    coupling += coupling_strength * np.cos(x[i] - x[j])**5
            
            multimodal_term += potential + coupling
        
        # Enhanced hyper-fractal conditioning with additional scaling factors
        condition_term = 0.0
        for i in range(self.dim):
            scale_factor = 1.6 + 1.1 * np.sin(i * 0.45 + x[i] * 0.55 + self.hyperchaos_params[i] * 0.25)
            condition_term += scale_factor * (i + 1)**(2.2 + 0.35 * np.cos(x[i])) * x[i]**9
        
        # Enhanced hyper-saddle point term with more complex fractal positioning
        saddle_term = 0.0
        for i in range(0, self.dim, 4):
            if i + 3 < self.dim:
                saddle_x = 2.7 * np.sin(i * 0.55 + x[i] * 0.35)
                saddle_y = 2.7 * np.cos(i * 0.65 + x[i+1] * 0.35)
                saddle_z = 2.7 * np.sin((i+1) * 0.45 + x[i+2] * 0.35)
                saddle_w = 2.7 * np.cos((i+2) * 0.55 + x[i+3] * 0.35)
                
                strength = self.saddle_strength_factor[i] * (2.4 + 1.7 * np.sin(x[i] * 0.75 + x[i+1] * 0.65 + x[i+2] * 0.55 + x[i+3] * 0.45 + i * 0.25))
                
                dist = np.sqrt((x[i] - saddle_x)**2 + (x[i+1] - saddle_y)**2 + (x[i+2] - saddle_z)**2 + (x[i+3] - saddle_w)**2)
                saddle_term += strength * np.exp(-dist**(2.2) / 0.28)
        
        # Enhanced fractal noise term with increased ruggedness
        noise_term = 0.0
        for i in range(self.dim):
            noise = 0.35 * np.sin(x[i] * 6.5 + i * 2.7) * np.cos(x[i] * 4.5 + self.chaos_mod[i])
            noise_term += noise
        
        # Enhanced chaotic basin term with improved coupling
        chaos_basin = 0.06 * np.sum(np.sin(x)**4 * np.cos(x)**3)
        
        # Improved conditioning and bias reduction in final function
        return 0.85 * basin_term + 1.6 * condition_term + 1.2 * multimodal_term - 0.95 * saddle_term + 0.75 * noise_term + 0.45 * chaos_basin