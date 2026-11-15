import numpy as np

class ChaoticMultimodalBenchmark:
    def __init__(self, dim):
        self.dim = dim
        
    def f(self, x):
        # Ensure x is within bounds [-5, 5]
        x = np.clip(x, -5.0, 5.0)
        
        # Base quadratic component
        quadratic = np.sum(x**2)
        
        # Enhanced chaotic sinusoidal perturbations with modified frequencies and exponential damping
        chaotic = 0
        for i in range(self.dim):
            chaotic += (np.sin(11 * x[i]) * np.cos(7 * x[i]) * np.tan(0.3 * x[i]) * 
                       np.exp(-0.03 * x[i]**2) * np.sin(0.15 * x[i]**3))
        
        # Higher-order saddle point structure with modified exponents and trigonometric coupling
        saddle = 0
        for i in range(self.dim):
            saddle += (x[i]**6 - 4 * x[i]**4 + 3 * x[i]**2) * np.cos(0.4 * x[i])
        
        # Complex cross-term interactions with modified polynomial degrees and trigonometric coupling
        cross = 0
        for i in range(self.dim):
            for j in range(i+1, self.dim):
                cross += 0.15 * x[i] * x[j] * (x[i]**4 + x[j]**4) * np.cos(0.3 * (x[i]**2 + x[j]**2))
        
        # Additional chaotic interference term with modified trigonometric and polynomial components
        interference = 0
        for i in range(self.dim):
            for j in range(i+1, min(i+3, self.dim)):  # Reduced interaction for better control
                interference += 0.08 * np.sin(3 * x[i] + 2 * x[j]) * (x[i]**2 + x[j]**2) * np.exp(-0.08 * (x[i] - x[j])**2)
        
        # Hyperbolic and logarithmic perturbations with modified scaling factors
        hyperbolic = 0
        for i in range(self.dim):
            hyperbolic += np.log(1 + 0.5 * np.abs(x[i])) * np.tanh(x[i]**2) * np.sin(0.25 * x[i]**4)
        
        # Additional higher-order polynomial and trigonometric coupling with adjusted weights
        high_order = 0
        for i in range(self.dim):
            high_order += 0.03 * x[i]**7 * np.cos(0.15 * x[i]**3) * np.sin(0.08 * x[i])
        
        # Logarithmic coupling between dimensions to increase complexity
        log_coupling = 0
        for i in range(self.dim):
            for j in range(i+1, self.dim):
                log_coupling += 0.1 * np.log(1 + np.abs(x[i] * x[j])) * np.sin(0.2 * (x[i] + x[j]))
        
        return quadratic + chaotic + saddle + cross + interference + hyperbolic + high_order + log_coupling