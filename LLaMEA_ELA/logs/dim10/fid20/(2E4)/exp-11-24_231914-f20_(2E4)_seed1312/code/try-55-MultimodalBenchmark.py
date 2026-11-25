import numpy as np

class MultimodalBenchmark:
    def __init__(self, dim):
        self.dim = dim
    
    def f(self, x):
        # Scale input to [-5, 5] if not already
        x = np.clip(x, -5.0, 5.0)
        
        # Quadratic basin term
        quadratic = np.sum(x**2) / self.dim
        
        # Enhanced chaotic saddle-point terms with modified hyperbolic sine interactions
        chaotic = 0.0
        for i in range(self.dim):
            # Stronger asymmetric hyperbolic sine interaction with varying coefficients
            chaotic += (1.5 * np.sinh(4.0 * x[i]) * np.exp(-0.2 * x[i]**2) + 
                       1.0 * np.cosh(3.0 * x[i]) * np.exp(-0.1 * x[i]**2))
        
        # Modified exponentially decaying correlation terms with different decay rates
        decay_corr = 0.0
        for i in range(self.dim - 1):
            decay_corr += np.exp(-0.4 * (x[i] - x[i+1])**2) * \
                         np.sin(10 * (x[i] + x[i+1])) + \
                         0.6 * np.exp(-0.8 * (x[i] - x[i+1])**2) * \
                         np.cos(7 * (x[i] + x[i+1]))
        
        # Enhanced periodic multimodal components with increased frequency and amplitude
        periodic = 0.0
        for i in range(self.dim):
            periodic += (2.0 * np.sin(25 * x[i]) ** 2 + 
                        1.5 * np.cos(20 * x[i]) ** 2 + 
                        1.2 * np.sin(15 * x[i]) ** 2)
        
        # Rugged cubic terms with stronger nonlinearity
        cubic = 0.0
        for i in range(self.dim):
            cubic += 1.0 * (x[i]**3) * np.exp(-0.15 * np.abs(x[i]))
        
        # Higher-order interaction terms with stronger coupling
        high_order = 0.0
        for i in range(self.dim - 2):
            high_order += 2.0 * (x[i] * x[i+1] * x[i+2])**2 + \
                         0.5 * (x[i]**4 + x[i+1]**4 + x[i+2]**4)
        
        # Add a global modulation term to increase landscape complexity
        modulation = 0.0
        for i in range(self.dim):
            modulation += 0.6 * np.sin(6 * x[i]) * np.cos(4 * x[i])
        
        # Combine all terms to create challenging landscape
        return quadratic + 1.0 * chaotic + 0.5 * decay_corr + 0.7 * periodic + 0.4 * cubic + 0.3 * high_order + 0.2 * modulation