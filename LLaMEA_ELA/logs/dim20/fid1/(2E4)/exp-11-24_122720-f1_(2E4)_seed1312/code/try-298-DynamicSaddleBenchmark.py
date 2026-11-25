import numpy as np

class DynamicSaddleBenchmark:
    def __init__(self, dim):
        self.dim = dim
        # Initialize parameters for superellipse basins
        self.basin_params = [np.random.uniform(0.5, 2.0) for _ in range(dim)]
        self.saddle_strength = [np.random.uniform(1.0, 3.0) for _ in range(dim)]
        self.time_phase = np.random.rand() * 2 * np.pi
        
    def f(self, x):
        # Ensure x is within bounds [-5, 5]
        x = np.clip(x, -5.0, 5.0)
        
        # Superellipse basin component with enhanced non-linearity
        basins = 0
        for i in range(self.dim):
            param = self.basin_params[i]
            # Enhanced superellipse with logarithmic scaling
            basins += (np.abs(x[i]) ** (2.0 / param)) / param * np.log(np.abs(x[i]) + 1.0)
            
        # Dynamic saddle points with enhanced time-varying complexity
        saddles = 0
        for i in range(self.dim):
            strength = self.saddle_strength[i]
            # Enhanced time-varying saddle term with harmonic modulation
            time_factor = np.sin(self.time_phase + x[i]) * np.cos(2 * self.time_phase + x[i])
            saddle_term = strength * (x[i]**2 - 1) * time_factor
            saddles += saddle_term
            
        # Gradient field modulation with enhanced non-linearity
        gradients = 0
        for i in range(self.dim):
            # Enhanced gradient scaling with exponential function
            grad_scale = np.exp(0.5 * x[i]) / (1.0 + np.exp(0.5 * x[i]))
            gradients += grad_scale * np.sin(x[i] * np.pi / 2.0)
            
        # Cross-dimension coupling with enhanced dynamic weights
        coupling = 0
        for i in range(self.dim):
            for j in range(i+1, self.dim):
                # Enhanced coupling weight based on distance and time with exponential decay
                dist = np.abs(x[i] - x[j])
                time_weight = 0.5 + 0.5 * np.cos(self.time_phase + dist) * np.exp(-dist/5.0)
                coupling += time_weight * np.cos(x[i] * x[j]) * (i + j + 1)
                
        # Enhanced noise component with adaptive amplitude
        noise_amp = 0.05 * (1.0 + 0.1 * np.sin(self.time_phase))
        noise = noise_amp * np.random.uniform(-1, 1, size=self.dim).sum()
        
        # Combine all components with adjusted weights for better balance
        result = 1.0 * basins + 0.9 * saddles + 0.7 * gradients + 0.5 * coupling + 0.1 * noise
        
        # Enhanced dimensionality scaling with polynomial factor
        dim_factor = (self.dim + 1) ** 0.7 / (1.0 + np.log(self.dim + 1))
        result *= (1.0 + 0.2 * dim_factor)
        
        return result