import numpy as np

class MultimodalBenchmark:
    def __init__(self, dim):
        self.dim = dim
        
    def f(self, x):
        # Normalize input to [-1, 1] for stability
        x_norm = x / 5.0
        
        # Base polynomial term with varying exponents
        term1 = np.sum(x_norm**4)
        
        # High-frequency trigonometric components with amplitude modulation
        term2 = 0.5 * np.sum(np.sin(20 * x_norm) * np.cos(12 * x_norm) * np.exp(-0.5 * x_norm**2))
        
        # Logarithmic-modulated sinusoids for increased complexity
        term3 = 0.3 * np.sum(np.log(1 + 0.1 * np.abs(x_norm)) * np.sin(10 * np.pi * x_norm))
        
        # Asymmetric cross-dimensional coupling with different interaction strengths
        interaction = 0
        for i in range(self.dim - 1):
            if i % 2 == 0:
                interaction += x_norm[i] * (x_norm[i + 1]**3) * np.sin(3 * np.pi * x_norm[i])
            else:
                interaction += (x_norm[i]**2) * x_norm[i + 1] * np.cos(5 * np.pi * x_norm[i + 1])
        term4 = 0.25 * interaction
        
        # Polynomial with trigonometric modulation and varying degrees
        term5 = 0.4 * np.sum((x_norm**6) * np.cos(7 * np.pi * x_norm))
        
        # Non-uniform shift of global minimum with asymmetric scaling
        shift = np.array([0.3, -0.2, 0.1] + [0.05] * (self.dim - 3)) if self.dim > 3 else np.array([0.3, -0.2])
        term6 = 0.3 * np.sum((x_norm - shift[:self.dim])**3)
        
        # Chaotic exponential terms with varying decay rates
        term7 = 0.2 * np.sum(np.exp(-3 * np.abs(x_norm)) * np.sin(15 * x_norm))
        
        # Higher-order interaction with logarithmic scaling
        log_interaction = 0
        for i in range(self.dim - 2):
            if i % 3 == 0:
                log_interaction += np.log(1 + np.abs(x_norm[i])) * x_norm[i + 1] * (x_norm[i + 2]**2)
        term8 = 0.15 * log_interaction
        
        # Combine all terms
        result = term1 + term2 + term3 + term4 + term5 + term6 + term7 + term8
        
        return result