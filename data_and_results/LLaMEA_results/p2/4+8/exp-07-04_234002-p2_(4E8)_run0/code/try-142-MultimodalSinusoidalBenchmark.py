import numpy as np

class MultimodalSinusoidalBenchmark:
    def __init__(self, dim):
        self.dim = dim
        self.global_min = 0.0
        
    def f(self, x):
        # Ensure x is within bounds [-5, 5]
        x = np.clip(x, -5.0, 5.0)
        
        # Compute the multimodal function with nested sinusoidal components
        result = 0.0
        
        # Main nested sinusoidal contribution with varying frequencies and polynomial terms
        for i in range(self.dim):
            # Nested sinusoidal terms with varying interaction strengths
            nested_sin = np.sin(2.0 * x[i]) * np.cos(1.5 * x[i]) * np.sin(0.7 * x[i])
            result += 1.5 * nested_sin + 0.2 * x[i]**2 + 0.03 * x[i]**3 + 0.005 * x[i]**4 + 0.001 * x[i]**6
            
        # Add complex interaction terms with nested coupling
        for i in range(self.dim):
            for j in range(i+1, self.dim):
                # Complex interaction with multiple sinusoidal components
                interaction = (0.1 * np.sin(2.5 * x[i]) * np.cos(1.8 * x[j]) + 
                              0.05 * np.sin(3.2 * x[i] + 1.1 * x[j]) * 
                              np.cos(0.9 * x[i] - 1.3 * x[j]) + 
                              0.02 * x[i] * x[j] * np.sin(1.4 * x[i] + x[j]))
                result += interaction
                
        # Add adaptive scaling with multiple polynomial and logarithmic components
        poly_sum = np.sum(x**2) + 0.1 * np.sum(x**3) + 0.05 * np.sum(x**4) + 0.01 * np.sum(x**5)
        log_term = np.log(1.0 + 0.2 * np.sum(x**2))
        adaptive_scale = 1.0 + 0.5 * poly_sum + 0.2 * np.sum(x**6) + 0.05 * np.sum(x**8) + 0.01 * log_term
        
        # Add fractal-like chaotic perturbations with multiple frequency components
        chaotic_perturbation = 1.0
        for i in range(self.dim):
            # Multiple chaotic components with different frequencies and amplitudes
            chaotic_perturbation += (0.05 * np.sin(20.0 * x[i]) * np.cos(17.0 * x[i]) + 
                                   0.03 * np.sin(28.0 * x[i]) * np.cos(23.0 * x[i]) + 
                                   0.02 * np.sin(35.0 * x[i]**2) + 
                                   0.01 * np.sin(42.0 * x[i]**3))
        
        # Combine all components with adaptive scaling
        result = result * adaptive_scale * chaotic_perturbation
        
        # Add a final complex correction term for increased multimodality
        correction = 0.0
        for i in range(self.dim):
            for j in range(i+1, self.dim):
                correction += 0.005 * np.sin(5.0 * x[i] + 3.0 * x[j]) * np.cos(4.0 * x[i] - 2.0 * x[j])
        
        result += correction
        
        return result