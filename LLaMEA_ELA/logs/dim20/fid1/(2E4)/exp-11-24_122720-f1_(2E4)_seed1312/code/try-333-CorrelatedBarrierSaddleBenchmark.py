import numpy as np

class CorrelatedBarrierSaddleBenchmark:
    def __init__(self, dim):
        self.dim = dim
        # Initialize correlation decay parameters
        self.decay_rates = np.random.uniform(0.1, 1.0, dim)
        # Initialize barrier strengths
        self.barrier_strengths = np.random.uniform(1.0, 5.0, dim)
        # Initialize saddle point positions
        self.saddle_positions = np.random.uniform(-3.0, 3.0, dim)
        # Initialize exponential decay base
        self.decay_base = np.random.uniform(0.5, 0.95, dim)
        
    def f(self, x):
        # Ensure x is within bounds [-5, 5]
        x = np.clip(x, -5.0, 5.0)
        
        # Correlated exponential decay component
        correlation = 0
        for i in range(self.dim):
            decay_term = np.exp(-self.decay_rates[i] * np.abs(x[i]))
            correlation += decay_term
        
        # Logarithmic barrier component
        barrier = 0
        for i in range(self.dim):
            # Add logarithmic barrier near boundaries
            barrier += self.barrier_strengths[i] * (np.log(np.abs(x[i]) + 1) + 
                                                   np.log(5.0 - np.abs(x[i]) + 1))
        
        # Saddle point attractor component
        saddle = 0
        for i in range(self.dim):
            # Hyperbolic tangent saddle with position-dependent scaling
            pos_diff = x[i] - self.saddle_positions[i]
            saddle += 0.5 * np.tanh(pos_diff) * (1 + 0.3 * np.sin(i))
        
        # Cross-dimension coupling with exponential decay
        coupling = 0
        for i in range(self.dim):
            for j in range(i+1, self.dim):
                # Exponentially decaying interaction based on dimension indices
                distance = np.abs(x[i] - x[j])
                coupling += (self.decay_base[i] ** (j-i)) * np.sin(distance)
        
        # Multi-scale sinusoidal modulation
        modulation = 0
        for i in range(self.dim):
            modulation += np.sin(2.0 * x[i]) + 0.5 * np.sin(4.0 * x[i]) + 0.2 * np.sin(8.0 * x[i])
        
        # Combine all components with dimensionality scaling
        result = (1.5 * correlation + 
                 2.0 * barrier + 
                 1.0 * saddle + 
                 0.8 * coupling + 
                 0.5 * modulation)
        
        return result