import numpy as np

class FractalMultimodalBenchmark:
    def __init__(self, dim):
        self.dim = dim
    
    def f(self, x):
        # Ensure x is within bounds
        x = np.clip(x, -5.0, 5.0)
        
        # Initialize result
        result = 0.0
        
        # Enhanced fractal component with multi-scale self-similarity
        for i in range(self.dim):
            # Create complex fractal behavior using multiple trigonometric layers
            fractal_term = (np.sin(x[i]) + 
                           0.7 * np.sin(3 * x[i]) + 
                           0.4 * np.sin(9 * x[i]) + 
                           0.2 * np.sin(27 * x[i]))
            result += fractal_term**2
        
        # Stronger frequency modulation with chaotic elements
        for i in range(self.dim):
            # Chaotic frequency modulation using nested sinusoids
            freq_mod = np.sin(15 * np.sin(5 * np.sin(x[i]))) * np.cos(11 * np.cos(3 * np.cos(x[i])))
            result += 1.2 * freq_mod
        
        # Enhanced cross-dimensional interaction with non-linear coupling
        for i in range(self.dim - 1):
            # Non-linear nested coupling with varying strength
            coupling = np.exp(-0.2 * (x[i]**2 + x[i+1]**2)) * np.sin(8 * x[i] * x[i+1]) * np.cos(3 * x[i] + x[i+1])
            result += 0.6 * coupling
        
        # Complex polynomial fractal component
        for i in range(self.dim):
            # High-order polynomial with chaotic behavior
            poly_term = 0.05 * x[i]**8 - 0.3 * x[i]**6 + 0.7 * x[i]**4 - 0.9 * x[i]**2 + 0.1 * np.sin(10 * x[i])
            result += poly_term
        
        # Additional chaotic recursive-like structure
        for i in range(self.dim):
            # Recursive behavior with multiple exponential decays
            recursive = (np.exp(-0.1 * x[i]**2) * np.sin(20 * x[i]) + 
                        0.5 * np.exp(-0.05 * x[i]**2) * np.cos(15 * x[i]))
            result += 0.4 * recursive
        
        # Add multi-scale ridge structures
        for i in range(self.dim):
            ridge = 0.3 * np.sin(50 * x[i]) * np.exp(-0.01 * x[i]**2)
            result += ridge
        
        # Introduce stochastic perturbations to increase complexity
        stochastic_perturbation = 0.0
        for i in range(self.dim):
            stochastic_perturbation += np.sin(7 * x[i] + np.random.rand()) * np.cos(4 * x[i] + np.random.rand())
        result += 0.3 * stochastic_perturbation
        
        # Add a highly non-linear, multi-modal component
        for i in range(self.dim):
            multimodal = (np.sin(25 * x[i]) + 
                         0.5 * np.sin(75 * x[i]) + 
                         0.2 * np.sin(125 * x[i]))
            result += 0.8 * multimodal**3
        
        # Add a global scaling factor to control difficulty
        global_scale = 1.0 + 0.5 * np.sin(np.sum(x) / self.dim)
        result *= global_scale
        
        # Normalize by dimension to keep scale reasonable
        result /= self.dim
        
        return result