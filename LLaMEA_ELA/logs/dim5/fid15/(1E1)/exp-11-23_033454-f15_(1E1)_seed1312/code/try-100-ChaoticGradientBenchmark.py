import numpy as np

class ChaoticGradientBenchmark:
    def __init__(self, dim):
        self.dim = dim
        self.global_min = np.zeros(dim)
        # Precompute hyper-chaotic parameters for each dimension
        self.chaos_params = 3.8 + 0.7 * np.sin(np.arange(dim) * 0.8 + np.pi/4)
        self.fractal_dims = 1.2 + 0.3 * np.cos(np.arange(dim) * 0.6)
        
    def f(self, x):
        if len(x) != self.dim:
            if len(x) < self.dim:
                x = np.pad(x, (0, self.dim - len(x)), mode='constant', constant_values=0.0)
            else:
                x = x[:self.dim]
        
        # Clip to bounds
        x = np.clip(x, -5.0, 5.0)
        
        # Hyper-chaotic basin term with fractal conditioning
        basin_term = 0.05 * np.sum(x**2)
        
        # Fractal-like multimodal term with self-similar patterns
        multimodal_term = 0.0
        
        for i in range(self.dim):
            # Fractal harmonic potential with multi-scale chaos
            freq = self.chaos_params[i] + 0.4 * np.sin(x[i] * 0.6 + i * 0.3)
            amp = 1.2 + 0.5 * np.cos(x[i] * 0.4 + i * 0.2)
            
            # Multi-fractal phase modulation
            phase = 0.7 * np.sin(i * 0.5 + np.sum(x) * 0.15 + np.sin(x[i] * 0.3))
            
            # Create fractal harmonic potential with multi-scale frequency
            potential = amp * np.sin(freq * x[i] + phase)**(2 + self.fractal_dims[i])
            
            # Add hyper-coupling between dimensions using fractal interaction terms
            coupling = 0.0
            for j in range(self.dim):
                if i != j:
                    # Hyper-coupling strength based on fractal dimensions and variable values
                    coupling_strength = 0.4 + 0.3 * np.sin(i * 0.4 + j * 0.3 + x[i] * 0.15 + x[j] * 0.2)
                    coupling += coupling_strength * np.cos(x[i] - x[j])**3
            
            multimodal_term += potential + coupling
        
        # Hyper-dynamic conditioning term with fractal scaling
        condition_term = 0.0
        for i in range(self.dim):
            # Fractal scaling factor influenced by chaotic parameters and current position
            scale_factor = 1.5 + 0.8 * np.sin(i * 0.3 + x[i] * 0.4 + self.chaos_params[i] * 0.15)
            condition_term += scale_factor * (i + 1)**self.fractal_dims[i] * x[i]**5
        
        # Hyper-saddle point term with fractal modulation
        saddle_term = 0.0
        for i in range(0, self.dim, 3):
            if i + 2 < self.dim:
                # Create hyper-saddle points with fractal positions
                saddle_x = 2.0 * np.sin(i * 0.4 + x[i] * 0.25)
                saddle_y = 2.0 * np.cos(i * 0.5 + x[i+1] * 0.25)
                saddle_z = 2.0 * np.sin(i * 0.3 + x[i+2] * 0.25)
                
                # Fractal modulation of saddle strength
                strength = 1.0 + 0.5 * np.sin(x[i] * 0.6 + x[i+1] * 0.5 + x[i+2] * 0.4 + i * 0.15)
                
                dist = np.sqrt((x[i] - saddle_x)**2 + (x[i+1] - saddle_y)**2 + (x[i+2] - saddle_z)**2)
                saddle_term += strength * np.exp(-dist**2 / 0.3) * (1.0 + 0.2 * np.sin(dist * 2))
        
        # Add fractal noise term for extreme landscape complexity
        noise_term = 0.0
        for i in range(self.dim):
            noise = 0.3 * np.sin(x[i] * 10.0 + i * 2.0) * np.cos(x[i] * 7.0 + i * 1.5)
            noise_term += noise
        
        return basin_term + condition_term + multimodal_term - saddle_term + noise_term