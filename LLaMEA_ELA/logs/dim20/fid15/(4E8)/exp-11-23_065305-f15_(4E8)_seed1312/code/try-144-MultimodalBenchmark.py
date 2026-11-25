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
        
        # Introduce a large mutation: significantly modified coefficients and frequencies to increase difficulty
        result *= 1.1 + 0.05 * np.sin(np.sum(x) * 2)
        result += 0.05 * np.sum(np.sin(12 * x) * np.cos(8 * x)) / self.dim
        
        # Add a new chaotic component with high-frequency oscillations and complex coupling
        chaotic_component = 0.3 * np.sum(np.sin(10 * x) * np.cos(13 * x) + 
                                       0.2 * np.sin(15 * x) * np.cos(7 * x) +
                                       0.1 * np.sin(20 * x) * np.cos(5 * x)) / self.dim
        result += chaotic_component
        
        # Add a new multi-modal radial basis function with variable scale and chaotic modulation
        multi_modal_rbf = 0.25 * np.sum(np.exp(-np.sum((x - np.sin(3 * x))**2, axis=0) / (2 * self.dim)) *
                                       np.exp(-np.sum((x - np.cos(4 * x))**2, axis=0) / (2 * self.dim)) *
                                       np.exp(-np.sum((x - np.tan(2 * x))**2, axis=0) / (2 * self.dim))) / self.dim
        result += multi_modal_rbf
        
        # Add a new polynomial interaction term with higher-order chaotic modulation
        high_order_poly = 0.15 * np.sum(x**10 + x**9 + 0.5 * x**8 + 0.3 * x**7) / self.dim
        result += high_order_poly
        
        # Add a new complex cross-dimensional coupling with higher frequency chaotic modulation
        complex_cross_dim = 0.4 * np.sum(np.sin(2 * x[:-1] - x[1:]) * np.cos(3 * x[:-1] + x[1:]) +
                                         0.2 * np.sin(4 * x[:-1]) * np.cos(6 * x[1:]) +
                                         0.1 * np.cos(5 * x[:-1]) * np.sin(7 * x[1:])) / (self.dim - 1)
        result += complex_cross_dim
        
        # Add a new chaotic component with extremely high frequency oscillations and multi-scale coupling
        ultra_chaotic = 0.4 * np.sum(np.sin(25 * x) * np.cos(30 * x) + 
                                   0.3 * np.sin(35 * x) * np.cos(20 * x) +
                                   0.2 * np.sin(40 * x) * np.cos(15 * x) +
                                   0.1 * np.sin(50 * x) * np.cos(10 * x)) / self.dim
        result += ultra_chaotic
        
        # Add a new hyper-chaotic radial basis function with multiple nested components
        hyper_rbf = 0.3 * np.sum(np.exp(-np.sum((x - np.sin(5 * x))**2, axis=0) / (2 * self.dim)) *
                                np.exp(-np.sum((x - np.cos(7 * x))**2, axis=0) / (2 * self.dim)) *
                                np.exp(-np.sum((x - np.tan(3 * x))**2, axis=0) / (2 * self.dim)) *
                                np.exp(-np.sum((x - np.sinh(2 * x))**2, axis=0) / (2 * self.dim))) / self.dim
        result += hyper_rbf
        
        # Add a new higher-order interaction term with exponentially increasing complexity
        high_order_interaction = 0.2 * np.sum(x[:-1]**5 * x[1:]**3 + x[:-1]**3 * x[1:]**5) / (self.dim - 1)
        result += high_order_interaction
        
        # Add a new fractal-like coupling term with self-similar chaotic behavior
        fractal_coupling = 0.25 * np.sum(np.sin(10 * x) * np.cos(10 * x) + 
                                        0.3 * np.sin(20 * x) * np.cos(20 * x) +
                                        0.1 * np.sin(30 * x) * np.cos(30 * x)) / self.dim
        result += fractal_coupling
        
        # Add a new multi-dimensional chaotic phase modulation with variable scaling
        phase_modulation = 0.35 * np.sum(np.sin(8 * x + 0.5 * np.sin(12 * x)) * 
                                        np.cos(6 * x + 0.3 * np.cos(9 * x))) / self.dim
        result += phase_modulation
        
        # Add a new chaotic polynomial with variable exponents and multi-scale behavior
        variable_poly = 0.18 * np.sum(x**12 + x**11 + 0.7 * x**10 + 0.5 * x**9 + 0.3 * x**8) / self.dim
        result += variable_poly
        
        # Add a new complex cross-dimensional interaction with chaotic modulation and multiple scales
        multi_scale_cross = 0.5 * np.sum(np.sin(3 * x[:-1] - 2 * x[1:]) * np.cos(4 * x[:-1] + 3 * x[1:]) +
                                        0.25 * np.sin(5 * x[:-1]) * np.cos(7 * x[1:]) +
                                        0.15 * np.cos(6 * x[:-1]) * np.sin(8 * x[1:]) +
                                        0.1 * np.sin(9 * x[:-1]) * np.cos(11 * x[1:])) / (self.dim - 1)
        result += multi_scale_cross
        
        return float(result)