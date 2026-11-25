import numpy as np

class MultimodalBenchmark:
    def __init__(self, dim):
        self.dim = dim
    
    def f(self, x):
        # Scale input to [-5, 5] if not already
        x = np.clip(x, -5.0, 5.0)
        
        # Quadratic basin term
        quadratic = np.sum(x**2) / self.dim
        
        # Chaotic saddle-point terms with hyperbolic sine interactions
        chaotic = 0.0
        for i in range(self.dim):
            # Asymmetric hyperbolic sine interaction
            chaotic += np.sinh(3 * x[i]) * np.exp(-0.1 * x[i]**2) + \
                       0.5 * np.cosh(2 * x[i]) * np.exp(-0.05 * x[i]**2)
        
        # Exponentially decaying correlation terms
        decay_corr = 0.0
        for i in range(self.dim - 1):
            decay_corr += np.exp(-0.5 * (x[i] - x[i+1])**2) * \
                         np.sin(10 * (x[i] + x[i+1]))
        
        # Add periodic multimodal components with varying frequencies
        periodic = 0.0
        for i in range(self.dim):
            periodic += (np.sin(15 * x[i]) ** 2 + 
                        0.6 * np.cos(12 * x[i]) ** 2 + 
                        0.3 * np.sin(8 * x[i]) ** 2)
        
        # Add asymmetric cubic terms for ruggedness
        cubic = 0.0
        for i in range(self.dim):
            cubic += 0.5 * (x[i]**3) * np.exp(-0.1 * np.abs(x[i]))
        
        # Add higher-order interaction terms with varying weights
        high_order = 0.0
        for i in range(self.dim - 2):
            high_order += (x[i] * x[i+1] * x[i+2])**2 + \
                         0.2 * (x[i]**4 + x[i+1]**4 + x[i+2]**4)
        
        # Combine all terms to create challenging landscape
        return quadratic + 0.7 * chaotic + 0.3 * decay_corr + 0.5 * periodic + 0.2 * cubic + 0.1 * high_order