import numpy as np

class ChaoticGradientBenchmark:
    def __init__(self, dim):
        self.dim = dim
        self.global_min = np.zeros(dim)
        # Precompute chaotic parameters for each dimension
        self.chaos_params = 4.0 + 0.5 * np.sin(np.arange(dim) * 0.7)
        
    def f(self, x):
        if len(x) != self.dim:
            if len(x) < self.dim:
                x = np.pad(x, (0, self.dim - len(x)), mode='constant', constant_values=0.0)
            else:
                x = x[:self.dim]
        
        # Clip to bounds
        x = np.clip(x, -5.0, 5.0)
        
        # Quadratic basin term with time-varying conditioning
        basin_term = 0.1 * np.sum(x**2)
        
        # Chaotic gradient-based multimodal term with dynamic harmonic potentials
        multimodal_term = 0.0
        
        for i in range(self.dim):
            # Dynamic harmonic potential with chaotic modulation
            freq = self.chaos_params[i] + 0.3 * np.sin(x[i] * 0.5 + i * 0.2)
            amp = 1.0 + 0.4 * np.cos(x[i] * 0.3 + i * 0.1)
            
            # Time-varying phase shift
            phase = 0.5 * np.sin(i * 0.4 + np.sum(x) * 0.1)
            
            # Create harmonic potential with chaotic frequency and amplitude
            potential = amp * np.sin(freq * x[i] + phase)**2
            
            # Add coupling between dimensions using chaotic interaction terms
            coupling = 0.0
            for j in range(self.dim):
                if i != j:
                    # Chaotic coupling strength based on dimension indices and variable values
                    coupling_strength = 0.3 + 0.2 * np.sin(i * 0.3 + j * 0.2 + x[i] * 0.1 + x[j] * 0.15)
                    coupling += coupling_strength * np.cos(x[i] - x[j])**2
            
            multimodal_term += potential + coupling
        
        # Dynamic conditioning term with time-varying scaling
        condition_term = 0.0
        for i in range(self.dim):
            # Time-varying scaling factor influenced by chaotic parameters and current position
            scale_factor = 1.0 + 0.6 * np.sin(i * 0.25 + x[i] * 0.3 + self.chaos_params[i] * 0.1)
            condition_term += scale_factor * (i + 1) * x[i]**4
        
        # Add dynamic saddle point term with chaotic modulation
        saddle_term = 0.0
        for i in range(0, self.dim, 2):
            if i + 1 < self.dim:
                # Create chaotic saddle points with time-varying positions
                saddle_x = 1.5 * np.sin(i * 0.3 + x[i] * 0.2)
                saddle_y = 1.5 * np.cos(i * 0.4 + x[i+1] * 0.2)
                
                # Chaotic modulation of saddle strength
                strength = 0.8 + 0.3 * np.sin(x[i] * 0.5 + x[i+1] * 0.4 + i * 0.1)
                
                dist = np.sqrt((x[i] - saddle_x)**2 + (x[i+1] - saddle_y)**2)
                saddle_term += strength * np.exp(-dist**2 / 0.5)
        
        # Enhanced multimodal structure with additional chaotic perturbations
        enhanced_multimodal = 0.0
        for i in range(self.dim):
            # Additional chaotic perturbation to increase landscape complexity
            perturbation = 0.5 * np.sin(x[i] * 2.0 + i * 0.3 + np.sum(x) * 0.2)
            enhanced_multimodal += perturbation * x[i]**2
        
        return basin_term + condition_term + multimodal_term - saddle_term + enhanced_multimodal