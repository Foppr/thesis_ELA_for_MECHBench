import numpy as np

class DynamicSaddleBenchmark:
    def __init__(self, dim):
        self.dim = dim
        # Initialize parameters for chaotic basin structures
        self.basin_params = [np.random.uniform(0.1, 0.9) for _ in range(dim)]
        self.saddle_strength = [np.random.uniform(2.0, 5.0) for _ in range(dim)]
        self.time_phase = np.random.rand() * 2 * np.pi
        # Add chaotic modulation parameters
        self.chaos_params = [np.random.uniform(0.5, 2.0) for _ in range(dim)]
        
    def f(self, x):
        # Ensure x is within bounds [-5, 5]
        x = np.clip(x, -5.0, 5.0)
        
        # Chaotic basin component with fractal-like scaling
        basins = 0
        for i in range(self.dim):
            param = self.basin_params[i]
            # Fractal-like superellipse with chaotic modulation
            chaotic_factor = np.sin(self.chaos_params[i] * x[i]) * np.cos(self.chaos_params[i] * x[i])
            basins += (np.abs(x[i]) ** (2.0 / param)) / param + 0.3 * chaotic_factor
            
        # Hyperelastic saddle points with time-varying nonlinearity
        saddles = 0
        for i in range(self.dim):
            strength = self.saddle_strength[i]
            # Time-varying hyperelastic term with chaotic modulation
            time_factor = np.sin(self.time_phase + x[i]) * np.cos(self.time_phase + x[i])
            # Hyperelastic function: (x^2 - 1)^3
            saddle_term = strength * ((x[i]**2 - 1)**3) * time_factor
            saddles += saddle_term
            
        # Cross-dimensional resonance coupling with chaotic weights
        coupling = 0
        for i in range(self.dim):
            for j in range(i+1, self.dim):
                # Chaotic coupling weight based on coordinate values and time
                dist = np.abs(x[i] - x[j])
                chaos_weight = np.sin(self.chaos_params[i] * x[i]) * np.cos(self.chaos_params[j] * x[j])
                time_weight = 0.5 + 0.5 * np.cos(self.time_phase + dist)
                coupling += time_weight * chaos_weight * np.sin(x[i] * x[j]) * (i + j + 1)
                
        # Gradient field with chaotic modulation and hyperelastic scaling
        gradients = 0
        for i in range(self.dim):
            # Hyperelastic gradient scaling based on coordinate value
            grad_scale = 1.0 + 0.8 * np.tanh(x[i]**3)
            chaotic_grad = np.sin(self.chaos_params[i] * x[i])
            gradients += grad_scale * np.sin(x[i] * np.pi / 2.0) * chaotic_grad
            
        # Add noise component with chaotic amplitude modulation
        noise_amp = 0.15 * (1.0 + 0.3 * np.sin(self.time_phase)) * np.prod([np.abs(np.sin(self.chaos_params[i])) for i in range(self.dim)])
        noise = noise_amp * np.random.uniform(-1, 1, size=self.dim).sum()
        
        # Combine all components with chaotic weights
        result = 1.5 * basins + 1.2 * saddles + 0.8 * gradients + 0.6 * coupling + 0.2 * noise
        
        # Add dimensionality scaling with chaotic factor
        dim_factor = np.log(self.dim + 3) / np.log(12)
        chaos_dim_factor = np.prod([np.sin(self.chaos_params[i]) for i in range(min(3, self.dim))])
        result *= (1.0 + 0.5 * dim_factor * chaos_dim_factor)
        
        return result