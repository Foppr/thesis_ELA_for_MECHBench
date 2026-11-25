import numpy as np

class ChaoticGradientBenchmark:
    def __init__(self, dim):
        self.dim = dim
        self.global_min = np.zeros(dim)
        # Precompute hyperchaotic parameters for each dimension
        self.hyperchaos_params = 6.0 + 1.5 * np.sin(np.arange(dim) * 0.8)
        self.fractal_dim = 1.2 + 0.3 * np.cos(np.arange(dim) * 0.6)
        
    def f(self, x):
        if len(x) != self.dim:
            if len(x) < self.dim:
                x = np.pad(x, (0, self.dim - len(x)), mode='constant', constant_values=0.0)
            else:
                x = x[:self.dim]
        
        # Clip to bounds
        x = np.clip(x, -5.0, 5.0)
        
        # Hyperbolic basin term with fractal conditioning
        basin_term = 0.05 * np.sum(np.abs(x)**(1.8 + 0.2 * np.sin(self.fractal_dim)))
        
        # Hyperchaotic multimodal term with fractal potentials
        multimodal_term = 0.0
        
        for i in range(self.dim):
            # Fractal harmonic potential with hyperchaotic modulation
            freq = self.hyperchaos_params[i] + 0.5 * np.sin(x[i] * 0.4 + i * 0.3)
            amp = 1.5 + 0.8 * np.cos(x[i] * 0.2 + i * 0.15)
            
            # Fractal phase shift
            phase = 0.7 * np.sin(i * 0.5 + np.sum(x) * 0.15 + x[i] * 0.1)
            
            # Create fractal potential with hyperchaotic frequency and amplitude
            potential = amp * np.sin(freq * x[i] + phase)**3
            
            # Add cross-dimensional coupling with fractal scaling (slightly increased coupling strength)
            coupling = 0.0
            for j in range(self.dim):
                if i != j:
                    # Fractal coupling strength based on dimension indices and variable values (increased from 0.4 to 0.6)
                    coupling_strength = 0.6 + 0.4 * np.sin(i * 0.25 + j * 0.2 + x[i] * 0.12 + x[j] * 0.18)
                    # Fractal coupling function
                    coupling += coupling_strength * np.cos(x[i] - x[j])**3
            
            multimodal_term += potential + coupling
        
        # Hyper-fractal conditioning term with time-varying scaling
        condition_term = 0.0
        for i in range(self.dim):
            # Fractal scaling factor influenced by hyperchaotic parameters and current position
            scale_factor = 1.2 + 0.8 * np.sin(i * 0.3 + x[i] * 0.4 + self.hyperchaos_params[i] * 0.15)
            # Fractal power term (increased exponent from 5 to 6 for more ruggedness)
            condition_term += scale_factor * (i + 1)**(1.5 + 0.2 * np.cos(x[i])) * x[i]**6
        
        # Hyper-saddle point term with fractal modulation
        saddle_term = 0.0
        for i in range(0, self.dim, 3):
            if i + 2 < self.dim:
                # Create hyper-saddle points with fractal positions
                saddle_x = 2.0 * np.sin(i * 0.4 + x[i] * 0.25)
                saddle_y = 2.0 * np.cos(i * 0.5 + x[i+1] * 0.25)
                saddle_z = 2.0 * np.sin((i+1) * 0.3 + x[i+2] * 0.25)
                
                # Fractal modulation of saddle strength (slightly increased from 1.0 to 1.2)
                strength = 1.2 + 0.6 * np.sin(x[i] * 0.6 + x[i+1] * 0.5 + x[i+2] * 0.4 + i * 0.15)
                
                dist = np.sqrt((x[i] - saddle_x)**2 + (x[i+1] - saddle_y)**2 + (x[i+2] - saddle_z)**2)
                # Fractal distance function
                saddle_term += strength * np.exp(-dist**(1.8) / 0.3)
        
        # Add fractal noise term for extreme ruggedness
        noise_term = 0.0
        for i in range(self.dim):
            noise = 0.2 * np.sin(x[i] * 5.0 + i * 2.0) * np.cos(x[i] * 3.0)
            noise_term += noise
        
        return basin_term + condition_term + multimodal_term - saddle_term + noise_term