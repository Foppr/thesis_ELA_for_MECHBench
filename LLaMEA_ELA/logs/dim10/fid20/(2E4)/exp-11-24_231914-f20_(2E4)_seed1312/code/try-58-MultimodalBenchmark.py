import numpy as np

class MultimodalBenchmark:
    def __init__(self, dim):
        self.dim = dim
    
    def f(self, x):
        # Scale input to [-5, 5] if not already
        x = np.clip(x, -5.0, 5.0)
        
        # Quadratic basin term
        quadratic = np.sum(x**2) / self.dim
        
        # Enhanced chaotic saddle-point terms with stronger hyperbolic sine and cosine interactions
        chaotic = 0.0
        for i in range(self.dim):
            # Stronger asymmetric hyperbolic interactions with varying coefficients
            chaotic += (2.0 * np.sinh(5.0 * x[i]) * np.exp(-0.25 * x[i]**2) + 
                       1.5 * np.cosh(4.0 * x[i]) * np.exp(-0.15 * x[i]**2))
        
        # Modified exponentially decaying correlation terms with different decay rates and enhanced interaction
        decay_corr = 0.0
        for i in range(self.dim - 1):
            decay_corr += np.exp(-0.5 * (x[i] - x[i+1])**2) * \
                         np.sin(12 * (x[i] + x[i+1])) + \
                         0.7 * np.exp(-0.9 * (x[i] - x[i+1])**2) * \
                         np.cos(8 * (x[i] + x[i+1]))
        
        # Enhanced periodic multimodal components with increased frequency and amplitude
        periodic = 0.0
        for i in range(self.dim):
            periodic += (2.5 * np.sin(30 * x[i]) ** 2 + 
                        2.0 * np.cos(25 * x[i]) ** 2 + 
                        1.8 * np.sin(20 * x[i]) ** 2)
        
        # Rugged cubic terms with stronger nonlinearity and additional noise
        cubic = 0.0
        for i in range(self.dim):
            cubic += 1.5 * (x[i]**3) * np.exp(-0.2 * np.abs(x[i]))
        
        # Higher-order interaction terms with stronger coupling and additional complexity
        high_order = 0.0
        for i in range(self.dim - 2):
            high_order += 2.5 * (x[i] * x[i+1] * x[i+2])**2 + \
                         0.7 * (x[i]**4 + x[i+1]**4 + x[i+2]**4)
        
        # Add a global modulation term to increase landscape complexity
        modulation = 0.0
        for i in range(self.dim):
            modulation += 0.8 * np.sin(7 * x[i]) * np.cos(5 * x[i])
        
        # Global minimum shifting term with enhanced nonlinearity
        shift = 0.0
        for i in range(self.dim):
            shift += 0.4 * np.sin(0.6 * x[i])**2
        
        # Combine all terms to create challenging landscape
        return quadratic + 1.2 * chaotic + 0.7 * decay_corr + 0.9 * periodic + 0.5 * cubic + 0.4 * high_order + 0.3 * modulation + 0.2 * shift