import numpy as np

class ChaoticGradientBenchmark:
    def __init__(self, dim):
        self.dim = dim
        self.global_min = np.zeros(dim)
        # Precompute chaotic parameters for each dimension with modified coefficients
        self.chaos_params = 3.5 + 0.7 * np.sin(np.arange(dim) * 0.6)
        
    def f(self, x):
        if len(x) != self.dim:
            if len(x) < self.dim:
                x = np.pad(x, (0, self.dim - len(x)), mode='constant', constant_values=0.0)
            else:
                x = x[:self.dim]
        
        # Clip to bounds
        x = np.clip(x, -5.0, 5.0)
        
        # Quadratic basin term with modified conditioning
        basin_term = 0.15 * np.sum(x**2)
        
        # Chaotic gradient-based multimodal term with altered harmonic potentials
        multimodal_term = 0.0
        
        for i in range(self.dim):
            # Modified harmonic potential with altered frequency and amplitude
            freq = self.chaos_params[i] + 0.4 * np.sin(x[i] * 0.6 + i * 0.25)
            amp = 1.2 + 0.3 * np.cos(x[i] * 0.25 + i * 0.15)
            
            # Time-varying phase shift with different frequency
            phase = 0.4 * np.sin(i * 0.35 + np.sum(x) * 0.12)
            
            # Create harmonic potential with altered frequency and amplitude
            potential = amp * np.sin(freq * x[i] + phase)**2
            
            # Altered coupling between dimensions using modified interaction terms
            coupling = 0.0
            for j in range(self.dim):
                if i != j:
                    # Modified coupling strength based on dimension indices and variable values
                    coupling_strength = 0.4 + 0.15 * np.sin(i * 0.35 + j * 0.25 + x[i] * 0.12 + x[j] * 0.18)
                    coupling += coupling_strength * np.cos(x[i] - x[j])**2.5
            
            multimodal_term += potential + coupling
        
        # Modified conditioning term with altered scaling
        condition_term = 0.0
        for i in range(self.dim):
            # Altered scaling factor influenced by chaotic parameters and current position
            scale_factor = 1.0 + 0.7 * np.sin(i * 0.3 + x[i] * 0.35 + self.chaos_params[i] * 0.12)
            condition_term += scale_factor * (i + 1) * x[i]**4
        
        # Enhanced saddle point term with modified chaotic modulation
        saddle_term = 0.0
        for i in range(0, self.dim, 2):
            if i + 1 < self.dim:
                # Create enhanced chaotic saddle points with altered positions
                saddle_x = 1.8 * np.sin(i * 0.35 + x[i] * 0.25)
                saddle_y = 1.8 * np.cos(i * 0.45 + x[i+1] * 0.25)
                
                # Modified modulation of saddle strength
                strength = 0.9 + 0.25 * np.sin(x[i] * 0.55 + x[i+1] * 0.45 + i * 0.15)
                
                dist = np.sqrt((x[i] - saddle_x)**2 + (x[i+1] - saddle_y)**2)
                saddle_term += strength * np.exp(-dist**2 / 0.6)
        
        return basin_term + condition_term + multimodal_term - saddle_term