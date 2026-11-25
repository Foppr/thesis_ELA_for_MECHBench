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
            # Modified fractal basin with additional sinusoidal modulation
            basins += (np.abs(x[i]) ** (1.0 + fractal)) / (1.0 + fractal) * (1.0 + 0.2 * np.sin(self.time_phase + x[i]))
            
        # Hyperbolic saddle points with time-varying strength and modified cubic term
        saddles = 0
        for i in range(self.dim):
            hyperbolic = self.saddle_hyperbolic[i]
            # Enhanced hyperbolic saddle with quadratic modulation
            time_factor = np.tanh(np.sin(self.time_phase + x[i]))
            saddle_term = hyperbolic * (x[i]**4 - 2*x[i]**2) * time_factor
            saddles += saddle_term
            
        # Chaotic gradient field with multi-scale modulation and additional nonlinearity
        gradients = 0
        for i in range(self.dim):
            # Multi-scale chaotic gradient scaling with modified frequency
            scale1 = np.sin(x[i] * np.pi * 1.5)
            scale2 = np.cos(x[i] * np.pi / 2.0)
            scale3 = np.sin(x[i] * np.pi / 5.0)
            grad_scale = 1.0 + 0.4 * (scale1 + scale2 + scale3)
            gradients += grad_scale * np.tan(x[i] / 1.5)
            
        # Cross-dimension coupling with fractal weights and additional interaction term
        coupling = 0
        for i in range(self.dim):
            for j in range(i+1, self.dim):
                # Fractal coupling weight with modified distance function
                dist = np.abs(x[i] - x[j])
                fractal_weight = 0.6 + 0.4 * np.sin(self.time_phase + dist * (i + j + 1) * 1.2)
                coupling += fractal_weight * np.exp(-dist**2 * 0.5) * (i + j + 1) * 0.8
                
        # Add chaotic noise component with time-dependent amplitude
        noise_amp = 0.3 * (1.0 + 0.4 * np.cos(self.time_phase * 2.5))
        noise = noise_amp * np.random.uniform(-1, 1, size=self.dim).sum()
        
        # Combine all components
        result = 1.7 * basins + 1.4 * saddles + 1.1 * gradients + 0.8 * coupling + 0.25 * noise
        
        # Add chaotic dimensionality scaling with modified factor
        dim_factor = np.sin(self.time_phase + self.dim * 1.3) * 0.6 + 0.4
        result *= (1.0 + 0.5 * dim_factor)
        
        return result