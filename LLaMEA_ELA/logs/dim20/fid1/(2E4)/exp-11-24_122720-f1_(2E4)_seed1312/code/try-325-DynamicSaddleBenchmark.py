import numpy as np

class DynamicSaddleBenchmark:
    def __init__(self, dim):
        self.dim = dim
        # Initialize chaotic parameters for each dimension with enhanced randomness
        self.chaos_params = [np.random.uniform(0.3, 1.2) for _ in range(dim)]
        self.ridge_strength = [np.random.uniform(1.0, 3.0) for _ in range(dim)]
        self.fractal_dim = 1.8 + np.random.rand() * 0.7
        # Add additional chaotic coupling terms
        self.coupling_strength = np.random.uniform(0.5, 2.5, (dim, dim))
        
    def f(self, x):
        # Ensure x is within bounds [-5, 5]
        x = np.clip(x, -5.0, 5.0)
        
        # Enhanced chaotic component with multiple sine harmonics and cubic terms
        chaotic = 0
        for i in range(self.dim):
            param = self.chaos_params[i]
            # Add higher-order polynomial and multi-frequency sine components
            chaotic += param * x[i] * (1 - x[i]**2) + 0.2 * np.sin(2.0 * x[i] * np.pi) + \
                       0.15 * np.sin(3.0 * x[i] * np.pi) + 0.08 * x[i]**3 + 0.03 * x[i]**4
            
        # Fractal basin component with self-similar scaling and logarithmic exponents
        fractal = 0
        for i in range(self.dim):
            # Use log-scale exponents for more extreme fractal behavior
            exponent = 1.0 + 1.5 * np.log(i + 2) / np.log(self.dim + 1)
            fractal += np.abs(x[i])**exponent
            
        # Enhanced ridge structure with piecewise and hyperbolic components
        ridges = 0
        for i in range(self.dim):
            strength = self.ridge_strength[i]
            # Add discontinuous and piecewise functions for increased non-smoothness
            ridge = strength * (np.exp(-x[i]**2) + 0.6 * np.sin(x[i]) + 0.4 * np.cos(2 * x[i]) + 
                               0.15 * np.tanh(x[i]) + 0.1 * np.sign(x[i]) * np.log(np.abs(x[i]) + 1))
            ridges += ridge
            
        # Cross-dimension interaction with multiple coupling modes and chaotic modulation
        interaction = 0
        for i in range(self.dim):
            for j in range(i+1, self.dim):
                # Add chaotic modulation to coupling strength and introduce higher-order terms
                coupling = self.coupling_strength[i][j] * (1 + 0.2 * np.sin(x[i] * x[j]))
                interaction += coupling * np.sin(4.0 * x[i] * x[j]) * np.cos(3.0 * (x[i] + x[j])) * \
                              np.exp(-0.1 * (x[i]**2 + x[j]**2)) * (1 + 0.25 * np.sin(i * j * np.pi / self.dim))
                
        # Hyperbolic saddle term with exponential decay and multiple asymptotic behaviors
        saddle = 0
        for i in range(self.dim):
            # Add exponential and multi-asymptotic saddle points
            saddle += 0.4 * np.abs(x[i]) * np.tanh(x[i]) + 0.15 * np.exp(-x[i]**2) * np.sinh(x[i])
            
        # Add a global scaling factor with chaotic modulation based on dimension
        global_factor = 1.5 + 0.5 * np.sin(self.dim * np.pi / 4)
        
        # Combine all components with adaptive weights and chaotic scaling
        result = global_factor * (2.5 * chaotic + 1.8 * fractal + 1.5 * ridges + 0.8 * interaction + 1.0 * saddle)
        
        # Add dimensionality-dependent modulation with fractal scaling
        dim_modulation = np.log(self.dim + 2) * 0.3
        result *= (1.0 + dim_modulation)
        
        return result