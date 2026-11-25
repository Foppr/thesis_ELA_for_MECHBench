import numpy as np

class DynamicSaddleBenchmark:
    def __init__(self, dim):
        self.dim = dim
        # Initialize parameters for fractal basin structures
        self.basin_fractals = [np.random.uniform(0.1, 0.5) for _ in range(dim)]
        self.saddle_hyperbolic = [np.random.uniform(2.0, 5.0) for _ in range(dim)]
        self.time_phase = np.random.rand() * 2 * np.pi
        
    def f(self, x):
        # Ensure x is within bounds [-5, 5]
        x = np.clip(x, -5.0, 5.0)
        
        # Fractal basin component with chaotic scaling
        basins = 0
        for i in range(self.dim):
            fractal = self.basin_fractals[i]
            # Fractal basin: modified L1 norm with fractional exponents
            basins += (np.abs(x[i]) ** (1.0 + fractal)) / (1.0 + fractal)
            
        # Hyperbolic saddle points with time-varying strength
        saddles = 0
        for i in range(self.dim):
            hyperbolic = self.saddle_hyperbolic[i]
            # Time-varying hyperbolic saddle term
            time_factor = np.tanh(np.sin(self.time_phase + x[i]))
            saddle_term = hyperbolic * (x[i]**3 - x[i]) * time_factor
            saddles += saddle_term
            
        # Chaotic gradient field with multi-scale modulation
        gradients = 0
        for i in range(self.dim):
            # Multi-scale chaotic gradient scaling
            scale1 = np.sin(x[i] * np.pi)
            scale2 = np.cos(x[i] * np.pi / 3.0)
            scale3 = np.sin(x[i] * np.pi / 7.0)
            grad_scale = 1.0 + 0.3 * (scale1 + scale2 + scale3)
            gradients += grad_scale * np.tan(x[i] / 2.0)
            
        # Cross-dimension coupling with fractal weights
        coupling = 0
        for i in range(self.dim):
            for j in range(i+1, self.dim):
                # Fractal coupling weight based on coordinate relationships
                dist = np.abs(x[i] - x[j])
                fractal_weight = 0.5 + 0.5 * np.sin(self.time_phase + dist * (i + j + 1))
                coupling += fractal_weight * np.exp(-dist**2) * (i + j + 1)
                
        # Add chaotic noise component with time-dependent amplitude
        noise_amp = 0.2 * (1.0 + 0.3 * np.cos(self.time_phase * 3))
        noise = noise_amp * np.random.uniform(-1, 1, size=self.dim).sum()
        
        # Combine all components
        result = 1.5 * basins + 1.2 * saddles + 0.9 * gradients + 0.7 * coupling + 0.2 * noise
        
        # Add chaotic dimensionality scaling
        dim_factor = np.sin(self.time_phase + self.dim) * 0.5 + 0.5
        result *= (1.0 + 0.4 * dim_factor)
        
        return result