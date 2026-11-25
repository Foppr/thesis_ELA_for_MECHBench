import numpy as np

class MultimodalBenchmark:
    def __init__(self, dim):
        self.dim = dim
        self.global_min = 0.0
        
    def f(self, x):
        x = np.array(x)
        
        # Normalize to [-5, 5] domain
        x = np.clip(x, -5.0, 5.0)
        
        # Enhanced nested exponential decay with multiple scales and chaotic modulation
        exp_decay = (np.exp(-np.sum(x**2) / (2 * self.dim)) * 
                    np.exp(-np.sum((x - 1)**2) / (2 * self.dim)) * 
                    np.exp(-np.sum((x + 1)**2) / (2 * self.dim)) *
                    np.exp(-np.sum((x - 2)**2) / (2 * self.dim)) *
                    np.exp(-np.sum((x + 2)**2) / (2 * self.dim)))
        
        # Multiple trigonometric coupling terms with different frequencies and phases
        trig_coupling = (np.sum(np.sin(x) * np.cos(3 * x)) + 
                        np.sum(np.sin(2 * x) * np.cos(x)) + 
                        np.sum(np.sin(0.5 * x) * np.cos(4 * x)) + 
                        np.sum(np.sin(1.5 * x) * np.cos(2.5 * x)) +
                        np.sum(np.sin(3 * x) * np.cos(0.5 * x)) +
                        np.sum(np.sin(0.7 * x) * np.cos(3.2 * x))) / self.dim
        
        # Enhanced exponential modulation with polynomial interaction and chaotic component
        exponential_mod = np.sum(np.exp(-x**2) * (np.sin(x) + 0.5 * np.cos(2 * x) + 0.3 * np.sin(3 * x) + 
                                                  0.1 * np.sin(7 * x) * np.cos(5 * x))) / self.dim
        
        # Higher-order polynomial and logarithmic terms for complexity with chaotic interaction
        poly_term = (np.sum(x**6) / (6 * self.dim) + 
                    np.sum(x**4) / (4 * self.dim) + 
                    np.sum(x**2) / (2 * self.dim) +
                    0.5 * np.sum(x**8) / (8 * self.dim))
        log_term = np.sum(np.log(1 + x**6)) / self.dim
        
        # Enhanced cross-dimensional interaction terms with chaotic coupling
        cross_dim = 0.5 * np.sum(np.sin(x[:-1] - x[1:]) + 0.3 * np.cos(x[:-1] + x[1:]) +
                                0.2 * np.sin(2 * x[:-1]) * np.cos(3 * x[1:]) +
                                0.1 * np.cos(4 * x[:-1]) * np.sin(5 * x[1:])) / (self.dim - 1)
        
        # Global minimum with chaotic behavior around it
        result = exp_decay * (trig_coupling + exponential_mod + poly_term + log_term + cross_dim)
        
        # Add high-frequency radial component for increased multimodality with chaotic modulation
        radius = np.sqrt(np.sum(x**2))
        radial_component = 0.5 * np.sin(18 * radius) * np.exp(-radius / 4) * np.sin(2 * radius)
        result += radial_component
        
        # Add a nested structure with multiple local minima using higher frequency components and chaotic modulation
        nested_term = 0.3 * np.sum(np.sin(10 * x) * np.cos(4 * x) + 0.5 * np.sin(5 * x) * np.cos(7 * x) +
                                  0.2 * np.sin(12 * x) * np.cos(3 * x) + 0.1 * np.sin(8 * x) * np.cos(6 * x)) / self.dim
        result += nested_term
        
        # Add a chaotic shift to the global minimum to make optimization harder with multiple components
        shift = 0.1 * np.sum(np.sin(x) * np.cos(2 * x) * np.exp(-x**2) + 
                           0.05 * np.sin(3 * x) * np.cos(4 * x) * np.exp(-x**4)) / self.dim
        result += shift
        
        # Add a new chaotic radial basis function component for increased multimodality
        rbf_component = 0.2 * np.sum(np.exp(-np.sum((x - np.sin(x))**2, axis=0) / (2 * self.dim))) / self.dim
        result += rbf_component
        
        # Add a cubic coupling term for enhanced complexity
        cubic_coupling = 0.1 * np.sum(x[:-1]**3 * x[1:] + x[:-1] * x[1:]**3) / (self.dim - 1)
        result += cubic_coupling
        
        # Add chaotic hyperbolic tangent and sech components for additional complexity
        tanh_component = 0.05 * np.sum(np.tanh(x) * np.sech(x)) / self.dim
        result += tanh_component
        
        # Add a new frequency-modulated sine wave component with chaotic phase shifts
        freq_mod = 0.15 * np.sum(np.sin(15 * x + 0.2 * np.sin(7 * x))) / self.dim
        result += freq_mod
        
        # Add a power-law decay with exponential modulation for long-range interactions
        power_decay = 0.08 * np.sum(x**(-1.5) * np.exp(-x**2)) / self.dim
        result += power_decay
        
        # Add a chaotic Lorentz-like attractor component in the fitness landscape
        lorentz_component = 0.03 * np.sum(np.sin(4 * x) * np.cos(3 * x) + 
                                         np.cos(5 * x) * np.sin(2 * x)) / self.dim
        result += lorentz_component
        
        # Add a new multi-scale chaotic component with multiple frequencies and amplitudes
        multi_scale = 0.12 * np.sum(np.sin(20 * x) * np.cos(8 * x) * 
                                  np.exp(-x**2) + 
                                  0.3 * np.sin(9 * x) * np.cos(11 * x) * 
                                  np.exp(-x**4)) / self.dim
        result += multi_scale
        
        return float(result)