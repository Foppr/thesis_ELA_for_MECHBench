import numpy as np

class ChaoticSaddleBenchmark:
    def __init__(self, dim):
        self.dim = dim
        # Precompute chaotic parameters for each dimension with enhanced complexity
        self.chaos_params = [np.sin(i * 0.7 + 1.2) * 3.0 + 2.0 + np.random.uniform(-0.5, 0.5) for i in range(dim)]
        self.saddle_params = [np.cos(i * 0.5 + 0.8) * 0.5 + 1.0 + np.random.uniform(-0.3, 0.3) for i in range(dim)]
        # Add new exponential interaction parameters with enhanced variability
        self.exp_params = [np.exp(-i * 0.1 + 0.5) * (1.0 + 0.2 * np.sin(i * 0.8)) for i in range(dim)]
        # Add cross-dimensional coupling strength parameters
        self.coupling_strengths = [0.5 + 0.5 * np.cos(i * 0.6) for i in range(dim)]
        
    def f(self, x):
        # Ensure x is within bounds [-5, 5]
        x = np.clip(x, -5.0, 5.0)
        
        # Enhanced polynomial chaos expansion component with varying degrees and chaotic modulation
        chaos = 0.0
        for i in range(self.dim):
            degree = int(2 + 3 * np.sin(i * 0.3 + 1.0) + 0.5 * np.cos(i * 0.4))
            coeff = self.chaos_params[i]
            chaos += coeff * (x[i] ** degree)
        
        # Enhanced saddle-point structure with dynamic orientation and additional nonlinear terms
        saddle = 0.0
        for i in range(self.dim):
            orient = self.saddle_params[i]
            saddle += x[i] ** 2 * np.sin(orient * x[i]) + x[i] ** 3 * np.cos(orient * x[i]) + \
                      0.1 * x[i] ** 4 * np.sin(0.5 * orient * x[i])
        
        # Enhanced cross-dimensional coupling with chaotic modulation and dynamic strengths
        coupling = 0.0
        for i in range(self.dim):
            for j in range(i+1, self.dim):
                mod_i = 0.5 + 0.5 * np.sin(0.3 * (i + j) + 1.0 + 0.2 * np.cos(i * 0.5))
                mod_j = 0.5 + 0.5 * np.cos(0.3 * (i - j) + 1.0 + 0.2 * np.sin(j * 0.5))
                strength = self.coupling_strengths[i] * self.coupling_strengths[j]
                coupling += strength * (x[i] ** 2 + x[j] ** 2) * mod_i * mod_j
        
        # Enhanced exponential cross-dimensional interactions with dynamic scaling
        exp_interaction = 0.0
        for i in range(self.dim):
            for j in range(i+1, self.dim):
                exp_term = np.exp(-self.exp_params[i] * (x[i] - x[j])**2) * (1.0 + 0.3 * np.sin(i + j))
                exp_interaction += exp_term * (x[i] + x[j])**2
        
        # Enhanced adaptive noise injection with time-varying amplitude and chaotic modulation
        noise = 0.0
        for i in range(self.dim):
            amp = 0.3 + 0.2 * np.sin(0.4 * i + 2.0) + 0.1 * np.cos(i * 0.6)
            noise += amp * np.random.normal(0, 1) * (1.0 + 0.2 * np.sin(i * 0.3))
        
        # Combined function with enhanced dynamic scaling and additional complexity terms
        total = 1.0 * chaos + 1.5 * saddle + 0.8 * coupling + 0.5 * exp_interaction + 0.4 * noise
        
        return total