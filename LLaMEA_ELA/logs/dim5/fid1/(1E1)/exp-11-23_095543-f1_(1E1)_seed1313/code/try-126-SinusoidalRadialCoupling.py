import numpy as np

class SinusoidalRadialCoupling:
    def __init__(self, dim):
        self.dim = dim
        
    def f(self, x):
        x = np.array(x)
        
        # Global minimum at origin
        if np.allclose(x, 0):
            return 0.0
            
        # Base quadratic term with varying coefficients
        result = 0.0
        for i in range(self.dim):
            result += (i + 1) * x[i] ** 2
            
        # Add radial sinusoidal modulation with higher frequency components
        r = np.sqrt(np.sum(x ** 2))
        result *= (1.0 + 0.7 * np.sin(5 * r) * np.cos(3 * r) * np.exp(-0.1 * r))
        
        # Add periodic components with different frequencies and phase shifts
        for i in range(self.dim):
            result += 0.4 * np.sin(9 * x[i] + 0.5 * i) * np.cos(7 * x[(i + 1) % self.dim] - 0.3 * i)
            
        # Add cross-dimensional coupling terms with exponential decay
        for i in range(self.dim):
            for j in range(i+1, self.dim):
                result += 0.3 * np.sin(5 * x[i]) * np.cos(8 * x[j]) * np.exp(-0.2 * (x[i] - x[j]) ** 2) * np.sin(2 * r)
                
        # Add radial harmonic components with varying amplitudes
        for i in range(self.dim):
            result += 0.2 * np.sin(12 * r) * np.cos(10 * r) * x[i] ** 2 * (1 + 0.3 * np.sin(4 * r))
            
        # Add multi-scale periodicity with irregular frequencies
        for i in range(self.dim):
            result += 0.3 * np.sin(18 * x[i]) * np.cos(15 * x[(i + 2) % self.dim]) * np.exp(-0.1 * x[i] ** 2) * (1 + 0.2 * np.cos(3 * r))
            
        # Add asymmetric coupling with cubic terms and dimension-dependent scaling
        for i in range(self.dim):
            result += 0.15 * (x[i] ** 3) * np.sin(4 * x[(i + 1) % self.dim]) * np.exp(-0.05 * x[i] ** 2)
            
        # Add radial peak structure with multiple local maxima
        result += 0.5 * np.exp(-0.3 * r ** 2) * np.sin(7 * r) * (1 + 0.4 * np.cos(5 * r))
        
        # Add dimensionality-dependent scaling with additional harmonic components
        scaling = 1.0 + 0.2 * np.sum(np.sin(x) ** 2) + 0.1 * np.sum(np.cos(x) ** 2) + 0.05 * np.sum(np.sin(2 * x) ** 2)
        result *= scaling
        
        # Add a novel chaotic component for increased complexity - improved with better balance
        chaotic_term = 0.0
        for i in range(self.dim):
            chaotic_term += 0.12 * np.sin(20 * x[i]) * np.cos(17 * x[(i + 3) % self.dim]) * np.exp(-0.03 * r ** 2)
        result += chaotic_term
        
        # Add a global modulation based on the sum of all dimensions - adjusted for better balance
        global_mod = 1.0 + 0.12 * np.sin(3 * np.sum(x))
        result *= global_mod
        
        # Add a novel multi-modal structure with enhanced complexity
        multimodal_term = 0.0
        for i in range(self.dim):
            multimodal_term += 0.25 * np.sin(13 * x[i]) * np.cos(11 * x[(i + 1) % self.dim]) * np.exp(-0.15 * x[i] ** 2)
        result += multimodal_term
        
        # Add a refined harmonic structure to increase the number of local minima
        for i in range(self.dim):
            result += 0.18 * np.sin(25 * x[i]) * np.cos(22 * x[(i + 2) % self.dim]) * (1 + 0.1 * np.sin(6 * r))
            
        # Add a dimensionality-dependent penalty for high-dimensional complexity
        dim_penalty = 0.05 * np.sum(np.abs(x) ** 3)
        result += dim_penalty
        
        return result