import numpy as np

class FractalMultimodalLandscape:
    def __init__(self, dim):
        self.dim = dim
        # Initialize fractal parameters
        self.fractal_dim = 1.5 + 0.5 * np.random.rand()
        self.peak_density = 2.0 + 1.0 * np.random.rand()
        self.correlation_strength = 0.3 + 0.4 * np.random.rand()
        self.time_phase = np.random.rand() * 2 * np.pi
        
    def f(self, x):
        # Ensure x is within bounds [-5, 5]
        x = np.clip(x, -5.0, 5.0)
        
        # Time-varying fractal scaling
        t = np.sin(self.time_phase) + 1.0
        scaled_x = x * (1.0 + 0.2 * np.sin(0.5 * self.time_phase))
        
        # Fractal-based multimodal component
        fractal_term = 0.0
        for i in range(self.dim):
            # Multi-scale fractal peaks with varying heights
            peak_height = 1.0 + 0.5 * np.sin(i * 0.7)
            peak_width = 0.8 + 0.3 * np.cos(i * 0.5)
            fractal_term += peak_height * np.exp(-0.5 * ((scaled_x[i] - 2.0 * np.sin(i * 0.3)) / peak_width)**2)
            
        # Adaptive correlation structure
        corr_term = 0.0
        for i in range(self.dim):
            for j in range(i+1, self.dim):
                corr_factor = self.correlation_strength * np.sin(0.3 * (i - j) + self.time_phase)
                corr_term += corr_factor * np.cos(scaled_x[i] * scaled_x[j])
                
        # Dynamic peak density modulation
        density_mod = 1.0 + 0.3 * np.sin(0.4 * self.time_phase + np.sum(x))
        
        # Basin connectivity term with varying smoothness
        basin_term = 0.0
        for i in range(self.dim):
            smoothness = 0.5 + 0.5 * np.cos(i * 0.6 + self.time_phase)
            basin_term += (x[i]**4 - 2.0 * x[i]**2) * smoothness
            
        # Time-varying global structure
        global_structure = np.sin(0.2 * np.sum(x) + self.time_phase) * np.cos(0.1 * np.sum(x**2))
        
        # Combine all components with dynamic weights
        result = (fractal_term * density_mod + 
                 corr_term * 0.5 + 
                 basin_term * 0.3 + 
                 global_structure * 0.2)
        
        return result