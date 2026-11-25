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
        radial_component = 0.5 * np.sin(15 * radius) * np.exp(-radius / 4) * np.sin(2 * radius)
        result += radial_component
        
        # Add a nested structure with multiple local minima using higher frequency components and chaotic modulation
        nested_term = 0.3 * np.sum(np.sin(9 * x) * np.cos(4 * x) + 0.5 * np.sin(5 * x) * np.cos(7 * x) +
                                  0.2 * np.sin(11 * x) * np.cos(3 * x) + 0.1 * np.sin(8 * x) * np.cos(6 * x)) / self.dim
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
        
        # Add a new chaotic hyperbolic tangent component for additional multimodality
        tanh_component = 0.15 * np.sum(np.tanh(5 * x) * np.sin(8 * x)) / self.dim
        result += tanh_component
        
        # Add a fourth-order polynomial interaction term with chaotic modulation
        quartic_interaction = 0.05 * np.sum(x[:-1]**4 + x[1:]**4 + 0.3 * x[:-1]**2 * x[1:]**2) / (self.dim - 1)
        result += quartic_interaction
        
        # Add a new chaotic sine-cosine product term with variable phase
        phase_coupling = 0.2 * np.sum(np.sin(6 * x) * np.cos(9 * x) + 0.4 * np.sin(4 * x) * np.cos(11 * x)) / self.dim
        result += phase_coupling
        
        # Add a new complex radial basis function with multi-scale chaotic modulation
        multi_scale_rbf = 0.1 * np.sum(np.exp(-np.sum((x - np.sin(2 * x))**2, axis=0) / (2 * self.dim)) * 
                                      np.exp(-np.sum((x - np.cos(3 * x))**2, axis=0) / (2 * self.dim))) / self.dim
        result += multi_scale_rbf
        
        # Add a new chaotic component with variable frequency modulation for better fitness
        var_freq_component = 0.1 * np.sum(np.sin(5 * x + np.sin(3 * x)) * np.cos(7 * x + np.cos(2 * x))) / self.dim
        result += var_freq_component
        
        # Add a modified chaotic radial basis function with different scaling for better balance
        mod_rbf = 0.15 * np.sum(np.exp(-np.sum((x - np.sin(0.5 * x))**2, axis=0) / (self.dim))) / self.dim
        result += mod_rbf
        
        # Add a new hyperbolic component with chaotic interaction
        hyperbolic_component = 0.1 * np.sum(np.tanh(3 * x + np.sin(x)) * np.cos(5 * x + np.cos(2 * x))) / self.dim
        result += hyperbolic_component
        
        # Add a modified nested structure with higher frequency components and chaotic modulation
        mod_nested = 0.25 * np.sum(np.sin(12 * x) * np.cos(5 * x) + 0.4 * np.sin(7 * x) * np.cos(9 * x) +
                                  0.15 * np.sin(10 * x) * np.cos(4 * x) + 0.08 * np.sin(6 * x) * np.cos(8 * x)) / self.dim
        result += mod_nested
        
        # Introduce a small mutation: Modify the radial component's frequency and amplitude for increased complexity
        mutated_radial = 0.7 * np.sin(18 * radius) * np.exp(-radius / 3.5) * np.sin(2.5 * radius)
        result += mutated_radial
        
        # Introduce a small mutation: Adjust the nested term's coefficients and frequencies
        mutated_nested = 0.35 * np.sum(np.sin(10 * x) * np.cos(3.5 * x) + 0.45 * np.sin(4.5 * x) * np.cos(8 * x) +
                                     0.25 * np.sin(12 * x) * np.cos(2.5 * x) + 0.12 * np.sin(7.5 * x) * np.cos(5.5 * x)) / self.dim
        result += mutated_nested
        
        # Introduce a small mutation: Modify the exponential modulation with altered coefficients
        mutated_exp_mod = np.sum(np.exp(-x**2) * (np.sin(x) + 0.6 * np.cos(2 * x) + 0.35 * np.sin(3 * x) + 
                                                  0.12 * np.sin(7 * x) * np.cos(5 * x))) / self.dim
        result += mutated_exp_mod
        
        return float(result)