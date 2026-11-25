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
                    np.exp(-np.sum((x - 1.2)**2) / (2 * self.dim)) * 
                    np.exp(-np.sum((x + 1.5)**2) / (2 * self.dim)) *
                    np.exp(-np.sum((x - 2.3)**2) / (2 * self.dim)) *
                    np.exp(-np.sum((x + 2.7)**2) / (2 * self.dim)))
        
        # Multiple trigonometric coupling terms with different frequencies and phases
        trig_coupling = (np.sum(np.sin(1.3 * x) * np.cos(2.7 * x)) + 
                        np.sum(np.sin(1.8 * x) * np.cos(1.4 * x)) + 
                        np.sum(np.sin(0.6 * x) * np.cos(3.8 * x)) + 
                        np.sum(np.sin(1.9 * x) * np.cos(2.1 * x)) +
                        np.sum(np.sin(2.5 * x) * np.cos(0.8 * x)) +
                        np.sum(np.sin(0.4 * x) * np.cos(3.1 * x))) / self.dim
        
        # Enhanced exponential modulation with polynomial interaction and chaotic component
        exponential_mod = np.sum(np.exp(-x**2) * (np.sin(1.2 * x) + 0.6 * np.cos(1.8 * x) + 0.35 * np.sin(2.7 * x) + 
                                                  0.12 * np.sin(6.3 * x) * np.cos(4.7 * x))) / self.dim
        
        # Higher-order polynomial and logarithmic terms for complexity with chaotic interaction
        poly_term = (np.sum(x**6) / (6 * self.dim) + 
                    np.sum(x**4) / (4 * self.dim) + 
                    np.sum(x**2) / (2 * self.dim) +
                    0.55 * np.sum(x**8) / (8 * self.dim))
        log_term = np.sum(np.log(1 + x**6)) / self.dim
        
        # Enhanced cross-dimensional interaction terms with chaotic coupling
        cross_dim = 0.55 * np.sum(np.sin(0.9 * x[:-1] - 1.1 * x[1:]) + 0.32 * np.cos(1.2 * x[:-1] + 0.8 * x[1:]) +
                                0.23 * np.sin(1.8 * x[:-1]) * np.cos(2.9 * x[1:]) +
                                0.11 * np.cos(3.4 * x[:-1]) * np.sin(4.6 * x[1:])) / (self.dim - 1)
        
        # Global minimum with chaotic behavior around it
        result = exp_decay * (trig_coupling + exponential_mod + poly_term + log_term + cross_dim)
        
        # Add high-frequency radial component for increased multimodality with chaotic modulation
        radius = np.sqrt(np.sum(x**2))
        radial_component = 0.55 * np.sin(16 * radius) * np.exp(-radius / 3.8) * np.sin(2.2 * radius)
        result += radial_component
        
        # Add a nested structure with multiple local minima using higher frequency components and chaotic modulation
        nested_term = 0.33 * np.sum(np.sin(9.5 * x) * np.cos(3.8 * x) + 0.52 * np.sin(4.7 * x) * np.cos(6.9 * x) +
                                  0.21 * np.sin(10.8 * x) * np.cos(2.7 * x) + 0.12 * np.sin(7.3 * x) * np.cos(5.4 * x)) / self.dim
        result += nested_term
        
        # Add a chaotic shift to the global minimum to make optimization harder with multiple components
        shift = 0.11 * np.sum(np.sin(1.1 * x) * np.cos(1.9 * x) * np.exp(-x**2) + 
                           0.055 * np.sin(2.7 * x) * np.cos(3.8 * x) * np.exp(-x**4)) / self.dim
        result += shift
        
        # Add a new chaotic radial basis function component for increased multimodality
        rbf_component = 0.21 * np.sum(np.exp(-np.sum((x - np.sin(1.3 * x))**2, axis=0) / (2 * self.dim))) / self.dim
        result += rbf_component
        
        # Add a cubic coupling term for enhanced complexity
        cubic_coupling = 0.11 * np.sum(x[:-1]**3 * x[1:] + x[:-1] * x[1:]**3) / (self.dim - 1)
        result += cubic_coupling
        
        # Add a new chaotic hyperbolic tangent component for additional multimodality
        tanh_component = 0.16 * np.sum(np.tanh(4.8 * x) * np.sin(7.9 * x)) / self.dim
        result += tanh_component
        
        # Add a fourth-order polynomial interaction term with chaotic modulation
        quartic_interaction = 0.055 * np.sum(x[:-1]**4 + x[1:]**4 + 0.32 * x[:-1]**2 * x[1:]**2) / (self.dim - 1)
        result += quartic_interaction
        
        # Add a new chaotic sine-cosine product term with variable phase
        phase_coupling = 0.21 * np.sum(np.sin(5.8 * x) * np.cos(9.3 * x) + 0.41 * np.sin(3.9 * x) * np.cos(10.7 * x)) / self.dim
        result += phase_coupling
        
        # Add a new complex radial basis function with multi-scale chaotic modulation
        multi_scale_rbf = 0.11 * np.sum(np.exp(-np.sum((x - np.sin(1.8 * x))**2, axis=0) / (2 * self.dim)) * 
                                      np.exp(-np.sum((x - np.cos(2.9 * x))**2, axis=0) / (2 * self.dim))) / self.dim
        result += multi_scale_rbf
        
        # Introduce a small mutation: slightly modified coefficients and frequencies to increase difficulty
        result *= 1.04 + 0.018 * np.sin(np.sum(x))
        result += 0.031 * np.sum(np.sin(9.7 * x) * np.cos(6.8 * x)) / self.dim
        
        return float(result)