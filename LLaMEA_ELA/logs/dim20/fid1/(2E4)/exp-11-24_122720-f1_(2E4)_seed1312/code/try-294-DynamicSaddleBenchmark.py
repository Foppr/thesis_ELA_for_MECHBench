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
        
        # Superellipse basin component
        basins = 0
        for i in range(self.dim):
            param = self.basin_params[i]
            # Superellipse function: |x|^p + |y|^p = 1
            # Here we use a softened version for optimization
            basins += (np.abs(x[i]) ** (2.0 / param)) / param
            
        # Dynamic saddle points with time-varying strength
        saddles = 0
        for i in range(self.dim):
            strength = self.saddle_strength[i]
            # Time-varying saddle term
            time_factor = np.sin(self.time_phase + x[i])
            saddle_term = strength * (x[i]**2 - 1) * time_factor
            saddles += saddle_term
            
        # Gradient field modulation with non-linear scaling
        gradients = 0
        for i in range(self.dim):
            # Non-linear gradient scaling based on coordinate value
            grad_scale = 1.0 + 0.5 * np.tanh(x[i])
            gradients += grad_scale * np.sin(x[i] * np.pi / 2.0)
            
        # Cross-dimension coupling with dynamic weights
        coupling = 0
        for i in range(self.dim):
            for j in range(i+1, self.dim):
                # Dynamic coupling weight based on distance and time
                dist = np.abs(x[i] - x[j])
                time_weight = 0.5 + 0.5 * np.cos(self.time_phase + dist)
                coupling += time_weight * np.cos(x[i] * x[j]) * (i + j + 1)
                
        # Add noise component with amplitude modulation
        noise_amp = 0.1 * (1.0 + 0.2 * np.sin(self.time_phase))
        noise = noise_amp * np.random.uniform(-1, 1, size=self.dim).sum()
        
        # Combine all components
        result = 1.2 * basins + 0.8 * saddles + 0.6 * gradients + 0.4 * coupling + 0.1 * noise
        
        # Add dimensionality scaling
        dim_factor = np.log(self.dim + 2) / np.log(10)
        result *= (1.0 + 0.3 * dim_factor)
        
        return result